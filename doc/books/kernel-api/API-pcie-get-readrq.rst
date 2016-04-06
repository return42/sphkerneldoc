
.. _API-pcie-get-readrq:

===============
pcie_get_readrq
===============

*man pcie_get_readrq(9)*

*4.6.0-rc1*

get PCI Express read request size


Synopsis
========

.. c:function:: int pcie_get_readrq( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to query


Description
===========

Returns maximum memory read request in bytes or appropriate error value.
