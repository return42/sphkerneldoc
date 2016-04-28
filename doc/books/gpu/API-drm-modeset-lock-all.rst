.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-lock-all:

====================
drm_modeset_lock_all
====================

*man drm_modeset_lock_all(9)*

*4.6.0-rc5*

take all modeset locks


Synopsis
========

.. c:function:: void drm_modeset_lock_all( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This function takes all modeset locks, suitable where a more
fine-grained scheme isn't (yet) implemented. Locks must be dropped by
calling the ``drm_modeset_unlock_all`` function.

This function is deprecated. It allocates a lock acquisition context and
stores it in the DRM device's ->mode_config. This facilitate conversion
of existing code because it removes the need to manually deal with the
acquisition context, but it is also brittle because the context is
global and care must be taken not to nest calls. New code should use the
``drm_modeset_lock_all_ctx`` function and pass in the context
explicitly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
