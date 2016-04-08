
.. _API-irq-setup-generic-chip:

======================
irq_setup_generic_chip
======================

*man irq_setup_generic_chip(9)*

*4.6.0-rc1*

Setup a range of interrupts with a generic chip


Synopsis
========

.. c:function:: void irq_setup_generic_chip( struct irq_chip_generic * gc, u32 msk, enum irq_gc_flags flags, unsigned int clr, unsigned int set )

Arguments
=========

``gc``
    Generic irq chip holding all data

``msk``
    Bitmask holding the irqs to initialize relative to gc->irq_base

``flags``
    Flags for initialization

``clr``
    IRQ_⋆ bits to clear

``set``
    IRQ_⋆ bits to set


Description
===========

Set up max. 32 interrupts starting from gc->irq_base. Note, this initializes all interrupts to the primary irq_chip_type and its associated handler.
