.. -*- coding: utf-8; mode: rst -*-

==========
watchdog.c
==========


.. _`touch_softlockup_watchdog_sched`:

touch_softlockup_watchdog_sched
===============================

.. c:function:: void touch_softlockup_watchdog_sched ( void)

    touch watchdog on scheduler stalls

    :param void:
        no arguments



.. _`touch_softlockup_watchdog_sched.description`:

Description
-----------


Call when the scheduler may have stalled for legitimate reasons
preventing the watchdog task from executing - e.g. the scheduler
entering idle state.  This should only be used for scheduler events.
Use :c:func:`touch_softlockup_watchdog` for everything else.

