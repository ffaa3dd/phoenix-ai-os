"""Risk Manager Agent"""
from typing import Dict, Any
from datetime import datetime
from agents.base_agent import BaseAgent, AgentType, AnalysisStatus, AnalysisResult
from utils.logger import logger


class RiskManagerAgent(BaseAgent):
    """Evaluates and manages trading risks"""
    
    def __init__(self):
        """Initialize Risk Manager Agent"""
        super().__init__(AgentType.RISK_MANAGER)
    
    def get_prompt(self) -> str:
        """Get agent prompt
        
        Returns:
            Prompt string
        """
        return """You are a Risk Manager Agent for an AI Trading System.
        
Your role:
- Evaluate risk of proposed trades
- Calculate position sizes based on risk
- Assess portfolio risk exposure
- Monitor drawdown levels
- Enforce daily loss limits
- Manage correlation risks

Provide:
1. Risk score (0-100, where 100 is maximum risk)
2. Recommended position size
3. Maximum loss amount
4. Stop-loss level
5. Risk/Reward ratio
6. Approval recommendation (APPROVE, REJECT, CONDITIONAL)

Prioritize capital preservation over profits."""
    
    async def analyze(self, data: Dict[str, Any]) -> AnalysisResult:
        """Analyze risk of trade
        
        Args:
            data: Trade data including entry price, stop loss, etc.
            
        Returns:
            AnalysisResult
        """
        try:
            # Extract data
            symbol = data.get("symbol", "UNKNOWN")
            entry_price = data.get("entry_price", 0)
            stop_loss = data.get("stop_loss", 0)
            take_profit = data.get("take_profit", 0)
            capital = data.get("capital", 10000)
            
            # Calculate risk metrics
            risk_per_trade = 2  # percent
            account_risk = capital * (risk_per_trade / 100)
            
            if entry_price > 0 and stop_loss > 0:
                price_difference = abs(entry_price - stop_loss)
                max_shares = int(account_risk / price_difference) if price_difference > 0 else 0
            else:
                max_shares = 0
            
            # Calculate risk/reward ratio
            if entry_price > 0 and stop_loss > 0 and take_profit > 0:
                risk_distance = abs(entry_price - stop_loss)
                reward_distance = abs(take_profit - entry_price)
                risk_reward_ratio = reward_distance / risk_distance if risk_distance > 0 else 0
            else:
                risk_reward_ratio = 0
            
            # Determine risk score
            if risk_reward_ratio < 1:
                risk_score = 75
                recommendation = "CONDITIONAL"
            elif risk_reward_ratio < 1.5:
                risk_score = 50
                recommendation = "APPROVE"
            else:
                risk_score = 25
                recommendation = "APPROVE"
            
            reasoning = f"Risk/Reward ratio: {risk_reward_ratio:.2f}, Position size: {max_shares} shares"
            
            return AnalysisResult(
                agent_type=self.agent_type,
                status=AnalysisStatus.COMPLETED,
                timestamp=datetime.utcnow(),
                reasoning=reasoning,
                confidence=85,
                data={
                    "symbol": symbol,
                    "risk_score": risk_score,
                    "position_size": max_shares,
                    "max_loss": account_risk,
                    "risk_reward_ratio": risk_reward_ratio,
                    "recommendation": recommendation,
                    "stop_loss": stop_loss,
                    "take_profit": take_profit
                }
            )
            
        except Exception as e:
            logger.error(
                f"Risk Manager analysis failed: {str(e)}",
                exc_info=True
            )
            
            return AnalysisResult(
                agent_type=self.agent_type,
                status=AnalysisStatus.FAILED,
                timestamp=datetime.utcnow(),
                reasoning="Analysis failed",
                confidence=0,
                data={},
                error=str(e)
            )
