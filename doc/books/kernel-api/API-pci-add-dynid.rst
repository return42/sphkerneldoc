
.. _API-pci-add-dynid:

=============
pci_add_dynid
=============

*man pci_add_dynid(9)*

*4.6.0-rc1*

add a new PCI device ID to this driver and re-probe devices


Synopsis
========

.. c:function:: int pci_add_dynid( struct pci_driver * drv, unsigned int vendor, unsigned int device, unsigned int subvendor, unsigned int subdevice, unsigned int class, unsigned int class_mask, unsigned long driver_data )

Arguments
=========

``drv``
    target pci driver

``vendor``
    PCI vendor ID

``device``
    PCI device ID

``subvendor``
    PCI subvendor ID

``subdevice``
    PCI subdevice ID

``class``
    PCI class

``class_mask``
    PCI class mask

``driver_data``
    private driver data


Description
===========

Adds a new dynamic pci device ID to this driver and causes the driver to probe for all devices again. ``drv`` must have been registered prior to calling this function.


CONTEXT
=======

Does GFP_KERNEL allocation.


RETURNS
=======

0 on success, -errno on failure.
