
.. _API-audit-alloc:

===========
audit_alloc
===========

*man audit_alloc(9)*

*4.6.0-rc1*

allocate an audit context block for a task


Synopsis
========

.. c:function:: int audit_alloc( struct task_struct * tsk )

Arguments
=========

``tsk``
    task


Description
===========

Filter on the task information and allocate a per-task audit context if necessary. Doing so turns on system call auditing for the specified task. This is called from copy_process,
so no lock is needed.
