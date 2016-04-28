.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-plane-helper-add:

====================
drm_plane_helper_add
====================

*man drm_plane_helper_add(9)*

*4.6.0-rc5*

sets the helper vtable for a plane


Synopsis
========

.. c:function:: void drm_plane_helper_add( struct drm_plane * plane, const struct drm_plane_helper_funcs * funcs )

Arguments
=========

``plane``
    DRM plane

``funcs``
    helper vtable to set for ``plane``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
