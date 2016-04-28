.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-cleanup-planes:

================================
drm_atomic_helper_cleanup_planes
================================

*man drm_atomic_helper_cleanup_planes(9)*

*4.6.0-rc5*

cleanup plane resources after commit


Synopsis
========

.. c:function:: void drm_atomic_helper_cleanup_planes( struct drm_device * dev, struct drm_atomic_state * old_state )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures


Description
===========

This function cleans up plane state, specifically framebuffers, from the
old configuration. Hence the old configuration must be perserved in
``old_state`` to be able to call this function.

This function must also be called on the new state when the atomic
update fails at any point after calling
``drm_atomic_helper_prepare_planes``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
