.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-page-flip:

===========================
drm_atomic_helper_page_flip
===========================

*man drm_atomic_helper_page_flip(9)*

*4.6.0-rc5*

execute a legacy page flip


Synopsis
========

.. c:function:: int drm_atomic_helper_page_flip( struct drm_crtc * crtc, struct drm_framebuffer * fb, struct drm_pending_vblank_event * event, uint32_t flags )

Arguments
=========

``crtc``
    DRM crtc

``fb``
    DRM framebuffer

``event``
    optional DRM event to signal upon completion

``flags``
    flip flags for non-vblank sync'ed updates


Description
===========

Provides a default page flip implementation using the atomic driver
interface.

Note that for now so called async page flips (i.e. updates which are not
synchronized to vblank) are not supported, since the atomic interfaces
have no provisions for this yet.


Returns
=======

Returns 0 on success, negative errno numbers on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
