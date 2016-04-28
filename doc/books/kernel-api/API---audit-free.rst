.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-free:

============
__audit_free
============

*man __audit_free(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
