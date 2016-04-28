.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-disable-rom:

===============
pci_disable_rom
===============

*man pci_disable_rom(9)*

*4.6.0-rc5*

disable ROM decoding for a PCI device


Synopsis
========

.. c:function:: void pci_disable_rom( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device to disable


Description
===========

Disable ROM decoding on a PCI device by turning off the last bit in the
ROM BAR.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
