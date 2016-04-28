.. -*- coding: utf-8; mode: rst -*-

.. _API-remove-irq:

==========
remove_irq
==========

*man remove_irq(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
