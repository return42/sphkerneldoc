
.. _API-pcie-set-readrq:

===============
pcie_set_readrq
===============

*man pcie_set_readrq(9)*

*4.6.0-rc1*

set PCI Express maximum memory read request


Synopsis
========

.. c:function:: int pcie_set_readrq( struct pci_dev * dev, int rq )

Arguments
=========

``dev``
    PCI device to query

``rq``
    maximum memory read count in bytes valid values are 128, 256, 512, 1024, 2048, 4096


Description
===========

If possible sets maximum memory read request in bytes
