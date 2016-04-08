
.. _API-irq-chip-eoi-parent:

===================
irq_chip_eoi_parent
===================

*man irq_chip_eoi_parent(9)*

*4.6.0-rc1*

Invoke EOI on the parent interrupt


Synopsis
========

.. c:function:: void irq_chip_eoi_parent( struct irq_data * data )

Arguments
=========

``data``
    Pointer to interrupt specific data
