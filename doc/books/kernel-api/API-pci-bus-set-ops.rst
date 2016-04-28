.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-bus-set-ops:

===============
pci_bus_set_ops
===============

*man pci_bus_set_ops(9)*

*4.6.0-rc5*

Set raw operations of pci bus


Synopsis
========

.. c:function:: struct pci_ops * pci_bus_set_ops( struct pci_bus * bus, struct pci_ops * ops )

Arguments
=========

``bus``
    pci bus struct

``ops``
    new raw operations


Description
===========

Return previous raw operations


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
