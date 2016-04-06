
.. _API-console-conditional-schedule:

============================
console_conditional_schedule
============================

*man console_conditional_schedule(9)*

*4.6.0-rc1*

yield the CPU if required


Synopsis
========

.. c:function:: void __sched console_conditional_schedule( void )

Arguments
=========

``void``
    no arguments


Description
===========

If the console code is currently allowed to sleep, and if this CPU should yield the CPU to another task, do so here.

Must be called within ``console_lock``;.
