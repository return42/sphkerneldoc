.. -*- coding: utf-8; mode: rst -*-

.. _API-alloc-workqueue:

===============
alloc_workqueue
===============

*man alloc_workqueue(9)*

*4.6.0-rc5*

allocate a workqueue


Synopsis
========

.. c:function:: alloc_workqueue( fmt, flags, max_active, args... )

Arguments
=========

``fmt``
    printf format for the name of the workqueue

``flags``
    WQ_* flags

``max_active``
    max in-flight work items, 0 for default ``args``...: args for
    ``fmt``

``args...``
    variable arguments


Description
===========

Allocate a workqueue with the specified parameters. For detailed
information on WQ_* flags, please refer to Documentation/workqueue.txt.

The __lock_name macro dance is to guarantee that single
lock_class_key doesn't end up with different namesm, which isn't
allowed by lockdep.


RETURNS
=======

Pointer to the allocated workqueue on success, ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
