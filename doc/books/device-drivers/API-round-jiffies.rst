.. -*- coding: utf-8; mode: rst -*-

.. _API-round-jiffies:

=============
round_jiffies
=============

*man round_jiffies(9)*

*4.6.0-rc5*

function to round jiffies to a full second


Synopsis
========

.. c:function:: unsigned long round_jiffies( unsigned long j )

Arguments
=========

``j``
    the time in (absolute) jiffies that should be rounded


Description
===========

``round_jiffies`` rounds an absolute time in the future (in jiffies) up
or down to (approximately) full seconds. This is useful for timers for
which the exact time they fire does not matter too much, as long as they
fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire at
the same time, rather than at various times spread out. The goal of this
is to have the CPU wake up less, which saves power.

The return value is the rounded version of the ``j`` parameter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
