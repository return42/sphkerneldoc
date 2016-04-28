.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-parent-resource:

========================
pci_find_parent_resource
========================

*man pci_find_parent_resource(9)*

*4.6.0-rc5*

return resource region of parent bus of given region


Synopsis
========

.. c:function:: struct resource * pci_find_parent_resource( const struct pci_dev * dev, struct resource * res )

Arguments
=========

``dev``
    PCI device structure contains resources to be searched

``res``
    child resource record for which parent is sought


Description
===========

For given resource region of given device, return the resource region of
parent bus the given region is contained in.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
