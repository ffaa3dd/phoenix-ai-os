"""Working Memory Implementation"""
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid
from memory.base_memory import BaseMemory, MemoryItem
from utils.logger import logger


class WorkingMemory(BaseMemory):
    """In-memory storage for current session data"""
    
    def __init__(self, max_size: int = 100):
        """Initialize Working Memory
        
        Args:
            max_size: Maximum items to keep
        """
        super().__init__(max_size)
        logger.info(f"Working Memory initialized with max size: {max_size}")
    
    async def store(self, item_id: str, data: Dict[str, Any], 
                   metadata: Optional[Dict[str, Any]] = None) -> bool:
        """Store item in working memory
        
        Args:
            item_id: Unique identifier
            data: Data to store
            metadata: Optional metadata
            
        Returns:
            Success status
        """
        try:
            # Check if item already exists and remove it
            self.items = [item for item in self.items if item.id != item_id]
            
            # Create new item
            item = MemoryItem(
                id=item_id,
                timestamp=datetime.utcnow(),
                data=data,
                metadata=metadata or {}
            )
            
            # Add to front (most recent)
            self.items.insert(0, item)
            
            # Remove oldest if exceeding max size
            if len(self.items) > self.max_size:
                self.items.pop()
            
            logger.debug(f"Stored item {item_id} in working memory")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store in working memory: {str(e)}")
            return False
    
    async def retrieve(self, item_id: str) -> Optional[MemoryItem]:
        """Retrieve item from working memory
        
        Args:
            item_id: Unique identifier
            
        Returns:
            MemoryItem or None
        """
        try:
            for item in self.items:
                if item.id == item_id:
                    logger.debug(f"Retrieved item {item_id} from working memory")
                    return item
            
            logger.debug(f"Item {item_id} not found in working memory")
            return None
            
        except Exception as e:
            logger.error(f"Failed to retrieve from working memory: {str(e)}")
            return None
    
    async def query(self, query: Dict[str, Any]) -> List[MemoryItem]:
        """Query working memory
        
        Args:
            query: Query parameters (supports 'limit' key)
            
        Returns:
            List of matching items
        """
        try:
            limit = query.get("limit", len(self.items))
            results = self.items[:limit]
            
            logger.debug(f"Query returned {len(results)} items from working memory")
            return results
            
        except Exception as e:
            logger.error(f"Failed to query working memory: {str(e)}")
            return []
    
    async def delete(self, item_id: str) -> bool:
        """Delete item from working memory
        
        Args:
            item_id: Unique identifier
            
        Returns:
            Success status
        """
        try:
            original_length = len(self.items)
            self.items = [item for item in self.items if item.id != item_id]
            
            if len(self.items) < original_length:
                logger.debug(f"Deleted item {item_id} from working memory")
                return True
            
            logger.debug(f"Item {item_id} not found in working memory")
            return False
            
        except Exception as e:
            logger.error(f"Failed to delete from working memory: {str(e)}")
            return False
    
    def clear(self) -> None:
        """Clear all items from working memory"""
        self.items = []
        logger.info("Working Memory cleared")
