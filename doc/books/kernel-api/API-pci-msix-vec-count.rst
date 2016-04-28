.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-msix-vec-count:

==================
pci_msix_vec_count
==================

*man pci_msix_vec_count(9)*

*4.6.0-rc5*

return the number of device's MSI-X table entries


Synopsis
========

.. c:function:: int pci_msix_vec_count( struct pci_dev * dev )

Arguments
=========

``dev``
    pointer to the pci_dev data structure of MSI-X device function This
    function returns the number of device's MSI-X table entries and
    therefore the number of MSI-X vectors device is capable of sending.
    It returns a negative errno if the device is not capable of sending
    MSI-X interrupts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
