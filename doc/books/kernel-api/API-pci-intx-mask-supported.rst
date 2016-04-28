.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-intx-mask-supported:

=======================
pci_intx_mask_supported
=======================

*man pci_intx_mask_supported(9)*

*4.6.0-rc5*

probe for INTx masking support


Synopsis
========

.. c:function:: bool pci_intx_mask_supported( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to operate on


Description
===========

Check if the device dev support INTx masking via the config space
command word.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
