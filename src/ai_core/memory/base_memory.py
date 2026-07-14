"""Base Memory Module"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class MemoryItem:
    """Memory Item Data Class"""
    id: str
    timestamp: datetime
    data: Dict[str, Any]
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = asdict(self)
        result["timestamp"] = self.timestamp.isoformat()
        return result


class BaseMemory(ABC):
    """Base class for memory systems"""
    
    def __init__(self, max_size: int = 1000):
        """Initialize memory
        
        Args:
            max_size: Maximum number of items to store
        """
        self.max_size = max_size
        self.items: List[MemoryItem] = []
    
    @abstractmethod
    async def store(self, item_id: str, data: Dict[str, Any], 
                   metadata: Optional[Dict[str, Any]] = None) -> bool:
        """Store item in memory
        
        Args:
            item_id: Unique identifier
            data: Data to store
            metadata: Optional metadata
            
        Returns:
            Success status
        """
        pass
    
    @abstractmethod
    async def retrieve(self, item_id: str) -> Optional[MemoryItem]:
        """Retrieve item from memory
        
        Args:
            item_id: Unique identifier
            
        Returns:
            MemoryItem or None
        """
        pass
    
    @abstractmethod
    async def query(self, query: Dict[str, Any]) -> List[MemoryItem]:
        """Query memory
        
        Args:
            query: Query parameters
            
        Returns:
            List of matching items
        """
        pass
    
    @abstractmethod
    async def delete(self, item_id: str) -> bool:
        """Delete item from memory
        
        Args:
            item_id: Unique identifier
            
        Returns:
            Success status
        """
        pass
    
    def get_size(self) -> int:
        """Get current memory size
        
        Returns:
            Number of items stored
        """
        return len(self.items)
    
    def is_full(self) -> bool:
        """Check if memory is full
        
        Returns:
            True if full
        """
        return len(self.items) >= self.max_size
