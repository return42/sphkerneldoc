
.. _API-irq-chip-disable-parent:

=======================
irq_chip_disable_parent
=======================

*man irq_chip_disable_parent(9)*

*4.6.0-rc1*

Disable the parent interrupt (defaults to mask if NULL)


Synopsis
========

.. c:function:: void irq_chip_disable_parent( struct irq_data * data )

Arguments
=========

``data``
    Pointer to interrupt specific data
