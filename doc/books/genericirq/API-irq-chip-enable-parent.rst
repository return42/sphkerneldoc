.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-chip-enable-parent:

======================
irq_chip_enable_parent
======================

*man irq_chip_enable_parent(9)*

*4.6.0-rc5*

Enable the parent interrupt (defaults to unmask if NULL)


Synopsis
========

.. c:function:: void irq_chip_enable_parent( struct irq_data * data )

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
