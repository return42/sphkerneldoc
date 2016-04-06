
.. _API-drm-send-event-locked:

=====================
drm_send_event_locked
=====================

*man drm_send_event_locked(9)*

*4.6.0-rc1*

send DRM event to file descriptor


Synopsis
========

.. c:function:: void drm_send_event_locked( struct drm_device * dev, struct drm_pending_event * e )

Arguments
=========

``dev``
    DRM device

``e``
    DRM event to deliver


Description
===========

This function sends the event ``e``, initialized with ``drm_event_reserve_init``, to its associated userspace DRM file. Callers must already hold dev->event_lock, see
``drm_send_event`` for the unlocked version.

Note that the core will take care of unlinking and disarming events when the corresponding DRM file is closed. Drivers need not worry about whether the DRM file for this event
still exists and can call this function upon completion of the asynchronous work unconditionally.
