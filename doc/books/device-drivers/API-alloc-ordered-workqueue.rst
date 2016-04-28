.. -*- coding: utf-8; mode: rst -*-

.. _API-alloc-ordered-workqueue:

=======================
alloc_ordered_workqueue
=======================

*man alloc_ordered_workqueue(9)*

*4.6.0-rc5*

allocate an ordered workqueue


Synopsis
========

.. c:function:: alloc_ordered_workqueue( fmt, flags, args... )

Arguments
=========

``fmt``
    printf format for the name of the workqueue

``flags``
    WQ_* flags (only WQ_FREEZABLE and WQ_MEM_RECLAIM are meaningful)
    ``args``...: args for ``fmt``

``args...``
    variable arguments


Description
===========

Allocate an ordered workqueue. An ordered workqueue executes at most one
work item at any given time in the queued order. They are implemented as
unbound workqueues with ``max_active`` of one.


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
