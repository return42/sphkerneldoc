.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-task-stopped:

=================
wait_task_stopped
=================

*man wait_task_stopped(9)*

*4.6.0-rc5*

Wait for ``TASK_STOPPED`` or ``TASK_TRACED``


Synopsis
========

.. c:function:: int wait_task_stopped( struct wait_opts * wo, int ptrace, struct task_struct * p )

Arguments
=========

``wo``
    wait options

``ptrace``
    is the wait for ptrace

``p``
    task to wait for


Description
===========

Handle ``sys_wait4`` work for ``p`` in state ``TASK_STOPPED`` or
``TASK_TRACED``.


CONTEXT
=======

read_lock( ``tasklist_lock``), which is released if return value is
non-zero. Also, grabs and releases ``p``->sighand->siglock.


RETURNS
=======

0 if wait condition didn't exist and search for other wait conditions
should continue. Non-zero return, -errno on failure and ``p``'s pid on
success, implies that tasklist_lock is released and wait condition
search should terminate.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
