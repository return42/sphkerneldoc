.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-chip-disable-parent:

=======================
irq_chip_disable_parent
=======================

*man irq_chip_disable_parent(9)*

*4.6.0-rc5*

Disable the parent interrupt (defaults to mask if NULL)


Synopsis
========

.. c:function:: void irq_chip_disable_parent( struct irq_data * data )

Arguments
=========

``data``
    Pointer to interrupt specific data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
