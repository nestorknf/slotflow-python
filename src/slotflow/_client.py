from __future__ import annotations

from typing import Optional

from ._http import AsyncHTTPClient, SyncHTTPClient
from ._resources import (
    AsyncAvailabilityResource,
    AsyncBookingsResource,
    AsyncHumansResource,
    AsyncScheduleOverridesResource,
    AsyncSlotsResource,
    AsyncWebhooksResource,
    AvailabilityResource,
    BookingsResource,
    HumansResource,
    ScheduleOverridesResource,
    SlotsResource,
    WebhooksResource,
)


class Slotflow:
    """Synchronous Slotflow API client.

    Usage::

        from slotflow import Slotflow

        client = Slotflow(api_key="sk_live_...")
        humans = client.humans.list()
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> None:
        self._http = SyncHTTPClient(api_key, base_url=base_url, timeout=timeout)
        self.humans = HumansResource(self._http)
        self.availability = AvailabilityResource(self._http)
        self.slots = SlotsResource(self._http)
        self.bookings = BookingsResource(self._http)
        self.schedule_overrides = ScheduleOverridesResource(self._http)
        self.webhooks = WebhooksResource(self._http)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._http.close()

    def __enter__(self) -> Slotflow:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncSlotflow:
    """Asynchronous Slotflow API client.

    Usage::

        from slotflow import AsyncSlotflow

        client = AsyncSlotflow(api_key="sk_live_...")
        humans = await client.humans.list()
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> None:
        self._http = AsyncHTTPClient(api_key, base_url=base_url, timeout=timeout)
        self.humans = AsyncHumansResource(self._http)
        self.availability = AsyncAvailabilityResource(self._http)
        self.slots = AsyncSlotsResource(self._http)
        self.bookings = AsyncBookingsResource(self._http)
        self.schedule_overrides = AsyncScheduleOverridesResource(self._http)
        self.webhooks = AsyncWebhooksResource(self._http)

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._http.close()

    async def __aenter__(self) -> AsyncSlotflow:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
