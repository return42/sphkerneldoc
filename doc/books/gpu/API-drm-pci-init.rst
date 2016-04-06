
.. _API-drm-pci-init:

============
drm_pci_init
============

*man drm_pci_init(9)*

*4.6.0-rc1*

Register matching PCI devices with the DRM subsystem


Synopsis
========

.. c:function:: int drm_pci_init( struct drm_driver * driver, struct pci_driver * pdriver )

Arguments
=========

``driver``
    DRM device driver

``pdriver``
    PCI device driver


Description
===========

Initializes a drm_device structures, registering the stubs and initializing the AGP device.


NOTE
====

This function is deprecated. Modern modesetting drm drivers should use ``pci_register_driver`` directly, this function only provides shadow-binding support for old legacy drivers
on top of that core pci function.


Return
======

0 on success or a negative error code on failure.
