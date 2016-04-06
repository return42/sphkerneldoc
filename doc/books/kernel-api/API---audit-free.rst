
.. _API---audit-free:

============
__audit_free
============

*man __audit_free(9)*

*4.6.0-rc1*

free a per-task audit context


Synopsis
========

.. c:function:: void __audit_free( struct task_struct * tsk )

Arguments
=========

``tsk``
    task whose audit context block to free


Description
===========

Called from copy_process and do_exit
