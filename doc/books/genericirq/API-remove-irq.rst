
.. _API-remove-irq:

==========
remove_irq
==========

*man remove_irq(9)*

*4.6.0-rc1*

free an interrupt


Synopsis
========

.. c:function:: void remove_irq( unsigned int irq, struct irqaction * act )

Arguments
=========

``irq``
    Interrupt line to free

``act``
    irqaction for the interrupt


Description
===========

Used to remove interrupts statically setup by the early boot process.
