.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-write-vpd:

=============
pci_write_vpd
=============

*man pci_write_vpd(9)*

*4.6.0-rc5*

Write entry to Vital Product Data


Synopsis
========

.. c:function:: ssize_t pci_write_vpd( struct pci_dev * dev, loff_t pos, size_t count, const void * buf )

Arguments
=========

``dev``
    pci device struct

``pos``
    offset in vpd space

``count``
    number of bytes to write

``buf``
    buffer containing write data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
