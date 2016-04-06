
.. _API-drm-warn-on-modeset-not-all-locked:

==================================
drm_warn_on_modeset_not_all_locked
==================================

*man drm_warn_on_modeset_not_all_locked(9)*

*4.6.0-rc1*

check that all modeset locks are locked


Synopsis
========

.. c:function:: void drm_warn_on_modeset_not_all_locked( struct drm_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Useful as a debug assert.
