.. -*- coding: utf-8; mode: rst -*-

.. _API-might-sleep:

===========
might_sleep
===========

*man might_sleep(9)*

*4.6.0-rc5*

annotation for functions that can sleep


Synopsis
========

.. c:function:: might_sleep(  )

Arguments
=========

None


Description
===========

this macro will print a stack trace if it is executed in an atomic
context (spinlock, irq-handler, ...).

This is a useful debugging help to be able to catch problems early and
not be bitten later when the calling function happens to sleep when it
is not supposed to.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
