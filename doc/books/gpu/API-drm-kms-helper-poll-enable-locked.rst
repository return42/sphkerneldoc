
.. _API-drm-kms-helper-poll-enable-locked:

=================================
drm_kms_helper_poll_enable_locked
=================================

*man drm_kms_helper_poll_enable_locked(9)*

*4.6.0-rc1*

re-enable output polling.


Synopsis
========

.. c:function:: void drm_kms_helper_poll_enable_locked( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device


Description
===========

This function re-enables the output polling work without locking the mode_config mutex.

This is like ``drm_kms_helper_poll_enable`` however it is to be called from a context where the mode_config mutex is locked already.
