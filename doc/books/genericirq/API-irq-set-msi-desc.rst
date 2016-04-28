.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-msi-desc:

================
irq_set_msi_desc
================

*man irq_set_msi_desc(9)*

*4.6.0-rc5*

set MSI descriptor data for an irq


Synopsis
========

.. c:function:: int irq_set_msi_desc( unsigned int irq, struct msi_desc * entry )

Arguments
=========

``irq``
    Interrupt number

``entry``
    Pointer to MSI descriptor data


Description
===========

Set the MSI descriptor entry for an irq


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
