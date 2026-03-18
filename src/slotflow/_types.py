"""TypedDict definitions for Slotflow API request and response types.

These provide IDE autocompletion and type checking but are not enforced at runtime.
All API methods return plain dicts that conform to these shapes.
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict
elif sys.version_info >= (3, 8):
    from typing import TypedDict

    from typing_extensions import NotRequired
else:
    from typing_extensions import NotRequired, TypedDict

from typing import Any, Dict, List, Literal, Optional


# --- Core types ---


class Human(TypedDict):
    id: str
    name: str
    email: Optional[str]
    role: Optional[str]
    timezone: str
    active: bool
    created_at: str


class AvailabilityRules(TypedDict):
    working_days: List[int]
    work_start: str
    work_end: str
    meeting_durations: List[int]


class HumanWithAvailability(Human):
    availability_rules: Optional[AvailabilityRules]


class Slot(TypedDict):
    starts_at: str
    ends_at: str


class SlotsResponse(TypedDict):
    human_id: str
    duration: int
    timezone: str
    slots: List[Slot]
    total: int


class Booking(TypedDict):
    id: str
    human_id: str
    starts_at: str
    ends_at: str
    duration_minutes: int
    attendee_name: str
    attendee_email: Optional[str]
    status: Literal["confirmed", "cancelled"]
    metadata: Optional[Dict[str, Any]]
    created_at: str


class RecurrenceRule(TypedDict, total=False):
    freq: Literal["weekly", "monthly"]
    interval: int
    days: List[int]
    day_of_month: int
    week: int
    day: int


class ScheduleOverride(TypedDict):
    id: str
    human_id: str
    type: Literal["block", "open"]
    title: str
    all_day: bool
    start_date: str
    end_date: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]
    recurrence: Optional[RecurrenceRule]
    created_at: str


class Webhook(TypedDict):
    id: str
    url: str
    events: List[str]
    signing_secret: str
    active: bool
    created_at: str


class DeleteResponse(TypedDict):
    deleted: bool
    id: str


class CancelBookingResponse(TypedDict):
    id: str
    status: str


# --- List responses ---


class ListHumansResponse(TypedDict):
    humans: List[Human]
    total: int


class BookingsListResponse(TypedDict):
    bookings: List[Booking]
    total: int
    limit: int
    offset: int


class ListOverridesResponse(TypedDict):
    overrides: List[ScheduleOverride]
    total: int


class ListWebhooksResponse(TypedDict):
    webhooks: List[Webhook]
    total: int
