
.. _API-pci-msi-vec-count:

=================
pci_msi_vec_count
=================

*man pci_msi_vec_count(9)*

*4.6.0-rc1*

Return the number of MSI vectors a device can send


Synopsis
========

.. c:function:: int pci_msi_vec_count( struct pci_dev * dev )

Arguments
=========

``dev``
    device to report about


Description
===========

This function returns the number of MSI vectors a device requested via Multiple Message Capable register. It returns a negative errno if the device is not capable sending MSI
interrupts. Otherwise, the call succeeds and returns a power of two, up to a maximum of 2^5 (32), according to the MSI specification.
