from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .._http import AsyncHTTPClient, SyncHTTPClient


class BookingsResource:
    def __init__(self, http: SyncHTTPClient) -> None:
        self._http = http

    def list(
        self,
        *,
        human_id: Optional[str] = None,
        status: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """List bookings with optional filters."""
        return self._http.request(
            "GET",
            "/v1/bookings",
            params={
                "human_id": human_id,
                "status": status,
                "date_from": date_from,
                "date_to": date_to,
                "limit": limit,
                "offset": offset,
            },
        )

    def create(
        self,
        *,
        human_id: str,
        starts_at: str,
        duration: int,
        attendee_name: str,
        attendee_email: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a confirmed booking."""
        body: Dict[str, Any] = {
            "human_id": human_id,
            "starts_at": starts_at,
            "duration": duration,
            "attendee_name": attendee_name,
        }
        if attendee_email is not None:
            body["attendee_email"] = attendee_email
        if metadata is not None:
            body["metadata"] = metadata
        return self._http.request("POST", "/v1/bookings", json=body)

    def cancel(self, booking_id: str) -> Dict[str, Any]:
        """Cancel a booking."""
        return self._http.request("DELETE", f"/v1/bookings/{booking_id}")


class AsyncBookingsResource:
    def __init__(self, http: AsyncHTTPClient) -> None:
        self._http = http

    async def list(
        self,
        *,
        human_id: Optional[str] = None,
        status: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """List bookings with optional filters."""
        return await self._http.request(
            "GET",
            "/v1/bookings",
            params={
                "human_id": human_id,
                "status": status,
                "date_from": date_from,
                "date_to": date_to,
                "limit": limit,
                "offset": offset,
            },
        )

    async def create(
        self,
        *,
        human_id: str,
        starts_at: str,
        duration: int,
        attendee_name: str,
        attendee_email: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a confirmed booking."""
        body: Dict[str, Any] = {
            "human_id": human_id,
            "starts_at": starts_at,
            "duration": duration,
            "attendee_name": attendee_name,
        }
        if attendee_email is not None:
            body["attendee_email"] = attendee_email
        if metadata is not None:
            body["metadata"] = metadata
        return await self._http.request("POST", "/v1/bookings", json=body)

    async def cancel(self, booking_id: str) -> Dict[str, Any]:
        """Cancel a booking."""
        return await self._http.request("DELETE", f"/v1/bookings/{booking_id}")
