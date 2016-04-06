
.. _API-pci-intx-mask-supported:

=======================
pci_intx_mask_supported
=======================

*man pci_intx_mask_supported(9)*

*4.6.0-rc1*

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

Check if the device dev support INTx masking via the config space command word.
