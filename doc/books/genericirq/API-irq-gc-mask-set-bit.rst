.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-gc-mask-set-bit:

===================
irq_gc_mask_set_bit
===================

*man irq_gc_mask_set_bit(9)*

*4.6.0-rc5*

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

Chip has a single mask register. Values of this register are cached and
protected by gc->lock


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
