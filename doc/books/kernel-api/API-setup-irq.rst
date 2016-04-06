
.. _API-setup-irq:

=========
setup_irq
=========

*man setup_irq(9)*

*4.6.0-rc1*

setup an interrupt


Synopsis
========

.. c:function:: int setup_irq( unsigned int irq, struct irqaction * act )

Arguments
=========

``irq``
    Interrupt line to setup

``act``
    irqaction for the interrupt


Description
===========

Used to statically setup interrupts in the early boot process.
