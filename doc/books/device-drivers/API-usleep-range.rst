.. -*- coding: utf-8; mode: rst -*-

.. _API-usleep-range:

============
usleep_range
============

*man usleep_range(9)*

*4.6.0-rc5*

Drop in replacement for udelay where wakeup is flexible


Synopsis
========

.. c:function:: void __sched usleep_range( unsigned long min, unsigned long max )

Arguments
=========

``min``
    Minimum time in usecs to sleep

``max``
    Maximum time in usecs to sleep


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
