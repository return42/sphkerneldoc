.. -*- coding: utf-8; mode: rst -*-

.. _API-pcie-get-readrq:

===============
pcie_get_readrq
===============

*man pcie_get_readrq(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
