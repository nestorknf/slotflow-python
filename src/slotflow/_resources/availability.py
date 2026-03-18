from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from .._http import AsyncHTTPClient, SyncHTTPClient


class AvailabilityResource:
    def __init__(self, http: SyncHTTPClient) -> None:
        self._http = http

    def set(
        self,
        human_id: str,
        *,
        working_days: List[int],
        work_start: str,
        work_end: str,
        meeting_durations: List[int],
    ) -> Dict[str, Any]:
        """Set availability rules for a human (full replace)."""
        return self._http.request(
            "PUT",
            f"/v1/humans/{human_id}/availability",
            json={
                "working_days": working_days,
                "work_start": work_start,
                "work_end": work_end,
                "meeting_durations": meeting_durations,
            },
        )


class AsyncAvailabilityResource:
    def __init__(self, http: AsyncHTTPClient) -> None:
        self._http = http

    async def set(
        self,
        human_id: str,
        *,
        working_days: List[int],
        work_start: str,
        work_end: str,
        meeting_durations: List[int],
    ) -> Dict[str, Any]:
        """Set availability rules for a human (full replace)."""
        return await self._http.request(
            "PUT",
            f"/v1/humans/{human_id}/availability",
            json={
                "working_days": working_days,
                "work_start": work_start,
                "work_end": work_end,
                "meeting_durations": meeting_durations,
            },
        )
