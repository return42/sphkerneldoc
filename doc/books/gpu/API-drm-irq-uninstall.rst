.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-irq-uninstall:

=================
drm_irq_uninstall
=================

*man drm_irq_uninstall(9)*

*4.6.0-rc5*

uninstall the IRQ handler


Synopsis
========

.. c:function:: int drm_irq_uninstall( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Calls the driver's ``irq_uninstall`` function and unregisters the IRQ
handler. This should only be called by drivers which used
``drm_irq_install`` to set up their interrupt handler. Other drivers
must only reset drm_device->irq_enabled to false.

Note that for kernel modesetting drivers it is a bug if this function
fails. The sanity checks are only to catch buggy user modesetting
drivers which call the same function through an ioctl.


Returns
=======

Zero on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
