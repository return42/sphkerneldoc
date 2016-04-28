.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-irq-install:

===============
drm_irq_install
===============

*man drm_irq_install(9)*

*4.6.0-rc5*

install IRQ handler


Synopsis
========

.. c:function:: int drm_irq_install( struct drm_device * dev, int irq )

Arguments
=========

``dev``
    DRM device

``irq``
    IRQ number to install the handler for


Description
===========

Initializes the IRQ related data. Installs the handler, calling the
driver ``irq_preinstall`` and ``irq_postinstall`` functions before and
after the installation.

This is the simplified helper interface provided for drivers with no
special needs. Drivers which need to install interrupt handlers for
multiple interrupts must instead set drm_device->irq_enabled to signal
the DRM core that vblank interrupts are available.


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
