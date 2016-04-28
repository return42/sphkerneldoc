.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-next-ht-capability:

===========================
pci_find_next_ht_capability
===========================

*man pci_find_next_ht_capability(9)*

*4.6.0-rc5*

query a device's Hypertransport capabilities


Synopsis
========

.. c:function:: int pci_find_next_ht_capability( struct pci_dev * dev, int pos, int ht_cap )

Arguments
=========

``dev``
    PCI device to query

``pos``
    Position from which to continue searching

``ht_cap``
    Hypertransport capability code


Description
===========

To be used in conjunction with ``pci_find_ht_capability`` to search for
all capabilities matching ``ht_cap``. ``pos`` should always be a value
returned from ``pci_find_ht_capability``.

NB. To be 100% safe against broken PCI devices, the caller should take
steps to avoid an infinite loop.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
