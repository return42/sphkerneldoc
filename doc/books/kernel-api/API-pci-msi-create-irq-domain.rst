.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-msi-create-irq-domain:

=========================
pci_msi_create_irq_domain
=========================

*man pci_msi_create_irq_domain(9)*

*4.6.0-rc5*

Create a MSI interrupt domain


Synopsis
========

.. c:function:: struct irq_domain * pci_msi_create_irq_domain( struct fwnode_handle * fwnode, struct msi_domain_info * info, struct irq_domain * parent )

Arguments
=========

``fwnode``
    Optional fwnode of the interrupt controller

``info``
    MSI domain info

``parent``
    Parent irq domain


Description
===========

Updates the domain and chip ops and creates a MSI interrupt domain.


Returns
=======

A domain pointer or NULL in case of failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
