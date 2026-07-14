"""Logging Configuration Module"""
import logging
import sys
import json
from typing import Any
from datetime import datetime
from config import settings


class JSONFormatter(logging.Formatter):
    """JSON Formatter for structured logging"""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON"""
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if record.exc_text:
            log_data["exc_text"] = record.exc_text
        
        return json.dumps(log_data)


class PlainFormatter(logging.Formatter):
    """Plain text formatter for development"""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as plain text"""
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        return (
            f"[{timestamp}] {record.levelname:8} "
            f"[{record.name}:{record.lineno}] {record.getMessage()}"
        )


def setup_logging() -> logging.Logger:
    """Setup logging configuration"""
    
    # Create logger
    logger = logging.getLogger("phoenix_ai_os")
    logger.setLevel(settings.LOG_LEVEL)
    
    # Remove existing handlers
    logger.handlers = []
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(settings.LOG_LEVEL)
    
    # Choose formatter
    if settings.LOG_FORMAT == "json":
        formatter = JSONFormatter()
    else:
        formatter = PlainFormatter()
    
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


# Global logger instance
logger = setup_logging()
