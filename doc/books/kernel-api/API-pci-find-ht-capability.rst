.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-ht-capability:

======================
pci_find_ht_capability
======================

*man pci_find_ht_capability(9)*

*4.6.0-rc5*

query a device's Hypertransport capabilities


Synopsis
========

.. c:function:: int pci_find_ht_capability( struct pci_dev * dev, int ht_cap )

Arguments
=========

``dev``
    PCI device to query

``ht_cap``
    Hypertransport capability code


Description
===========

Tell if a device supports a given Hypertransport capability. Returns an
address within the device's PCI configuration space or 0 in case the
device does not support the request capability. The address points to
the PCI capability, of type PCI_CAP_ID_HT, which has a Hypertransport
capability matching ``ht_cap``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
