.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/idle.c

.. _`sched_idle_set_state`:

sched_idle_set_state
====================

.. c:function:: void sched_idle_set_state(struct cpuidle_state *idle_state)

    Record idle state for the current CPU.

    :param struct cpuidle_state \*idle_state:
        State to record.

.. _`default_idle_call`:

default_idle_call
=================

.. c:function:: void __cpuidle default_idle_call( void)

    Default CPU idle routine.

    :param  void:
        no arguments

.. _`default_idle_call.description`:

Description
-----------

To use when the cpuidle framework cannot be used.

.. _`cpuidle_idle_call`:

cpuidle_idle_call
=================

.. c:function:: void cpuidle_idle_call( void)

    the main idle function

    :param  void:
        no arguments

.. _`cpuidle_idle_call.note`:

NOTE
----

no locks or semaphores should be used here

On archs that support TIF_POLLING_NRFLAG, is called with polling
set, and it returns with polling set.  If it ever stops polling, it
must clear the polling bit.

.. This file was automatic generated / don't edit.

