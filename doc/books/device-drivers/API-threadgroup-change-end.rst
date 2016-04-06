
.. _API-threadgroup-change-end:

======================
threadgroup_change_end
======================

*man threadgroup_change_end(9)*

*4.6.0-rc1*

mark the end of changes to a threadgroup


Synopsis
========

.. c:function:: void threadgroup_change_end( struct task_struct * tsk )

Arguments
=========

``tsk``
    task causing the changes


Description
===========

See ``threadgroup_change_begin``.
