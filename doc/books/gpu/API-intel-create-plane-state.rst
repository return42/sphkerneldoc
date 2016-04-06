
.. _API-intel-create-plane-state:

========================
intel_create_plane_state
========================

*man intel_create_plane_state(9)*

*4.6.0-rc1*

create plane state object


Synopsis
========

.. c:function:: struct intel_plane_state ⋆ intel_create_plane_state( struct drm_plane * plane )

Arguments
=========

``plane``
    drm plane


Description
===========

Allocates a fresh plane state for the given plane and sets some of the state values to sensible initial values.


Returns
=======

A newly allocated plane state, or NULL on failure
