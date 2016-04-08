
.. _API-irq-chip-set-type-parent:

========================
irq_chip_set_type_parent
========================

*man irq_chip_set_type_parent(9)*

*4.6.0-rc1*

Set IRQ type on the parent interrupt


Synopsis
========

.. c:function:: int irq_chip_set_type_parent( struct irq_data * data, unsigned int type )

Arguments
=========

``data``
    Pointer to interrupt specific data

``type``
    IRQ_TYPE_{LEVEL,EDGE}_⋆ value - see include/linux/irq.h


Description
===========

Conditional, as the underlying parent chip might not implement it.
