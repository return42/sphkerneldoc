
.. _API-irq-chip-enable-parent:

======================
irq_chip_enable_parent
======================

*man irq_chip_enable_parent(9)*

*4.6.0-rc1*

Enable the parent interrupt (defaults to unmask if NULL)


Synopsis
========

.. c:function:: void irq_chip_enable_parent( struct irq_data * data )

Arguments
=========

``data``
    Pointer to interrupt specific data
