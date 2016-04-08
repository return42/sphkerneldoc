
.. _API-irq-cpu-online:

==============
irq_cpu_online
==============

*man irq_cpu_online(9)*

*4.6.0-rc1*

Invoke all irq_cpu_online functions.


Synopsis
========

.. c:function:: void irq_cpu_online( void )

Arguments
=========

``void``
    no arguments


Description
===========

Iterate through all irqs and invoke the chip.\ ``irq_cpu_online`` for each.
