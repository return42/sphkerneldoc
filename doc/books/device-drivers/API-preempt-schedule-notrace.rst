
.. _API-preempt-schedule-notrace:

========================
preempt_schedule_notrace
========================

*man preempt_schedule_notrace(9)*

*4.6.0-rc1*

preempt_schedule called by tracing


Synopsis
========

.. c:function:: __visible void __sched notrace preempt_schedule_notrace( void )

Arguments
=========

``void``
    no arguments


Description
===========

The tracing infrastructure uses preempt_enable_notrace to prevent recursion and tracing preempt enabling caused by the tracing infrastructure itself. But as tracing can happen in
areas coming from userspace or just about to enter userspace, a preempt enable can occur before ``user_exit`` is called. This will cause the scheduler to be called when the system
is still in usermode.

To prevent this, the preempt_enable_notrace will use this function instead of ``preempt_schedule`` to exit user context if needed before calling the scheduler.
