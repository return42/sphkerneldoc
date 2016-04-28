.. -*- coding: utf-8; mode: rst -*-

.. _API-work-on-cpu:

===========
work_on_cpu
===========

*man work_on_cpu(9)*

*4.6.0-rc5*

run a function in thread context on a particular cpu


Synopsis
========

.. c:function:: long work_on_cpu( int cpu, long (*fn) void *, void * arg )

Arguments
=========

``cpu``
    the cpu to run on

``fn``
    the function to run

``arg``
    the function arg


Description
===========

It is up to the caller to ensure that the cpu doesn't go offline. The
caller must not hold any locks which would prevent ``fn`` from
completing.


Return
======

The value ``fn`` returns.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
