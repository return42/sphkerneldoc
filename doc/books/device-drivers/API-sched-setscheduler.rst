
.. _API-sched-setscheduler:

==================
sched_setscheduler
==================

*man sched_setscheduler(9)*

*4.6.0-rc1*

change the scheduling policy and/or RT priority of a thread.


Synopsis
========

.. c:function:: int sched_setscheduler( struct task_struct * p, int policy, const struct sched_param * param )

Arguments
=========

``p``
    the task in question.

``policy``
    new policy.

``param``
    structure containing the new RT priority.


Return
======

0 on success. An error code otherwise.

NOTE that the task may be already dead.
