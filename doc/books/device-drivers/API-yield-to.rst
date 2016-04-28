.. -*- coding: utf-8; mode: rst -*-

.. _API-yield-to:

========
yield_to
========

*man yield_to(9)*

*4.6.0-rc5*

yield the current processor to another thread in your thread group, or
accelerate that thread toward the processor it's on.


Synopsis
========

.. c:function:: int __sched yield_to( struct task_struct * p, bool preempt )

Arguments
=========

``p``
    target task

``preempt``
    whether task preemption is allowed or not


Description
===========

It's the caller's job to ensure that the target task struct can't go
away on us before we can do any checks.


Return
======

true (>0) if we indeed boosted the target task. false (0) if we failed
to boost the target. -ESRCH if there's no task to yield to.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
