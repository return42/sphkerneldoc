.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-unregister-driver:

=====================
pci_unregister_driver
=====================

*man pci_unregister_driver(9)*

*4.6.0-rc5*

unregister a pci driver


Synopsis
========

.. c:function:: void pci_unregister_driver( struct pci_driver * drv )

Arguments
=========

``drv``
    the driver structure to unregister


Description
===========

Deletes the driver structure from the list of registered PCI drivers,
gives it a chance to clean up by calling its ``remove`` function for
each device it was responsible for, and marks those devices as
driverless.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
