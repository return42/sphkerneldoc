.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-chip-set-vcpu-affinity-parent:

=================================
irq_chip_set_vcpu_affinity_parent
=================================

*man irq_chip_set_vcpu_affinity_parent(9)*

*4.6.0-rc5*

Set vcpu affinity on the parent interrupt


Synopsis
========

.. c:function:: int irq_chip_set_vcpu_affinity_parent( struct irq_data * data, void * vcpu_info )

Arguments
=========

``data``
    Pointer to interrupt specific data

``vcpu_info``
    The vcpu affinity information


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
