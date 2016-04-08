
.. _API-irq-alloc-domain-generic-chips:

==============================
irq_alloc_domain_generic_chips
==============================

*man irq_alloc_domain_generic_chips(9)*

*4.6.0-rc1*

Allocate generic chips for an irq domain


Synopsis
========

.. c:function:: int irq_alloc_domain_generic_chips( struct irq_domain * d, int irqs_per_chip, int num_ct, const char * name, irq_flow_handler_t handler, unsigned int clr, unsigned int set, enum irq_gc_flags gcflags )

Arguments
=========

``d``
    irq domain for which to allocate chips

``irqs_per_chip``
    Number of interrupts each chip handles

``num_ct``
    Number of irq_chip_type instances associated with this

``name``
    Name of the irq chip

``handler``
    Default flow handler associated with these chips

``clr``
    IRQ_⋆ bits to clear in the mapping function

``set``
    IRQ_⋆ bits to set in the mapping function

``gcflags``
    Generic chip specific setup flags
