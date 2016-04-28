.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-kms-helper-hotplug-event:

============================
drm_kms_helper_hotplug_event
============================

*man drm_kms_helper_hotplug_event(9)*

*4.6.0-rc5*

fire off KMS hotplug events


Synopsis
========

.. c:function:: void drm_kms_helper_hotplug_event( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device whose connector state changed


Description
===========

This function fires off the uevent for userspace and also calls the
output_poll_changed function, which is most commonly used to inform
the fbdev emulation code and allow it to update the fbcon output
configuration.

Drivers should call this from their hotplug handling code when a change
is detected. Note that this function does not do any output detection of
its own, like ``drm_helper_hpd_irq_event`` does - this is assumed to be
done by the driver already.

This function must be called from process context with no mode setting
locks held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
