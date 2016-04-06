
.. _API-sched-setscheduler-nocheck:

==========================
sched_setscheduler_nocheck
==========================

*man sched_setscheduler_nocheck(9)*

*4.6.0-rc1*

change the scheduling policy and/or RT priority of a thread from kernelspace.


Synopsis
========

.. c:function:: int sched_setscheduler_nocheck( struct task_struct * p, int policy, const struct sched_param * param )

Arguments
=========

``p``
    the task in question.

``policy``
    new policy.

``param``
    structure containing the new RT priority.


Description
===========

Just like sched_setscheduler, only don't bother checking if the current context has permission. For example, this is needed in ``stop_machine``: we create temporary high priority
worker threads, but our caller might not have that capability.


Return
======

0 on success. An error code otherwise.
