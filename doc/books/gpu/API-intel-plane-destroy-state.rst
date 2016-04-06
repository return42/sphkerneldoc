
.. _API-intel-plane-destroy-state:

=========================
intel_plane_destroy_state
=========================

*man intel_plane_destroy_state(9)*

*4.6.0-rc1*

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

Destroys the plane state (both common and Intel-specific) for the specified plane.
