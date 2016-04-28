.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-enable-sriov:

================
pci_enable_sriov
================

*man pci_enable_sriov(9)*

*4.6.0-rc5*

enable the SR-IOV capability


Synopsis
========

.. c:function:: int pci_enable_sriov( struct pci_dev * dev, int nr_virtfn )

Arguments
=========

``dev``
    the PCI device

``nr_virtfn``
    number of virtual functions to enable


Description
===========

Returns 0 on success, or negative on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
