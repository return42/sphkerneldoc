
.. _API-irq-alloc-generic-chip:

======================
irq_alloc_generic_chip
======================

*man irq_alloc_generic_chip(9)*

*4.6.0-rc1*

Allocate a generic chip and initialize it


Synopsis
========

.. c:function:: struct irq_chip_generic ⋆ irq_alloc_generic_chip( const char * name, int num_ct, unsigned int irq_base, void __iomem * reg_base, irq_flow_handler_t handler )

Arguments
=========

``name``
    Name of the irq chip

``num_ct``
    Number of irq_chip_type instances associated with this

``irq_base``
    Interrupt base nr for this chip

``reg_base``
    Register base address (virtual)

``handler``
    Default flow handler associated with this chip


Description
===========

Returns an initialized irq_chip_generic structure. The chip defaults to the primary (index 0) irq_chip_type and ``handler``
