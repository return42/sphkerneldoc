.. -*- coding: utf-8; mode: rst -*-

.. _API-setup-irq:

=========
setup_irq
=========

*man setup_irq(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
