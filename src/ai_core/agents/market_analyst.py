"""Market Analyst Agent"""
from typing import Dict, Any
from datetime import datetime
from agents.base_agent import BaseAgent, AgentType, AnalysisStatus, AnalysisResult
from utils.logger import logger


class MarketAnalystAgent(BaseAgent):
    """Analyzes market trends and conditions"""
    
    def __init__(self):
        """Initialize Market Analyst Agent"""
        super().__init__(AgentType.MARKET_ANALYST)
    
    def get_prompt(self) -> str:
        """Get agent prompt
        
        Returns:
            Prompt string
        """
        return """You are a Market Analyst Agent for an AI Trading System.
        
Your role:
- Analyze current market conditions
- Identify market trends (uptrend, downtrend, sideways)
- Assess market momentum
- Identify support and resistance levels
- Evaluate market volume
- Assess market volatility

Provide:
1. Market trend assessment
2. Key support/resistance levels
3. Volume analysis
4. Volatility assessment
5. Recommended action (BUY, SELL, HOLD)
6. Confidence level (0-100)

Be precise and data-driven in your analysis."""
    
    async def analyze(self, data: Dict[str, Any]) -> AnalysisResult:
        """Analyze market data
        
        Args:
            data: Market data containing OHLCV (Open, High, Low, Close, Volume)
            
        Returns:
            AnalysisResult
        """
        try:
            # Extract data
            symbol = data.get("symbol", "UNKNOWN")
            ohlcv = data.get("ohlcv", {})
            
            # Simple analysis logic
            close_price = ohlcv.get("close", 0)
            open_price = ohlcv.get("open", 0)
            high_price = ohlcv.get("high", 0)
            low_price = ohlcv.get("low", 0)
            volume = ohlcv.get("volume", 0)
            
            # Determine trend
            if close_price > open_price:
                trend = "UPTREND"
                momentum = ((close_price - open_price) / open_price * 100) if open_price > 0 else 0
            elif close_price < open_price:
                trend = "DOWNTREND"
                momentum = ((close_price - open_price) / open_price * 100) if open_price > 0 else 0
            else:
                trend = "SIDEWAYS"
                momentum = 0
            
            # Calculate volatility
            volatility = ((high_price - low_price) / open_price * 100) if open_price > 0 else 0
            
            # Determine action
            if trend == "UPTREND" and momentum > 1:
                action = "BUY"
                confidence = min(80 + abs(momentum), 100)
            elif trend == "DOWNTREND" and momentum < -1:
                action = "SELL"
                confidence = min(80 + abs(momentum), 100)
            else:
                action = "HOLD"
                confidence = 60
            
            reasoning = f"{symbol} is in {trend} with momentum {momentum:.2f}% and volatility {volatility:.2f}%"
            
            return AnalysisResult(
                agent_type=self.agent_type,
                status=AnalysisStatus.COMPLETED,
                timestamp=datetime.utcnow(),
                reasoning=reasoning,
                confidence=confidence,
                data={
                    "symbol": symbol,
                    "trend": trend,
                    "momentum": momentum,
                    "volatility": volatility,
                    "action": action,
                    "current_price": close_price,
                    "support": low_price,
                    "resistance": high_price,
                    "volume": volume
                }
            )
            
        except Exception as e:
            logger.error(
                f"Market Analyst analysis failed: {str(e)}",
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
