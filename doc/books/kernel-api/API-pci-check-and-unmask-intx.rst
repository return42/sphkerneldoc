.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-check-and-unmask-intx:

=========================
pci_check_and_unmask_intx
=========================

*man pci_check_and_unmask_intx(9)*

*4.6.0-rc5*

unmask INTx if no interrupt is pending


Synopsis
========

.. c:function:: bool pci_check_and_unmask_intx( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to operate on


Description
===========

Check if the device dev has its INTx line asserted, unmask it if not and
return true. False is returned and the mask remains active if there was
still an interrupt pending.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
