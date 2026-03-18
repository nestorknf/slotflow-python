from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .._http import AsyncHTTPClient, SyncHTTPClient


class ScheduleOverridesResource:
    def __init__(self, http: SyncHTTPClient) -> None:
        self._http = http

    def list(self, human_id: str) -> Dict[str, Any]:
        """List all schedule overrides for a human."""
        return self._http.request("GET", f"/v1/humans/{human_id}/overrides")

    def create(
        self,
        human_id: str,
        *,
        type: str,
        title: str,
        all_day: bool,
        start_date: str,
        end_date: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        recurrence: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a schedule override (block or open)."""
        body: Dict[str, Any] = {
            "type": type,
            "title": title,
            "all_day": all_day,
            "start_date": start_date,
        }
        if end_date is not None:
            body["end_date"] = end_date
        if start_time is not None:
            body["start_time"] = start_time
        if end_time is not None:
            body["end_time"] = end_time
        if recurrence is not None:
            body["recurrence"] = recurrence
        return self._http.request(
            "POST", f"/v1/humans/{human_id}/overrides", json=body
        )

    def delete(self, human_id: str, override_id: str) -> Dict[str, Any]:
        """Delete a schedule override."""
        return self._http.request(
            "DELETE", f"/v1/humans/{human_id}/overrides/{override_id}"
        )


class AsyncScheduleOverridesResource:
    def __init__(self, http: AsyncHTTPClient) -> None:
        self._http = http

    async def list(self, human_id: str) -> Dict[str, Any]:
        """List all schedule overrides for a human."""
        return await self._http.request("GET", f"/v1/humans/{human_id}/overrides")

    async def create(
        self,
        human_id: str,
        *,
        type: str,
        title: str,
        all_day: bool,
        start_date: str,
        end_date: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        recurrence: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a schedule override (block or open)."""
        body: Dict[str, Any] = {
            "type": type,
            "title": title,
            "all_day": all_day,
            "start_date": start_date,
        }
        if end_date is not None:
            body["end_date"] = end_date
        if start_time is not None:
            body["start_time"] = start_time
        if end_time is not None:
            body["end_time"] = end_time
        if recurrence is not None:
            body["recurrence"] = recurrence
        return await self._http.request(
            "POST", f"/v1/humans/{human_id}/overrides", json=body
        )

    async def delete(self, human_id: str, override_id: str) -> Dict[str, Any]:
        """Delete a schedule override."""
        return await self._http.request(
            "DELETE", f"/v1/humans/{human_id}/overrides/{override_id}"
        )
