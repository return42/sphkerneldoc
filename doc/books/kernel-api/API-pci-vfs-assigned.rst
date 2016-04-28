.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-vfs-assigned:

================
pci_vfs_assigned
================

*man pci_vfs_assigned(9)*

*4.6.0-rc5*

returns number of VFs are assigned to a guest


Synopsis
========

.. c:function:: int pci_vfs_assigned( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device


Description
===========

Returns number of VFs belonging to this device that are assigned to a
guest. If device is not a physical function returns 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
