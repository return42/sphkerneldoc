
.. _API-irq-chip-set-vcpu-affinity-parent:

=================================
irq_chip_set_vcpu_affinity_parent
=================================

*man irq_chip_set_vcpu_affinity_parent(9)*

*4.6.0-rc1*

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
