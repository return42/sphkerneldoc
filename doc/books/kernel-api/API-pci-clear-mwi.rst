.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-clear-mwi:

=============
pci_clear_mwi
=============

*man pci_clear_mwi(9)*

*4.6.0-rc5*

disables Memory-Write-Invalidate for device dev


Synopsis
========

.. c:function:: void pci_clear_mwi( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to disable


Description
===========

Disables PCI Memory-Write-Invalidate transaction on the device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
