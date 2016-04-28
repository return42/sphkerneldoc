.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-wait-for-pending-transaction:

================================
pci_wait_for_pending_transaction
================================

*man pci_wait_for_pending_transaction(9)*

*4.6.0-rc5*

waits for pending transaction


Synopsis
========

.. c:function:: int pci_wait_for_pending_transaction( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to operate on


Description
===========

Return 0 if transaction is pending 1 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
