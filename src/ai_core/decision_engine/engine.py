"""Decision Engine Module"""
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
from agents.base_agent import AnalysisResult, AnalysisStatus
from utils.logger import logger


@dataclass
class Decision:
    """Decision Data Class"""
    timestamp: datetime
    action: str  # BUY, SELL, HOLD
    confidence: float
    reasoning: str
    agent_inputs: List[AnalysisResult]
    final_score: float
    recommended: bool


class DecisionEngine:
    """Engine for making trading decisions based on agent analysis"""
    
    def __init__(self):
        """Initialize Decision Engine"""
        self.decisions: List[Decision] = []
        self.logger = logger
    
    async def make_decision(self, 
                          analyses: List[AnalysisResult],
                          risk_limit: float = 100) -> Optional[Decision]:
        """Make trading decision based on agent analyses
        
        Args:
            analyses: List of analysis results from agents
            risk_limit: Maximum acceptable risk
            
        Returns:
            Decision or None
        """
        try:
            if not analyses:
                self.logger.warning("No analyses provided to decision engine")
                return None
            
            # Filter successful analyses
            successful = [a for a in analyses if a.status == AnalysisStatus.COMPLETED]
            
            if not successful:
                self.logger.warning("No successful analyses to make decision")
                return None
            
            # Calculate weighted confidence
            total_confidence = sum(a.confidence for a in successful)
            avg_confidence = total_confidence / len(successful)
            
            # Extract actions and aggregate
            action_scores = self._aggregate_actions(successful)
            
            # Determine best action
            best_action = max(action_scores, key=action_scores.get)
            action_score = action_scores[best_action]
            
            # Build reasoning
            reasoning = f"Decision based on {len(successful)} agents. "
            reasoning += f"Top action: {best_action} with score {action_score:.2f}. "
            reasoning += f"Average confidence: {avg_confidence:.2f}"
            
            # Determine if recommended (with confidence threshold)
            recommended = avg_confidence >= 70 and action_score >= 0.6
            
            decision = Decision(
                timestamp=datetime.utcnow(),
                action=best_action,
                confidence=avg_confidence,
                reasoning=reasoning,
                agent_inputs=successful,
                final_score=action_score,
                recommended=recommended
            )
            
            self.decisions.append(decision)
            
            self.logger.info(
                f"Decision made: {best_action}",
                extra={
                    "action": best_action,
                    "confidence": avg_confidence,
                    "recommended": recommended
                }
            )
            
            return decision
            
        except Exception as e:
            self.logger.error(
                f"Decision engine failed: {str(e)}",
                exc_info=True
            )
            return None
    
    def _aggregate_actions(self, analyses: List[AnalysisResult]) -> Dict[str, float]:
        """Aggregate actions from analyses
        
        Args:
            analyses: List of analyses
            
        Returns:
            Dictionary with action scores
        """
        action_scores = {"BUY": 0, "SELL": 0, "HOLD": 0}
        
        for analysis in analyses:
            action = analysis.data.get("action", "HOLD")
            confidence = analysis.confidence / 100  # Normalize to 0-1
            
            if action in action_scores:
                action_scores[action] += confidence
        
        # Normalize
        total = sum(action_scores.values())
        if total > 0:
            for action in action_scores:
                action_scores[action] /= total
        
        return action_scores
    
    def get_decision_history(self, limit: int = 10) -> List[Decision]:
        """Get recent decision history
        
        Args:
            limit: Number of recent decisions
            
        Returns:
            List of decisions
        """
        return self.decisions[-limit:]
