.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-chip-compose-msi-msg:

========================
irq_chip_compose_msi_msg
========================

*man irq_chip_compose_msi_msg(9)*

*4.6.0-rc5*

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

For hierarchical domains we find the first chip in the hierarchy which
implements the irq_compose_msi_msg callback. For non hierarchical we
use the top level chip.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
