
.. _API-task-set-jobctl-pending:

=======================
task_set_jobctl_pending
=======================

*man task_set_jobctl_pending(9)*

*4.6.0-rc1*

set jobctl pending bits


Synopsis
========

.. c:function:: bool task_set_jobctl_pending( struct task_struct * task, unsigned long mask )

Arguments
=========

``task``
    target task

``mask``
    pending bits to set


Description
===========

Clear ``mask`` from ``task``->jobctl. ``mask`` must be subset of ``JOBCTL_PENDING_MASK`` | ``JOBCTL_STOP_CONSUME`` | ``JOBCTL_STOP_SIGMASK`` | ``JOBCTL_TRAPPING``. If stop signo
is being set, the existing signo is cleared. If ``task`` is already being killed or exiting, this function becomes noop.


CONTEXT
=======

Must be called with ``task``->sighand->siglock held.


RETURNS
=======

``true`` if ``mask`` is set, ``false`` if made noop because ``task`` was dying.
