.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-common-swizzle:

==================
pci_common_swizzle
==================

*man pci_common_swizzle(9)*

*4.6.0-rc5*

swizzle INTx all the way to root bridge


Synopsis
========

.. c:function:: u8 pci_common_swizzle( struct pci_dev * dev, u8 * pinp )

Arguments
=========

``dev``
    the PCI device

``pinp``
    pointer to the INTx pin value (1=INTA, 2=INTB, 3=INTD, 4=INTD)


Description
===========

Perform INTx swizzling for a device. This traverses through all
PCI-to-PCI bridges all the way up to a PCI root bus.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
