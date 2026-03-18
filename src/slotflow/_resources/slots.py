from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from .._http import AsyncHTTPClient, SyncHTTPClient


class SlotsResource:
    def __init__(self, http: SyncHTTPClient) -> None:
        self._http = http

    def list(
        self,
        human_id: str,
        *,
        date_from: str,
        date_to: str,
        duration: int,
    ) -> Dict[str, Any]:
        """Get available booking slots for a human."""
        return self._http.request(
            "GET",
            f"/v1/humans/{human_id}/slots",
            params={
                "date_from": date_from,
                "date_to": date_to,
                "duration": duration,
            },
        )


class AsyncSlotsResource:
    def __init__(self, http: AsyncHTTPClient) -> None:
        self._http = http

    async def list(
        self,
        human_id: str,
        *,
        date_from: str,
        date_to: str,
        duration: int,
    ) -> Dict[str, Any]:
        """Get available booking slots for a human."""
        return await self._http.request(
            "GET",
            f"/v1/humans/{human_id}/slots",
            params={
                "date_from": date_from,
                "date_to": date_to,
                "duration": duration,
            },
        )
