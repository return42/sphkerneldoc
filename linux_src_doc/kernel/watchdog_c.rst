.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/watchdog.c

.. _`watchdog_nmi_stop`:

watchdog_nmi_stop
=================

.. c:function:: void watchdog_nmi_stop( void)

    Stop the watchdog for reconfiguration

    :param void:
        no arguments
    :type void: 

.. _`watchdog_nmi_stop.the-reconfiguration-steps-are`:

The reconfiguration steps are
-----------------------------

\ :c:func:`watchdog_nmi_stop`\ ;
\ :c:func:`update_variables`\ ;
\ :c:func:`watchdog_nmi_start`\ ;

.. _`watchdog_nmi_start`:

watchdog_nmi_start
==================

.. c:function:: void watchdog_nmi_start( void)

    Start the watchdog after reconfiguration

    :param void:
        no arguments
    :type void: 

.. _`watchdog_nmi_start.description`:

Description
-----------

Counterpart to \ :c:func:`watchdog_nmi_stop`\ .

The following variables have been updated in \ :c:func:`update_variables`\  and

.. _`watchdog_nmi_start.contain-the-currently-valid-configuration`:

contain the currently valid configuration
-----------------------------------------

- watchdog_enabled
- watchdog_thresh
- watchdog_cpumask

.. _`lockup_detector_update_enable`:

lockup_detector_update_enable
=============================

.. c:function:: void lockup_detector_update_enable( void)

    Update the sysctl enable bit

    :param void:
        no arguments
    :type void: 

.. _`lockup_detector_update_enable.description`:

Description
-----------

Caller needs to make sure that the NMI/perf watchdogs are off, so this
can't race with \ :c:func:`watchdog_nmi_disable`\ .

.. _`touch_softlockup_watchdog_sched`:

touch_softlockup_watchdog_sched
===============================

.. c:function:: notrace void touch_softlockup_watchdog_sched( void)

    touch watchdog on scheduler stalls

    :param void:
        no arguments
    :type void: 

.. _`touch_softlockup_watchdog_sched.description`:

Description
-----------

Call when the scheduler may have stalled for legitimate reasons
preventing the watchdog task from executing - e.g. the scheduler
entering idle state.  This should only be used for scheduler events.
Use \ :c:func:`touch_softlockup_watchdog`\  for everything else.

.. _`lockup_detector_cleanup`:

lockup_detector_cleanup
=======================

.. c:function:: void lockup_detector_cleanup( void)

    Cleanup after cpu hotplug or sysctl changes

    :param void:
        no arguments
    :type void: 

.. _`lockup_detector_cleanup.description`:

Description
-----------

Caller must not hold the cpu hotplug rwsem.

.. _`lockup_detector_soft_poweroff`:

lockup_detector_soft_poweroff
=============================

.. c:function:: void lockup_detector_soft_poweroff( void)

    Interface to stop lockup detector(s)

    :param void:
        no arguments
    :type void: 

.. _`lockup_detector_soft_poweroff.description`:

Description
-----------

Special interface for parisc. It prevents lockup detector warnings from
the default \ :c:func:`pm_poweroff`\  function which busy loops forever.

.. This file was automatic generated / don't edit.

