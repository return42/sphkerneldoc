
.. _bugs:

==========================
Known Bugs And Assumptions
==========================

Interrupt Locking
    The locking in the driver is done via the global cli/sti lock. This makes for relatively poor SMP performance. Switching this to use a per device spin lock would probably
    materially improve performance.

Occasional Failures
    We have reports of occasional failures when run for very long periods of time and the driver starts to receive junk frames. At the moment the cause of this is not clear.
