.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-lock-all-ctx:

========================
drm_modeset_lock_all_ctx
========================

*man drm_modeset_lock_all_ctx(9)*

*4.6.0-rc5*

take all modeset locks


Synopsis
========

.. c:function:: int drm_modeset_lock_all_ctx( struct drm_device * dev, struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``dev``
    DRM device

``ctx``
    lock acquisition context


Description
===========

This function takes all modeset locks, suitable where a more
fine-grained scheme isn't (yet) implemented.

Unlike ``drm_modeset_lock_all``, it doesn't take the
dev->mode_config.mutex since that lock isn't required for modeset state
changes. Callers which need to grab that lock too need to do so outside
of the acquire context ``ctx``.

Locks acquired with this function should be released by calling the
``drm_modeset_drop_locks`` function on ``ctx``.


Returns
=======

0 on success or a negative error-code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
