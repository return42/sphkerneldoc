.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-chip-set-type-parent:

========================
irq_chip_set_type_parent
========================

*man irq_chip_set_type_parent(9)*

*4.6.0-rc5*

Set IRQ type on the parent interrupt


Synopsis
========

.. c:function:: int irq_chip_set_type_parent( struct irq_data * data, unsigned int type )

Arguments
=========

``data``
    Pointer to interrupt specific data

``type``
    IRQ_TYPE_{LEVEL,EDGE}_* value - see include/linux/irq.h


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
