
.. _API-pci-unregister-driver:

=====================
pci_unregister_driver
=====================

*man pci_unregister_driver(9)*

*4.6.0-rc1*

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

Deletes the driver structure from the list of registered PCI drivers, gives it a chance to clean up by calling its ``remove`` function for each device it was responsible for, and
marks those devices as driverless.
