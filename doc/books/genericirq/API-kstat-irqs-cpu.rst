.. -*- coding: utf-8; mode: rst -*-

.. _API-kstat-irqs-cpu:

==============
kstat_irqs_cpu
==============

*man kstat_irqs_cpu(9)*

*4.6.0-rc5*

Get the statistics for an interrupt on a cpu


Synopsis
========

.. c:function:: unsigned int kstat_irqs_cpu( unsigned int irq, int cpu )

Arguments
=========

``irq``
    The interrupt number

``cpu``
    The cpu number


Description
===========

Returns the sum of interrupt counts on ``cpu`` since boot for ``irq``.
The caller must ensure that the interrupt is not removed concurrently.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
