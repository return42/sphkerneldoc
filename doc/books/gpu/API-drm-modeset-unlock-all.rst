.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-unlock-all:

======================
drm_modeset_unlock_all
======================

*man drm_modeset_unlock_all(9)*

*4.6.0-rc5*

drop all modeset locks


Synopsis
========

.. c:function:: void drm_modeset_unlock_all( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This function drops all modeset locks taken by a previous call to the
``drm_modeset_lock_all`` function.

This function is deprecated. It uses the lock acquisition context stored
in the DRM device's ->mode_config. This facilitates conversion of
existing code because it removes the need to manually deal with the
acquisition context, but it is also brittle because the context is
global and care must be taken not to nest calls. New code should pass
the acquisition context directly to the ``drm_modeset_drop_locks``
function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
