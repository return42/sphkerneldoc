
.. _API-pci-dev-run-wake:

================
pci_dev_run_wake
================

*man pci_dev_run_wake(9)*

*4.6.0-rc1*

Check if device can generate run-time wake-up events.


Synopsis
========

.. c:function:: bool pci_dev_run_wake( struct pci_dev * dev )

Arguments
=========

``dev``
    Device to check.


Description
===========

Return true if the device itself is capable of generating wake-up events (through the platform or using the native PCIe PME) or if the device supports PME and one of its upstream
bridges can generate wake-up events.
