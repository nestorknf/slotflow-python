"""Slotflow Python SDK — scheduling infrastructure for AI agents."""

from ._client import AsyncSlotflow, Slotflow
from ._errors import (
    AuthenticationError,
    ConflictError,
    NotFoundError,
    PaymentRequiredError,
    SlotflowError,
    ValidationError,
)

__all__ = [
    "Slotflow",
    "AsyncSlotflow",
    "SlotflowError",
    "AuthenticationError",
    "PaymentRequiredError",
    "NotFoundError",
    "ConflictError",
    "ValidationError",
]

__version__ = "0.1.0"
