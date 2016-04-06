
.. _API-drm-atomic-helper-prepare-planes:

================================
drm_atomic_helper_prepare_planes
================================

*man drm_atomic_helper_prepare_planes(9)*

*4.6.0-rc1*

prepare plane resources before commit


Synopsis
========

.. c:function:: int drm_atomic_helper_prepare_planes( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    atomic state object with new state structures


Description
===========

This function prepares plane state, specifically framebuffers, for the new configuration. If any failure is encountered this function will call ->cleanup_fb on any already
successfully prepared framebuffer.


Returns
=======

0 on success, negative error code on failure.
