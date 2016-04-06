
.. _API-usb-hcd-pci-probe:

=================
usb_hcd_pci_probe
=================

*man usb_hcd_pci_probe(9)*

*4.6.0-rc1*

initialize PCI-based HCDs


Synopsis
========

.. c:function:: int usb_hcd_pci_probe( struct pci_dev * dev, const struct pci_device_id * id )

Arguments
=========

``dev``
    USB Host Controller being probed

``id``
    pci hotplug id connecting controller to HCD framework


Context
=======

!\ ``in_interrupt``


Description
===========

Allocates basic PCI resources for this USB host controller, and then invokes the ``start`` method for the HCD associated with it through the hotplug entry's driver_data.

Store this function in the HCD's struct pci_driver as ``probe``.


Return
======

0 if successful.
