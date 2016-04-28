.. -*- coding: utf-8; mode: rst -*-

.. _API-pcie-get-mps:

============
pcie_get_mps
============

*man pcie_get_mps(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
