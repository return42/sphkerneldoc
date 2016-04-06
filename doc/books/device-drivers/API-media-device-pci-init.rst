
.. _API-media-device-pci-init:

=====================
media_device_pci_init
=====================

*man media_device_pci_init(9)*

*4.6.0-rc1*

create and initialize a struct ``media_device`` from a PCI device.


Synopsis
========

.. c:function:: void media_device_pci_init( struct media_device * mdev, struct pci_dev * pci_dev, const char * name )

Arguments
=========

``mdev``
    pointer to struct ``media_device``

``pci_dev``
    pointer to struct pci_dev

``name``
    media device name. If ``NULL``, the routine will use the default name for the pci device, given by ``pci_name`` macro.
