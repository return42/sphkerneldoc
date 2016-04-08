
.. _API-irq-chip-set-affinity-parent:

============================
irq_chip_set_affinity_parent
============================

*man irq_chip_set_affinity_parent(9)*

*4.6.0-rc1*

Set affinity on the parent interrupt


Synopsis
========

.. c:function:: int irq_chip_set_affinity_parent( struct irq_data * data, const struct cpumask * dest, bool force )

Arguments
=========

``data``
    Pointer to interrupt specific data

``dest``
    The affinity mask to set

``force``
    Flag to enforce setting (disable online checks)


Description
===========

Conditinal, as the underlying parent chip might not implement it.
