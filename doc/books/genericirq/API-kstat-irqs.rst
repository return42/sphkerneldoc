
.. _API-kstat-irqs:

==========
kstat_irqs
==========

*man kstat_irqs(9)*

*4.6.0-rc1*

Get the statistics for an interrupt


Synopsis
========

.. c:function:: unsigned int kstat_irqs( unsigned int irq )

Arguments
=========

``irq``
    The interrupt number


Description
===========

Returns the sum of interrupt counts on all cpus since boot for ``irq``. The caller must ensure that the interrupt is not removed concurrently.
