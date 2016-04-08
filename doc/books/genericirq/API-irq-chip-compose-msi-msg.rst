
.. _API-irq-chip-compose-msi-msg:

========================
irq_chip_compose_msi_msg
========================

*man irq_chip_compose_msi_msg(9)*

*4.6.0-rc1*

Componse msi message for a irq chip


Synopsis
========

.. c:function:: int irq_chip_compose_msi_msg( struct irq_data * data, struct msi_msg * msg )

Arguments
=========

``data``
    Pointer to interrupt specific data

``msg``
    Pointer to the MSI message


Description
===========

For hierarchical domains we find the first chip in the hierarchy which implements the irq_compose_msi_msg callback. For non hierarchical we use the top level chip.
