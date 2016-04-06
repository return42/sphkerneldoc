
.. _API-pci-try-reset-function:

======================
pci_try_reset_function
======================

*man pci_try_reset_function(9)*

*4.6.0-rc1*

quiesce and reset a PCI device function


Synopsis
========

.. c:function:: int pci_try_reset_function( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to reset


Description
===========

Same as above, except return -EAGAIN if unable to lock device.
