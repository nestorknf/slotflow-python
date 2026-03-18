from __future__ import annotations

from typing import Any, Optional


class SlotflowError(Exception):
    """Base exception for Slotflow API errors."""

    status_code: int
    code: Optional[str]
    message: str
    body: Any

    def __init__(self, status_code: int, body: Any = None) -> None:
        self.status_code = status_code
        self.body = body
        if isinstance(body, dict) and "error" in body:
            err = body["error"]
            self.code = err.get("code")
            self.message = err.get("message", "Unknown error")
        else:
            self.code = None
            self.message = str(body) if body else f"HTTP {status_code}"
        super().__init__(self.message)


class AuthenticationError(SlotflowError):
    """401 — Missing or invalid API key."""

    def __init__(self, body: Any = None) -> None:
        super().__init__(401, body)


class PaymentRequiredError(SlotflowError):
    """402 — Plan limit reached."""

    def __init__(self, body: Any = None) -> None:
        super().__init__(402, body)


class NotFoundError(SlotflowError):
    """404 — Resource not found."""

    def __init__(self, body: Any = None) -> None:
        super().__init__(404, body)


class ConflictError(SlotflowError):
    """409 — Slot unavailable or duplicate resource."""

    def __init__(self, body: Any = None) -> None:
        super().__init__(409, body)


class ValidationError(SlotflowError):
    """422 — Validation error."""

    def __init__(self, body: Any = None) -> None:
        super().__init__(422, body)
