.. -*- coding: utf-8; mode: rst -*-

.. _API---drm-atomic-helper-plane-destroy-state:

=======================================
__drm_atomic_helper_plane_destroy_state
=======================================

*man __drm_atomic_helper_plane_destroy_state(9)*

*4.6.0-rc5*

release plane state


Synopsis
========

.. c:function:: void __drm_atomic_helper_plane_destroy_state( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    plane object

``state``
    plane state object to release


Description
===========

Releases all resources stored in the plane state without actually
freeing the memory of the plane state. This is useful for drivers that
subclass the plane state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
