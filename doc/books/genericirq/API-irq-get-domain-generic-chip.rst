.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-get-domain-generic-chip:

===========================
irq_get_domain_generic_chip
===========================

*man irq_get_domain_generic_chip(9)*

*4.6.0-rc5*

Get a pointer to the generic chip of a hw_irq


Synopsis
========

.. c:function:: struct irq_chip_generic * irq_get_domain_generic_chip( struct irq_domain * d, unsigned int hw_irq )

Arguments
=========

``d``
    irq domain pointer

``hw_irq``
    Hardware interrupt number


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
