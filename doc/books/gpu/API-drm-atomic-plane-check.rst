
.. _API-drm-atomic-plane-check:

======================
drm_atomic_plane_check
======================

*man drm_atomic_plane_check(9)*

*4.6.0-rc1*

check plane state


Synopsis
========

.. c:function:: int drm_atomic_plane_check( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    plane to check

``state``
    plane state to check


Description
===========

Provides core sanity checks for plane state.


RETURNS
=======

Zero on success, error code on failure
