.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-pme-capable:

===============
pci_pme_capable
===============

*man pci_pme_capable(9)*

*4.6.0-rc5*

check the capability of PCI device to generate PME#


Synopsis
========

.. c:function:: bool pci_pme_capable( struct pci_dev * dev, pci_power_t state )

Arguments
=========

``dev``
    PCI device to handle.

``state``
    PCI state from which device will issue PME#.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
