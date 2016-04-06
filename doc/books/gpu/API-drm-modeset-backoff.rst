
.. _API-drm-modeset-backoff:

===================
drm_modeset_backoff
===================

*man drm_modeset_backoff(9)*

*4.6.0-rc1*

deadlock avoidance backoff


Synopsis
========

.. c:function:: void drm_modeset_backoff( struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``ctx``
    the acquire context


Description
===========

If deadlock is detected (ie. ``drm_modeset_lock`` returns -EDEADLK), you must call this function to drop all currently held locks and block until the contended lock becomes
available.
