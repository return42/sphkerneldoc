.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-plane-duplicate-state:

===========================
intel_plane_duplicate_state
===========================

*man intel_plane_duplicate_state(9)*

*4.6.0-rc5*

duplicate plane state


Synopsis
========

.. c:function:: struct drm_plane_state * intel_plane_duplicate_state( struct drm_plane * plane )

Arguments
=========

``plane``
    drm plane


Description
===========

Allocates and returns a copy of the plane state (both common and
Intel-specific) for the specified plane.


Returns
=======

The newly allocated plane state, or NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
