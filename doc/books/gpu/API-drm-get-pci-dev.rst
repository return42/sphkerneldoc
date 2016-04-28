.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-get-pci-dev:

===============
drm_get_pci_dev
===============

*man drm_get_pci_dev(9)*

*4.6.0-rc5*

Register a PCI device with the DRM subsystem


Synopsis
========

.. c:function:: int drm_get_pci_dev( struct pci_dev * pdev, const struct pci_device_id * ent, struct drm_driver * driver )

Arguments
=========

``pdev``
    PCI device

``ent``
    entry from the PCI ID table that matches ``pdev``

``driver``
    DRM device driver


Description
===========

Attempt to gets inter module “drm” information. If we are first then
register the character device and inter module information. Try and
register, if we fail to register, backout previous work.


NOTE
====

This function is deprecated, please use ``drm_dev_alloc`` and
``drm_dev_register`` instead and remove your ->``load`` callback.


Return
======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
