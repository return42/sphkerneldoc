
.. _API-drm-vblank-cleanup:

==================
drm_vblank_cleanup
==================

*man drm_vblank_cleanup(9)*

*4.6.0-rc1*

cleanup vblank support


Synopsis
========

.. c:function:: void drm_vblank_cleanup( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This function cleans up any resources allocated in drm_vblank_init.
