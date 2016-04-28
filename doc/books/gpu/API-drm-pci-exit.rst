.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-pci-exit:

============
drm_pci_exit
============

*man drm_pci_exit(9)*

*4.6.0-rc5*

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

Unregisters one or more devices matched by a PCI driver from the DRM
subsystem.


NOTE
====

This function is deprecated. Modern modesetting drm drivers should use
``pci_unregister_driver`` directly, this function only provides
shadow-binding support for old legacy drivers on top of that core pci
function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
