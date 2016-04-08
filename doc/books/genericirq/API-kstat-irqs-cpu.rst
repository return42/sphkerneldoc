
.. _API-kstat-irqs-cpu:

==============
kstat_irqs_cpu
==============

*man kstat_irqs_cpu(9)*

*4.6.0-rc1*

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

Returns the sum of interrupt counts on ``cpu`` since boot for ``irq``. The caller must ensure that the interrupt is not removed concurrently.
