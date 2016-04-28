.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-enable-rom:

==============
pci_enable_rom
==============

*man pci_enable_rom(9)*

*4.6.0-rc5*

enable ROM decoding for a PCI device


Synopsis
========

.. c:function:: int pci_enable_rom( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device to enable


Description
===========

Enable ROM decoding on ``dev``. This involves simply turning on the last
bit of the PCI ROM BAR. Note that some cards may share address decoders
between the ROM and other resources, so enabling it may disable access
to MMIO registers or other card memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
