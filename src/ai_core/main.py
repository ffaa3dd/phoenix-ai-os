"""Main FastAPI Application"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import asyncio
from datetime import datetime

from config import settings
from utils.logger import logger
from agents.market_analyst import MarketAnalystAgent
from agents.risk_manager import RiskManagerAgent
from memory.working_memory import WorkingMemory
from decision_engine.engine import DecisionEngine


# Global instances
market_analyst: Optional[MarketAnalystAgent] = None
risk_manager: Optional[RiskManagerAgent] = None
working_memory: Optional[WorkingMemory] = None
decision_engine: Optional[DecisionEngine] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager"""
    # Startup
    global market_analyst, risk_manager, working_memory, decision_engine
    
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    market_analyst = MarketAnalystAgent()
    risk_manager = RiskManagerAgent()
    working_memory = WorkingMemory()
    decision_engine = DecisionEngine()
    
    logger.info("All systems initialized")
    
    yield
    
    # Shutdown
    logger.info("Shutting down")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)


from typing import Optional, Dict, Any


@app.get("/health", tags=["Health"])
async def health_check() -> Dict[str, Any]:
    """Health check endpoint
    
    Returns:
        Health status
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


@app.post("/analyze/market", tags=["Analysis"])
async def analyze_market(data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze market data
    
    Args:
        data: Market data with OHLCV
        
    Returns:
        Analysis result
    """
    try:
        if not market_analyst:
            raise HTTPException(status_code=500, detail="Market Analyst not initialized")
        
        result = await market_analyst.execute(data)
        return result.to_dict()
        
    except Exception as e:
        logger.error(f"Market analysis error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/analyze/risk", tags=["Analysis"])
async def analyze_risk(data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze trading risk
    
    Args:
        data: Trade data
        
    Returns:
        Risk analysis result
    """
    try:
        if not risk_manager:
            raise HTTPException(status_code=500, detail="Risk Manager not initialized")
        
        result = await risk_manager.execute(data)
        return result.to_dict()
        
    except Exception as e:
        logger.error(f"Risk analysis error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/decide", tags=["Decision"])
async def make_decision(analyses: Dict[str, Any]) -> Dict[str, Any]:
    """Make trading decision
    
    Args:
        analyses: Analysis results
        
    Returns:
        Decision
    """
    try:
        if not decision_engine:
            raise HTTPException(status_code=500, detail="Decision Engine not initialized")
        
        # Placeholder - in real implementation, convert analyses to AnalysisResult objects
        decision = await decision_engine.make_decision([])
        
        if decision:
            return {
                "action": decision.action,
                "confidence": decision.confidence,
                "recommended": decision.recommended,
                "reasoning": decision.reasoning
            }
        else:
            raise HTTPException(status_code=400, detail="Could not make decision")
        
    except Exception as e:
        logger.error(f"Decision error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/stats", tags=["Statistics"])
async def get_stats() -> Dict[str, Any]:
    """Get system statistics
    
    Returns:
        System stats
    """
    return {
        "market_analyst": market_analyst.get_stats() if market_analyst else None,
        "risk_manager": risk_manager.get_stats() if risk_manager else None,
        "working_memory_size": working_memory.get_size() if working_memory else 0,
        "decisions_made": len(decision_engine.decisions) if decision_engine else 0
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.AI_CORE_HOST,
        port=settings.AI_CORE_PORT,
        reload=settings.DEBUG
    )
