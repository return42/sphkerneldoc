.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/itmt.c

.. _`sched_set_itmt_support`:

sched_set_itmt_support
======================

.. c:function:: int sched_set_itmt_support( void)

    Indicate platform supports ITMT

    :param void:
        no arguments
    :type void: 

.. _`sched_set_itmt_support.description`:

Description
-----------

This function is used by the OS to indicate to scheduler that the platform
is capable of supporting the ITMT feature.

The current scheme has the pstate driver detects if the system
is ITMT capable and call sched_set_itmt_support.

This must be done only after sched_set_itmt_core_prio
has been called to set the cpus' priorities.
It must not be called with cpu hot plug lock
held as we need to acquire the lock to rebuild sched domains
later.

.. _`sched_set_itmt_support.return`:

Return
------

0 on success

.. _`sched_clear_itmt_support`:

sched_clear_itmt_support
========================

.. c:function:: void sched_clear_itmt_support( void)

    Revoke platform's support of ITMT

    :param void:
        no arguments
    :type void: 

.. _`sched_clear_itmt_support.description`:

Description
-----------

This function is used by the OS to indicate that it has
revoked the platform's support of ITMT feature.

It must not be called with cpu hot plug lock
held as we need to acquire the lock to rebuild sched domains
later.

.. _`sched_set_itmt_core_prio`:

sched_set_itmt_core_prio
========================

.. c:function:: void sched_set_itmt_core_prio(int prio, int core_cpu)

    Set CPU priority based on ITMT

    :param prio:
        Priority of cpu core
    :type prio: int

    :param core_cpu:
        The cpu number associated with the core
    :type core_cpu: int

.. _`sched_set_itmt_core_prio.description`:

Description
-----------

The pstate driver will find out the max boost frequency
and call this function to set a priority proportional
to the max boost frequency. CPU with higher boost
frequency will receive higher priority.

No need to rebuild sched domain after updating
the CPU priorities. The sched domains have no
dependency on CPU priorities.

.. This file was automatic generated / don't edit.

