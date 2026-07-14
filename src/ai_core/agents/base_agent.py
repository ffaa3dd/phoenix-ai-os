"""Base Agent Class Module"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum
from utils.logger import logger


class AgentType(str, Enum):
    """Agent Types"""
    ARCHITECT = "architect"
    PLANNER = "planner"
    MARKET_ANALYST = "market_analyst"
    NEWS_ANALYST = "news_analyst"
    TECHNICAL_ANALYST = "technical_analyst"
    RISK_MANAGER = "risk_manager"
    CRITIC = "critic"
    REVIEWER = "reviewer"
    PORTFOLIO_MANAGER = "portfolio_manager"
    STRATEGY_EVOLUTION = "strategy_evolution"
    MARKET_PROFESSOR = "market_professor"
    DEVILS_ADVOCATE = "devils_advocate"


class AnalysisStatus(str, Enum):
    """Analysis Status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class AnalysisResult:
    """Analysis Result Data Class"""
    agent_type: AgentType
    status: AnalysisStatus
    timestamp: datetime
    reasoning: str
    confidence: float  # 0-100
    data: Dict[str, Any]
    error: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = asdict(self)
        result["agent_type"] = self.agent_type.value
        result["status"] = self.status.value
        result["timestamp"] = self.timestamp.isoformat()
        return result


class BaseAgent(ABC):
    """Base class for all AI agents"""
    
    def __init__(self, agent_type: AgentType):
        """Initialize agent
        
        Args:
            agent_type: Type of agent
        """
        self.agent_type = agent_type
        self.logger = logger
        self.analysis_count = 0
        self.success_count = 0
        self.failure_count = 0
    
    @abstractmethod
    async def analyze(self, data: Dict[str, Any]) -> AnalysisResult:
        """Analyze data and return result
        
        Args:
            data: Data to analyze
            
        Returns:
            AnalysisResult
        """
        pass
    
    @abstractmethod
    def get_prompt(self) -> str:
        """Get agent prompt
        
        Returns:
            Prompt string
        """
        pass
    
    async def execute(self, data: Dict[str, Any]) -> AnalysisResult:
        """Execute analysis with error handling
        
        Args:
            data: Data to analyze
            
        Returns:
            AnalysisResult
        """
        self.analysis_count += 1
        
        try:
            self.logger.info(
                f"Agent {self.agent_type.value} starting analysis",
                extra={"agent": self.agent_type.value}
            )
            
            result = await self.analyze(data)
            
            if result.status == AnalysisStatus.COMPLETED:
                self.success_count += 1
                self.logger.info(
                    f"Agent {self.agent_type.value} analysis completed",
                    extra={
                        "agent": self.agent_type.value,
                        "confidence": result.confidence
                    }
                )
            else:
                self.failure_count += 1
                self.logger.error(
                    f"Agent {self.agent_type.value} analysis failed",
                    extra={
                        "agent": self.agent_type.value,
                        "error": result.error
                    }
                )
            
            return result
            
        except Exception as e:
            self.failure_count += 1
            self.logger.error(
                f"Agent {self.agent_type.value} exception",
                extra={
                    "agent": self.agent_type.value,
                    "error": str(e)
                },
                exc_info=True
            )
            
            return AnalysisResult(
                agent_type=self.agent_type,
                status=AnalysisStatus.FAILED,
                timestamp=datetime.utcnow(),
                reasoning="Analysis failed with exception",
                confidence=0,
                data={},
                error=str(e)
            )
    
    def get_stats(self) -> Dict[str, Any]:
        """Get agent statistics
        
        Returns:
            Dictionary with stats
        """
        success_rate = (
            (self.success_count / self.analysis_count * 100)
            if self.analysis_count > 0
            else 0
        )
        
        return {
            "agent_type": self.agent_type.value,
            "total_analyses": self.analysis_count,
            "successful": self.success_count,
            "failed": self.failure_count,
            "success_rate": round(success_rate, 2)
        }
