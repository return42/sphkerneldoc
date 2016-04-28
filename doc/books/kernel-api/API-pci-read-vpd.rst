.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-read-vpd:

============
pci_read_vpd
============

*man pci_read_vpd(9)*

*4.6.0-rc5*

Read one entry from Vital Product Data


Synopsis
========

.. c:function:: ssize_t pci_read_vpd( struct pci_dev * dev, loff_t pos, size_t count, void * buf )

Arguments
=========

``dev``
    pci device struct

``pos``
    offset in vpd space

``count``
    number of bytes to read

``buf``
    pointer to where to store result


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
