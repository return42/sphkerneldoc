
.. _API-task-clear-jobctl-trapping:

==========================
task_clear_jobctl_trapping
==========================

*man task_clear_jobctl_trapping(9)*

*4.6.0-rc1*

clear jobctl trapping bit


Synopsis
========

.. c:function:: void task_clear_jobctl_trapping( struct task_struct * task )

Arguments
=========

``task``
    target task


Description
===========

If JOBCTL_TRAPPING is set, a ptracer is waiting for us to enter TRACED. Clear it and wake up the ptracer. Note that we don't need any further locking. ``task``->siglock guarantees
that ``task``->parent points to the ptracer.


CONTEXT
=======

Must be called with ``task``->sighand->siglock held.
