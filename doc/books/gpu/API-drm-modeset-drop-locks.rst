
.. _API-drm-modeset-drop-locks:

======================
drm_modeset_drop_locks
======================

*man drm_modeset_drop_locks(9)*

*4.6.0-rc1*

drop all locks


Synopsis
========

.. c:function:: void drm_modeset_drop_locks( struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``ctx``
    the acquire context


Description
===========

Drop all locks currently held against this acquire context.
