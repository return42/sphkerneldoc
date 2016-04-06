
.. _API-pci-reenable-device:

===================
pci_reenable_device
===================

*man pci_reenable_device(9)*

*4.6.0-rc1*

Resume abandoned device


Synopsis
========

.. c:function:: int pci_reenable_device( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to be resumed


Description
===========

Note this function is a backend of pci_default_resume and is not supposed to be called by normal code, write proper resume handler and use it instead.
