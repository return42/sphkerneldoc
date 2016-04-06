
.. _API-drm-helper-hpd-irq-event:

========================
drm_helper_hpd_irq_event
========================

*man drm_helper_hpd_irq_event(9)*

*4.6.0-rc1*

hotplug processing


Synopsis
========

.. c:function:: bool drm_helper_hpd_irq_event( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device


Description
===========

Drivers can use this helper function to run a detect cycle on all connectors which have the DRM_CONNECTOR_POLL_HPD flag set in their ``polled`` member. All other connectors are
ignored, which is useful to avoid reprobing fixed panels.

This helper function is useful for drivers which can't or don't track hotplug interrupts for each connector.

Drivers which support hotplug interrupts for each connector individually and which have a more fine-grained detect logic should bypass this code and directly call
``drm_kms_helper_hotplug_event`` in case the connector state changed.

This function must be called from process context with no mode setting locks held.

Note that a connector can be both polled and probed from the hotplug handler, in case the hotplug interrupt is known to be unreliable.
