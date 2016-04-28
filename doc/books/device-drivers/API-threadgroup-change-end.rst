.. -*- coding: utf-8; mode: rst -*-

.. _API-threadgroup-change-end:

======================
threadgroup_change_end
======================

*man threadgroup_change_end(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
