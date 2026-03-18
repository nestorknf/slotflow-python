from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from .._http import AsyncHTTPClient, SyncHTTPClient


class WebhooksResource:
    def __init__(self, http: SyncHTTPClient) -> None:
        self._http = http

    def list(self) -> Dict[str, Any]:
        """List all registered webhooks."""
        return self._http.request("GET", "/v1/webhooks")

    def create(self, *, url: str, events: List[str]) -> Dict[str, Any]:
        """Register a webhook endpoint."""
        return self._http.request(
            "POST", "/v1/webhooks", json={"url": url, "events": events}
        )

    def delete(self, webhook_id: str) -> Dict[str, Any]:
        """Delete a webhook endpoint."""
        return self._http.request("DELETE", f"/v1/webhooks/{webhook_id}")


class AsyncWebhooksResource:
    def __init__(self, http: AsyncHTTPClient) -> None:
        self._http = http

    async def list(self) -> Dict[str, Any]:
        """List all registered webhooks."""
        return await self._http.request("GET", "/v1/webhooks")

    async def create(self, *, url: str, events: List[str]) -> Dict[str, Any]:
        """Register a webhook endpoint."""
        return await self._http.request(
            "POST", "/v1/webhooks", json={"url": url, "events": events}
        )

    async def delete(self, webhook_id: str) -> Dict[str, Any]:
        """Delete a webhook endpoint."""
        return await self._http.request("DELETE", f"/v1/webhooks/{webhook_id}")
