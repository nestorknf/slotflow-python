from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .._http import AsyncHTTPClient, SyncHTTPClient


class HumansResource:
    def __init__(self, http: SyncHTTPClient) -> None:
        self._http = http

    def list(self) -> Dict[str, Any]:
        """List all active humans in the organization."""
        return self._http.request("GET", "/v1/humans")

    def create(
        self,
        *,
        name: str,
        timezone: str,
        email: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a new human."""
        body: Dict[str, Any] = {"name": name, "timezone": timezone}
        if email is not None:
            body["email"] = email
        if role is not None:
            body["role"] = role
        return self._http.request("POST", "/v1/humans", json=body)

    def get(self, human_id: str) -> Dict[str, Any]:
        """Get a human by ID with availability rules."""
        return self._http.request("GET", f"/v1/humans/{human_id}")

    def delete(self, human_id: str) -> Dict[str, Any]:
        """Soft-delete a human."""
        return self._http.request("DELETE", f"/v1/humans/{human_id}")


class AsyncHumansResource:
    def __init__(self, http: AsyncHTTPClient) -> None:
        self._http = http

    async def list(self) -> Dict[str, Any]:
        """List all active humans in the organization."""
        return await self._http.request("GET", "/v1/humans")

    async def create(
        self,
        *,
        name: str,
        timezone: str,
        email: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a new human."""
        body: Dict[str, Any] = {"name": name, "timezone": timezone}
        if email is not None:
            body["email"] = email
        if role is not None:
            body["role"] = role
        return await self._http.request("POST", "/v1/humans", json=body)

    async def get(self, human_id: str) -> Dict[str, Any]:
        """Get a human by ID with availability rules."""
        return await self._http.request("GET", f"/v1/humans/{human_id}")

    async def delete(self, human_id: str) -> Dict[str, Any]:
        """Soft-delete a human."""
        return await self._http.request("DELETE", f"/v1/humans/{human_id}")
