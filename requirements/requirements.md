# Part 3. Requirements, INVEST, and acceptance criteria

Evidence IDs refer to `evidence/evidence_log.md`. `G` is the lab's configured grace period in minutes. All times are whole minutes after the reservation start.

## Four requirement slices

### R-1. Release after the configured grace period

- **User story:** As a checkout desk worker, I want a reservation with no check-in and no recorded hold to become releasable only once the lab's configured grace period has passed, so that I neither give away a kit too early nor hold it indefinitely.
- **Structured requirement:** When a reservation is not checked in and has no active staff hold, the system shall report it as "held" while minutes after start is less than G, and as "releasable" once minutes after start is G or greater. G is read from lab configuration and is not fixed in the software.
- **Trace:** E-2, Q-1. The value of G stays open (Q-1); only the rule that it is configured is settled.

### R-2. Checked-in reservations stay active

- **User story:** As a student borrower who has checked in at the desk, I want my reservation to stay active after the grace period passes, so that I do not lose equipment I am already picking up.
- **Structured requirement:** When a reservation is checked in, the system shall report it as "active" at any number of minutes after start, including after G has passed.
- **Trace:** E-3.

### R-3. Staff-recorded temporary hold

- **User story:** As a checkout desk worker, I want to record a temporary hold with an end time and a reason when a late student contacts the desk, so that the kit is not released while they are on the way and we can explain the decision later.
- **Structured requirement:** When staff record a hold ending H minutes after start on a reservation that is not checked in, the system shall report it as "held" while minutes after start is less than H, even if G has passed, and shall store the hold's end time and reason with the reservation.
- **Trace:** E-1, E-4, and `Assumption` (A-1). Read together with R-1, this slice assumes a hold can only extend a reservation: if a hold ends before G, R-1 still keeps the reservation "held" until G. Clarifying questions for Jordan: if a hold ends before G, does the reservation stay held until G? Is the kit still held at exactly minute H?

### R-4. Waitlist sees only ready equipment

- **User story:** As a waitlisted student, I want to be offered a kit only when its reservation is releasable and the technicians have finished preparing it, so that I am not sent to the desk for equipment that cannot be handed out yet.
- **Structured requirement:** The system shall offer a kit to the waitlist only when its reservation is "releasable" and preparation is recorded as complete. A releasable kit without completed preparation shall not be offered.
- **Trace:** E-5, Q-2. How technicians record preparation stays open (Q-2).

## INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-1 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-2 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-3 | Pass | Pass | Pass | Pass | Fail | Pass | S: bundles hold-status behavior with storing the hold reason for later audit |
| R-4 | Fail | Pass | Pass | Fail | Pass | Pass | I: depends on a technician preparation-complete signal that does not exist yet (Q-2). E: the technician workflow cannot be sized until the technicians are interviewed |

## Three acceptance criteria

### AC-1 (R-2)

- **Given** the lab's configured grace period is G minutes, and the student has checked in for the reservation
- **When** the desk checks the reservation status at G + 10 minutes after start
- **Then** the status is "active"

### AC-2 (R-3)

- **Given** the lab's configured grace period is G minutes, the student has not checked in, and staff have recorded a hold ending at G + 10 minutes after start
- **When** the desk checks the reservation status at G + 5 minutes after start
- **Then** the status is "held"

AC-2 checks a time strictly inside the hold, so it does not settle whether a kit is still held at exactly minute H (A-1).

### AC-3 (R-4)

- **Given** a reservation whose status is "releasable", and the technicians have not recorded preparation as complete
- **When** the system checks whether the kit may be offered to the waitlist
- **Then** the kit is not offered (the check returns false)
