
.. _API-pcim-enable-device:

==================
pcim_enable_device
==================

*man pcim_enable_device(9)*

*4.6.0-rc1*

Managed ``pci_enable_device``


Synopsis
========

.. c:function:: int pcim_enable_device( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device to be initialized


Description
===========

Managed ``pci_enable_device``.
