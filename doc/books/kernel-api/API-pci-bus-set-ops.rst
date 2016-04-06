
.. _API-pci-bus-set-ops:

===============
pci_bus_set_ops
===============

*man pci_bus_set_ops(9)*

*4.6.0-rc1*

Set raw operations of pci bus


Synopsis
========

.. c:function:: struct pci_ops ⋆ pci_bus_set_ops( struct pci_bus * bus, struct pci_ops * ops )

Arguments
=========

``bus``
    pci bus struct

``ops``
    new raw operations


Description
===========

Return previous raw operations
