.. -*- coding: utf-8; mode: rst -*-

.. _API-threadgroup-change-begin:

========================
threadgroup_change_begin
========================

*man threadgroup_change_begin(9)*

*4.6.0-rc5*

mark the beginning of changes to a threadgroup


Synopsis
========

.. c:function:: void threadgroup_change_begin( struct task_struct * tsk )

Arguments
=========

``tsk``
    task causing the changes


Description
===========

All operations which modify a threadgroup - a new thread joining the
group, death of a member thread (the assertion of PF_EXITING) and
exec(2) dethreading the process and replacing the leader - are wrapped
by threadgroup_change_{begin|end}(). This is to provide a place which
subsystems needing threadgroup stability can hook into for
synchronization.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
