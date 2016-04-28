.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-scan-slot:

=============
pci_scan_slot
=============

*man pci_scan_slot(9)*

*4.6.0-rc5*

scan a PCI slot on a bus for devices.


Synopsis
========

.. c:function:: int pci_scan_slot( struct pci_bus * bus, int devfn )

Arguments
=========

``bus``
    PCI bus to scan

``devfn``
    slot number to scan (must have zero function.)


Description
===========

Scan a PCI slot on the specified PCI bus for devices, adding discovered
devices to the ``bus``->devices list. New devices will not have
is_added set.

Returns the number of new devices found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
