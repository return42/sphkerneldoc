.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-msi-desc-off:

====================
irq_set_msi_desc_off
====================

*man irq_set_msi_desc_off(9)*

*4.6.0-rc5*

set MSI descriptor data for an irq at offset


Synopsis
========

.. c:function:: int irq_set_msi_desc_off( unsigned int irq_base, unsigned int irq_offset, struct msi_desc * entry )

Arguments
=========

``irq_base``
    Interrupt number base

``irq_offset``
    Interrupt number offset

``entry``
    Pointer to MSI descriptor data


Description
===========

Set the MSI descriptor entry for an irq at offset


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
