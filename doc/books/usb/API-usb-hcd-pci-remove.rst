
.. _API-usb-hcd-pci-remove:

==================
usb_hcd_pci_remove
==================

*man usb_hcd_pci_remove(9)*

*4.6.0-rc1*

shutdown processing for PCI-based HCDs


Synopsis
========

.. c:function:: void usb_hcd_pci_remove( struct pci_dev * dev )

Arguments
=========

``dev``
    USB Host Controller being removed


Context
=======

!\ ``in_interrupt``


Description
===========

Reverses the effect of ``usb_hcd_pci_probe``, first invoking the HCD's ``stop`` method. It is always called from a thread context, normally “rmmod”, “apmd”, or something similar.

Store this function in the HCD's struct pci_driver as ``remove``.
