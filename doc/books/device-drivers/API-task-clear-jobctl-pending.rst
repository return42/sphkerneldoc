.. -*- coding: utf-8; mode: rst -*-

.. _API-task-clear-jobctl-pending:

=========================
task_clear_jobctl_pending
=========================

*man task_clear_jobctl_pending(9)*

*4.6.0-rc5*

clear jobctl pending bits


Synopsis
========

.. c:function:: void task_clear_jobctl_pending( struct task_struct * task, unsigned long mask )

Arguments
=========

``task``
    target task

``mask``
    pending bits to clear


Description
===========

Clear ``mask`` from ``task``->jobctl. ``mask`` must be subset of
``JOBCTL_PENDING_MASK``. If ``JOBCTL_STOP_PENDING`` is being cleared,
other STOP bits are cleared together.

If clearing of ``mask`` leaves no stop or trap pending, this function
calls ``task_clear_jobctl_trapping``.


CONTEXT
=======

Must be called with ``task``->sighand->siglock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
