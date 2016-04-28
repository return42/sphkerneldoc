.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-wait-for-vblanks:

==================================
drm_atomic_helper_wait_for_vblanks
==================================

*man drm_atomic_helper_wait_for_vblanks(9)*

*4.6.0-rc5*

wait for vblank on crtcs


Synopsis
========

.. c:function:: void drm_atomic_helper_wait_for_vblanks( struct drm_device * dev, struct drm_atomic_state * old_state )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures


Description
===========

Helper to, after atomic commit, wait for vblanks on all effected crtcs
(ie. before cleaning up old framebuffers using
``drm_atomic_helper_cleanup_planes``). It will only wait on crtcs where
the framebuffers have actually changed to optimize for the legacy cursor
and plane update use-case.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
