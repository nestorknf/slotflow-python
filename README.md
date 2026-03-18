# Slotflow Python SDK

The official Python SDK for the [Slotflow API](https://slotflow.dev) — scheduling infrastructure for AI agents.

[![PyPI version](https://img.shields.io/pypi/v/slotflow.svg)](https://pypi.org/project/slotflow/)
[![Python 3.8+](https://img.shields.io/pypi/pyversions/slotflow.svg)](https://pypi.org/project/slotflow/)

## Installation

```bash
pip install slotflow
```

## Quick Start

```python
from slotflow import Slotflow

client = Slotflow(api_key="sk_live_...")

# Create a human
human = client.humans.create(
    name="Alice Smith",
    timezone="America/New_York",
)

# Set their availability (Mon-Fri, 9am-5pm, 30/60 min meetings)
client.availability.set(
    human["id"],
    working_days=[1, 2, 3, 4, 5],
    work_start="09:00",
    work_end="17:00",
    meeting_durations=[30, 60],
)

# Find available slots
slots = client.slots.list(
    human["id"],
    date_from="2026-03-20",
    date_to="2026-03-25",
    duration=30,
)

# Book a slot
booking = client.bookings.create(
    human_id=human["id"],
    starts_at=slots["slots"][0]["starts_at"],
    duration=30,
    attendee_name="Bob Jones",
    attendee_email="bob@example.com",
)
```

## Async Support

```python
from slotflow import AsyncSlotflow

client = AsyncSlotflow(api_key="sk_live_...")
humans = await client.humans.list()
```

## Resources

### Humans

```python
# List all humans
response = client.humans.list()

# Create a human
human = client.humans.create(
    name="Alice Smith",
    timezone="America/New_York",
    email="alice@example.com",  # optional
    role="Consultant",          # optional
)

# Get a human by ID
human = client.humans.get("human-id")

# Delete a human (soft delete)
client.humans.delete("human-id")
```

### Availability

```python
# Set availability (full replace)
client.availability.set(
    "human-id",
    working_days=[1, 2, 3, 4, 5],  # Mon-Fri
    work_start="09:00",
    work_end="17:00",
    meeting_durations=[30, 60],
)
```

### Slots

```python
# Get available slots
response = client.slots.list(
    "human-id",
    date_from="2026-03-20",
    date_to="2026-03-25",
    duration=30,
)

for slot in response["slots"]:
    print(f"{slot['starts_at']} — {slot['ends_at']}")
```

### Bookings

```python
# Create a booking
booking = client.bookings.create(
    human_id="human-id",
    starts_at="2026-03-20T14:00:00.000Z",
    duration=30,
    attendee_name="Bob Jones",
    attendee_email="bob@example.com",
    metadata={"lead_id": "lead_123"},
)

# List bookings
response = client.bookings.list(
    human_id="human-id",
    status="confirmed",
    limit=10,
)

# Cancel a booking
client.bookings.cancel("booking-id")
```

### Schedule Overrides

```python
# Block time (vacation)
client.schedule_overrides.create(
    "human-id",
    type="block",
    title="Vacation",
    all_day=True,
    start_date="2026-04-01",
    end_date="2026-04-05",
)

# Add extra availability (weekend overtime)
client.schedule_overrides.create(
    "human-id",
    type="open",
    title="Weekend hours",
    all_day=False,
    start_date="2026-03-22",
    start_time="10:00",
    end_time="14:00",
)

# Recurring block (weekly team meeting)
client.schedule_overrides.create(
    "human-id",
    type="block",
    title="Team standup",
    all_day=False,
    start_date="2026-03-17",
    start_time="09:00",
    end_time="09:30",
    recurrence={"freq": "weekly", "interval": 1, "days": [1]},
)

# List overrides
response = client.schedule_overrides.list("human-id")

# Delete an override
client.schedule_overrides.delete("human-id", "override-id")
```

### Webhooks

```python
# Register a webhook
webhook = client.webhooks.create(
    url="https://your-app.com/webhooks/slotflow",
    events=["booking.confirmed", "booking.cancelled"],
)

# Save the signing secret for payload verification
print(webhook["signing_secret"])  # whsec_...

# List webhooks
response = client.webhooks.list()

# Delete a webhook
client.webhooks.delete("webhook-id")
```

## Error Handling

```python
from slotflow import Slotflow, NotFoundError, ConflictError, ValidationError

client = Slotflow(api_key="sk_live_...")

try:
    booking = client.bookings.create(
        human_id="human-id",
        starts_at="2026-03-20T14:00:00.000Z",
        duration=30,
        attendee_name="Bob",
    )
except ConflictError:
    print("Slot already taken")
except ValidationError as e:
    print(f"Invalid request: {e.message}")
except NotFoundError:
    print("Human not found")
```

## Configuration

```python
client = Slotflow(
    api_key="sk_live_...",
    base_url="https://api.slotflow.dev",  # default
    timeout=30.0,                          # seconds, default
)
```

## Requirements

- Python 3.8+
- [httpx](https://www.python-httpx.org/) (installed automatically)

## Links

- [Documentation](https://docs.slotflow.dev)
- [API Reference](https://docs.slotflow.dev/api-reference)
- [Dashboard](https://app.slotflow.dev)
