.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-unmap-rom:

=============
pci_unmap_rom
=============

*man pci_unmap_rom(9)*

*4.6.0-rc5*

unmap the ROM from kernel space


Synopsis
========

.. c:function:: void pci_unmap_rom( struct pci_dev * pdev, void __iomem * rom )

Arguments
=========

``pdev``
    pointer to pci device struct

``rom``
    virtual address of the previous mapping


Description
===========

Remove a mapping of a previously mapped ROM


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
