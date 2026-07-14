"""AI Core Configuration Module"""
import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application Settings"""
    
    # Application
    APP_NAME: str = "Phoenix AI OS - Core"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Server
    AI_CORE_HOST: str = os.getenv("AI_CORE_HOST", "0.0.0.0")
    AI_CORE_PORT: int = int(os.getenv("AI_CORE_PORT", "8000"))
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://phoenix_user:secure_password@localhost:5432/phoenix_ai_os"
    )
    
    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB: int = int(os.getenv("REDIS_DB", "0"))
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = os.getenv("LOG_FORMAT", "json")
    
    # Trading
    TRADING_MODE: str = os.getenv("TRADING_MODE", "paper")
    MAX_POSITION_SIZE: float = float(os.getenv("MAX_POSITION_SIZE", "10000"))
    MAX_DAILY_LOSS_PERCENT: float = float(os.getenv("MAX_DAILY_LOSS_PERCENT", "5"))
    RISK_PER_TRADE: float = float(os.getenv("RISK_PER_TRADE", "2"))
    CIRCUIT_BREAKER_THRESHOLD: float = float(os.getenv("CIRCUIT_BREAKER_THRESHOLD", "10"))
    
    # API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global Settings Instance
settings = Settings()
