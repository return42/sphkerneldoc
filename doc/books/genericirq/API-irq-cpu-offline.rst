
.. _API-irq-cpu-offline:

===============
irq_cpu_offline
===============

*man irq_cpu_offline(9)*

*4.6.0-rc1*

Invoke all irq_cpu_offline functions.


Synopsis
========

.. c:function:: void irq_cpu_offline( void )

Arguments
=========

``void``
    no arguments


Description
===========

Iterate through all irqs and invoke the chip.\ ``irq_cpu_offline`` for each.
