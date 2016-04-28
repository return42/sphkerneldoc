.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-msi-vec-count:

=================
pci_msi_vec_count
=================

*man pci_msi_vec_count(9)*

*4.6.0-rc5*

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

This function returns the number of MSI vectors a device requested via
Multiple Message Capable register. It returns a negative errno if the
device is not capable sending MSI interrupts. Otherwise, the call
succeeds and returns a power of two, up to a maximum of 2^5 (32),
according to the MSI specification.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
