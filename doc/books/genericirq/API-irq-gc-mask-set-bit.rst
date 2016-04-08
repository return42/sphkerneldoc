
.. _API-irq-gc-mask-set-bit:

===================
irq_gc_mask_set_bit
===================

*man irq_gc_mask_set_bit(9)*

*4.6.0-rc1*

Mask chip via setting bit in mask register


Synopsis
========

.. c:function:: void irq_gc_mask_set_bit( struct irq_data * d )

Arguments
=========

``d``
    irq_data


Description
===========

Chip has a single mask register. Values of this register are cached and protected by gc->lock
