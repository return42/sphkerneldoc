
.. _API-enable-irq:

==========
enable_irq
==========

*man enable_irq(9)*

*4.6.0-rc1*

enable handling of an irq


Synopsis
========

.. c:function:: void enable_irq( unsigned int irq )

Arguments
=========

``irq``
    Interrupt to enable


Description
===========

Undoes the effect of one call to ``disable_irq``. If this matches the last disable, processing of interrupts on this IRQ line is re-enabled.

This function may be called from IRQ context only when desc->irq_data.chip->bus_lock and desc->chip->bus_sync_unlock are NULL !
