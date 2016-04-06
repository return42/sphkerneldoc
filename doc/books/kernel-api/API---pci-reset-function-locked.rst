
.. _API---pci-reset-function-locked:

===========================
__pci_reset_function_locked
===========================

*man __pci_reset_function_locked(9)*

*4.6.0-rc1*

reset a PCI device function while holding the ``dev`` mutex lock.


Synopsis
========

.. c:function:: int __pci_reset_function_locked( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to reset


Description
===========

Some devices allow an individual function to be reset without affecting other functions in the same device. The PCI device must be responsive to PCI config space in order to use
this function.

The device function is presumed to be unused and the caller is holding the device mutex lock when this function is called. Resetting the device will make the contents of PCI
configuration space random, so any caller of this must be prepared to reinitialise the device including MSI, bus mastering, BARs, decoding IO and memory spaces, etc.

Returns 0 if the device function was successfully reset or negative if the device doesn't support resetting a single function.
