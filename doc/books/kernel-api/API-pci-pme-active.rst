.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-pme-active:

==============
pci_pme_active
==============

*man pci_pme_active(9)*

*4.6.0-rc5*

enable or disable PCI device's PME# function


Synopsis
========

.. c:function:: void pci_pme_active( struct pci_dev * dev, bool enable )

Arguments
=========

``dev``
    PCI device to handle.

``enable``
    'true' to enable PME# generation; 'false' to disable it.


Description
===========

The caller must verify that the device is capable of generating PME#
before calling this function with ``enable`` equal to 'true'.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
