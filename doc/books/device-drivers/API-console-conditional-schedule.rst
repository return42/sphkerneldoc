.. -*- coding: utf-8; mode: rst -*-

.. _API-console-conditional-schedule:

============================
console_conditional_schedule
============================

*man console_conditional_schedule(9)*

*4.6.0-rc5*

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

If the console code is currently allowed to sleep, and if this CPU
should yield the CPU to another task, do so here.

Must be called within ``console_lock``;.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
