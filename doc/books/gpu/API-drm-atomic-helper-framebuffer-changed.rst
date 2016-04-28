.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-framebuffer-changed:

=====================================
drm_atomic_helper_framebuffer_changed
=====================================

*man drm_atomic_helper_framebuffer_changed(9)*

*4.6.0-rc5*

check if framebuffer has changed


Synopsis
========

.. c:function:: bool drm_atomic_helper_framebuffer_changed( struct drm_device * dev, struct drm_atomic_state * old_state, struct drm_crtc * crtc )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures

``crtc``
    DRM crtc


Description
===========

Checks whether the framebuffer used for this CRTC changes as a result of
the atomic update. This is useful for drivers which cannot use
``drm_atomic_helper_wait_for_vblanks`` and need to reimplement its
functionality.


Returns
=======

true if the framebuffer changed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
