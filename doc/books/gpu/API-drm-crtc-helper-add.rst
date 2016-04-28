.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-helper-add:

===================
drm_crtc_helper_add
===================

*man drm_crtc_helper_add(9)*

*4.6.0-rc5*

sets the helper vtable for a crtc


Synopsis
========

.. c:function:: void drm_crtc_helper_add( struct drm_crtc * crtc, const struct drm_crtc_helper_funcs * funcs )

Arguments
=========

``crtc``
    DRM CRTC

``funcs``
    helper vtable to set for ``crtc``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
