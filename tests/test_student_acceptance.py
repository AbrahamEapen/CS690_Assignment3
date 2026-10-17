"""Student acceptance tests, one per acceptance criterion AC-1 to AC-3.

Each expected result comes from the criterion in requirements/requirements.md,
not from the reference code. Tests call only the public functions in
``reference``, with named arguments.
"""

from reference import can_offer_to_waitlist, reservation_disposition

# Configured value for these tests only, not policy. The interview disputes the
# real grace period (Q-1: 15 minutes in INT-01:P06, 20 in INT-01:P12), so the
# criteria use a configured G and the tests must pass for any G.
GRACE_MINUTES = 12


def test_ac1_checked_in_stays_active() -> None:
    # AC-1 (R-2): checked in, status checked at G + 10 minutes after start.
    state = reservation_disposition(
        minutes_after_start=GRACE_MINUTES + 10,
        grace_minutes=GRACE_MINUTES,
        checked_in=True,
    )
    assert state == "active"


def test_ac2_staff_hold_stays_held() -> None:
    # AC-2 (R-3): not checked in, hold ends at G + 10, status checked at G + 5.
    # The check time is strictly inside the hold, so the test does not settle
    # whether a kit is still held at exactly the hold's end minute (A-1).
    state = reservation_disposition(
        minutes_after_start=GRACE_MINUTES + 5,
        grace_minutes=GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=GRACE_MINUTES + 10,
    )
    assert state == "held"


def test_ac3_unprepared_kit_not_offered() -> None:
    # AC-3 (R-4): releasable, preparation not recorded complete.
    offered = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    assert offered is False
