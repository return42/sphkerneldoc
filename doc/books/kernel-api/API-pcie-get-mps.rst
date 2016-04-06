
.. _API-pcie-get-mps:

============
pcie_get_mps
============

*man pcie_get_mps(9)*

*4.6.0-rc1*

get PCI Express maximum payload size


Synopsis
========

.. c:function:: int pcie_get_mps( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to query


Description
===========

Returns maximum payload size in bytes
