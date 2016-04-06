
.. _API-drm-modeset-is-locked:

=====================
drm_modeset_is_locked
=====================

*man drm_modeset_is_locked(9)*

*4.6.0-rc1*

equivalent to ``mutex_is_locked``


Synopsis
========

.. c:function:: bool drm_modeset_is_locked( struct drm_modeset_lock * lock )

Arguments
=========

``lock``
    lock to check
