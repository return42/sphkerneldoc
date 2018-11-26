.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/watchdog_hld.c

.. _`hardlockup_detector_perf_enable`:

hardlockup_detector_perf_enable
===============================

.. c:function:: void hardlockup_detector_perf_enable( void)

    Enable the local event

    :param void:
        no arguments
    :type void: 

.. _`hardlockup_detector_perf_disable`:

hardlockup_detector_perf_disable
================================

.. c:function:: void hardlockup_detector_perf_disable( void)

    Disable the local event

    :param void:
        no arguments
    :type void: 

.. _`hardlockup_detector_perf_cleanup`:

hardlockup_detector_perf_cleanup
================================

.. c:function:: void hardlockup_detector_perf_cleanup( void)

    Cleanup disabled events and destroy them

    :param void:
        no arguments
    :type void: 

.. _`hardlockup_detector_perf_cleanup.description`:

Description
-----------

Called from \ :c:func:`lockup_detector_cleanup`\ . Serialized by the caller.

.. _`hardlockup_detector_perf_stop`:

hardlockup_detector_perf_stop
=============================

.. c:function:: void hardlockup_detector_perf_stop( void)

    Globally stop watchdog events

    :param void:
        no arguments
    :type void: 

.. _`hardlockup_detector_perf_stop.description`:

Description
-----------

Special interface for x86 to handle the perf HT bug.

.. _`hardlockup_detector_perf_restart`:

hardlockup_detector_perf_restart
================================

.. c:function:: void hardlockup_detector_perf_restart( void)

    Globally restart watchdog events

    :param void:
        no arguments
    :type void: 

.. _`hardlockup_detector_perf_restart.description`:

Description
-----------

Special interface for x86 to handle the perf HT bug.

.. _`hardlockup_detector_perf_init`:

hardlockup_detector_perf_init
=============================

.. c:function:: int hardlockup_detector_perf_init( void)

    Probe whether NMI event is available at all

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

