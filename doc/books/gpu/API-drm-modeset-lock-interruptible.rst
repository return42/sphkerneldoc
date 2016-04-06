
.. _API-drm-modeset-lock-interruptible:

==============================
drm_modeset_lock_interruptible
==============================

*man drm_modeset_lock_interruptible(9)*

*4.6.0-rc1*

take modeset lock


Synopsis
========

.. c:function:: int drm_modeset_lock_interruptible( struct drm_modeset_lock * lock, struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``lock``
    lock to take

``ctx``
    acquire ctx


Description
===========

Interruptible version of ``drm_modeset_lock``
