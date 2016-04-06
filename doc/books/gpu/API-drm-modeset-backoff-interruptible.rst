
.. _API-drm-modeset-backoff-interruptible:

=================================
drm_modeset_backoff_interruptible
=================================

*man drm_modeset_backoff_interruptible(9)*

*4.6.0-rc1*

deadlock avoidance backoff


Synopsis
========

.. c:function:: int drm_modeset_backoff_interruptible( struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``ctx``
    the acquire context


Description
===========

Interruptible version of ``drm_modeset_backoff``
