.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-sriov-get-totalvfs:

======================
pci_sriov_get_totalvfs
======================

*man pci_sriov_get_totalvfs(9)*

*4.6.0-rc5*

- get total VFs supported on this device


Synopsis
========

.. c:function:: int pci_sriov_get_totalvfs( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI PF device


Description
===========

For a PCIe device with SRIOV support, return the PCIe SRIOV capability
value of TotalVFs or the value of driver_max_VFs if the driver reduced
it. Otherwise 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
