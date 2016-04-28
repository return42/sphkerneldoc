.. -*- coding: utf-8; mode: rst -*-

.. _API-pcie-set-mps:

============
pcie_set_mps
============

*man pcie_set_mps(9)*

*4.6.0-rc5*

set PCI Express maximum payload size


Synopsis
========

.. c:function:: int pcie_set_mps( struct pci_dev * dev, int mps )

Arguments
=========

``dev``
    PCI device to query

``mps``
    maximum payload size in bytes valid values are 128, 256, 512, 1024,
    2048, 4096


Description
===========

If possible sets maximum payload size


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
