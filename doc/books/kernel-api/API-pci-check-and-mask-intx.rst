.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-check-and-mask-intx:

=======================
pci_check_and_mask_intx
=======================

*man pci_check_and_mask_intx(9)*

*4.6.0-rc5*

mask INTx on pending interrupt


Synopsis
========

.. c:function:: bool pci_check_and_mask_intx( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to operate on


Description
===========

Check if the device dev has its INTx line asserted, mask it and return
true in that case. False is returned if not interrupt was pending.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
