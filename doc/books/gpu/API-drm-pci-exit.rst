
.. _API-drm-pci-exit:

============
drm_pci_exit
============

*man drm_pci_exit(9)*

*4.6.0-rc1*

Unregister matching PCI devices from the DRM subsystem


Synopsis
========

.. c:function:: void drm_pci_exit( struct drm_driver * driver, struct pci_driver * pdriver )

Arguments
=========

``driver``
    DRM device driver

``pdriver``
    PCI device driver


Description
===========

Unregisters one or more devices matched by a PCI driver from the DRM subsystem.


NOTE
====

This function is deprecated. Modern modesetting drm drivers should use ``pci_unregister_driver`` directly, this function only provides shadow-binding support for old legacy drivers
on top of that core pci function.
