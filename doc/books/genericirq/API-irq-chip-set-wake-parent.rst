.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-chip-set-wake-parent:

========================
irq_chip_set_wake_parent
========================

*man irq_chip_set_wake_parent(9)*

*4.6.0-rc5*

Set/reset wake-up on the parent interrupt


Synopsis
========

.. c:function:: int irq_chip_set_wake_parent( struct irq_data * data, unsigned int on )

Arguments
=========

``data``
    Pointer to interrupt specific data

``on``
    Whether to set or reset the wake-up capability of this irq


Description
===========

Conditional, as the underlying parent chip might not implement it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
