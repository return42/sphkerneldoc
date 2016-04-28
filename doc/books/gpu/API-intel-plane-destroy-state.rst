.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-plane-destroy-state:

=========================
intel_plane_destroy_state
=========================

*man intel_plane_destroy_state(9)*

*4.6.0-rc5*

destroy plane state


Synopsis
========

.. c:function:: void intel_plane_destroy_state( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    drm plane

``state``
    state object to destroy


Description
===========

Destroys the plane state (both common and Intel-specific) for the
specified plane.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
