
.. _API-yield-to:

========
yield_to
========

*man yield_to(9)*

*4.6.0-rc1*

yield the current processor to another thread in your thread group, or accelerate that thread toward the processor it's on.


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

It's the caller's job to ensure that the target task struct can't go away on us before we can do any checks.


Return
======

true (>0) if we indeed boosted the target task. false (0) if we failed to boost the target. -ESRCH if there's no task to yield to.
