"""Custom Exceptions Module"""


class PhoenixException(Exception):
    """Base exception for Phoenix AI OS"""
    pass


class ValidationError(PhoenixException):
    """Raised when validation fails"""
    pass


class RiskViolationError(PhoenixException):
    """Raised when risk limits are violated"""
    pass


class PolicyViolationError(PhoenixException):
    """Raised when policy is violated"""
    pass


class OrderExecutionError(PhoenixException):
    """Raised when order execution fails"""
    pass


class DatabaseError(PhoenixException):
    """Raised when database operation fails"""
    pass


class AIAnalysisError(PhoenixException):
    """Raised when AI analysis fails"""
    pass


class MemoryError(PhoenixException):
    """Raised when memory operation fails"""
    pass
