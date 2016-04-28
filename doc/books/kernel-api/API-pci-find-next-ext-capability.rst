.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-next-ext-capability:

============================
pci_find_next_ext_capability
============================

*man pci_find_next_ext_capability(9)*

*4.6.0-rc5*

Find an extended capability


Synopsis
========

.. c:function:: int pci_find_next_ext_capability( struct pci_dev * dev, int start, int cap )

Arguments
=========

``dev``
    PCI device to query

``start``
    address at which to start looking (0 to start at beginning of list)

``cap``
    capability code


Description
===========

Returns the address of the next matching extended capability structure
within the device's PCI configuration space or 0 if the device does not
support it. Some capabilities can occur several times, e.g., the
vendor-specific capability, and this provides a way to find them all.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
