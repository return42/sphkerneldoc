
.. _API-pcim-pin-device:

===============
pcim_pin_device
===============

*man pcim_pin_device(9)*

*4.6.0-rc1*

Pin managed PCI device


Synopsis
========

.. c:function:: void pcim_pin_device( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device to pin


Description
===========

Pin managed PCI device ``pdev``. Pinned device won't be disabled on driver detach. ``pdev`` must have been enabled with ``pcim_enable_device``.
