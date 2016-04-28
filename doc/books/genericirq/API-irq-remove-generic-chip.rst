.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-remove-generic-chip:

=======================
irq_remove_generic_chip
=======================

*man irq_remove_generic_chip(9)*

*4.6.0-rc5*

Remove a chip


Synopsis
========

.. c:function:: void irq_remove_generic_chip( struct irq_chip_generic * gc, u32 msk, unsigned int clr, unsigned int set )

Arguments
=========

``gc``
    Generic irq chip holding all data

``msk``
    Bitmask holding the irqs to initialize relative to gc->irq_base

``clr``
    IRQ_* bits to clear

``set``
    IRQ_* bits to set


Description
===========

Remove up to 32 interrupts starting from gc->irq_base.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
