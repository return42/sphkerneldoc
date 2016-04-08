
.. _API-irq-force-affinity:

==================
irq_force_affinity
==================

*man irq_force_affinity(9)*

*4.6.0-rc1*

Force the irq affinity of a given irq


Synopsis
========

.. c:function:: int irq_force_affinity( unsigned int irq, const struct cpumask * cpumask )

Arguments
=========

``irq``
    Interrupt to set affinity

``cpumask``
    cpumask


Description
===========

Same as irq_set_affinity, but without checking the mask against online cpus.

Solely for low level cpu hotplug code, where we need to make per cpu interrupts affine before the cpu becomes online.
