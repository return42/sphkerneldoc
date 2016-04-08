
.. _API-irq-get-domain-generic-chip:

===========================
irq_get_domain_generic_chip
===========================

*man irq_get_domain_generic_chip(9)*

*4.6.0-rc1*

Get a pointer to the generic chip of a hw_irq


Synopsis
========

.. c:function:: struct irq_chip_generic ⋆ irq_get_domain_generic_chip( struct irq_domain * d, unsigned int hw_irq )

Arguments
=========

``d``
    irq domain pointer

``hw_irq``
    Hardware interrupt number
