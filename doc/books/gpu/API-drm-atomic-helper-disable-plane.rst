
.. _API-drm-atomic-helper-disable-plane:

===============================
drm_atomic_helper_disable_plane
===============================

*man drm_atomic_helper_disable_plane(9)*

*4.6.0-rc1*

Helper for primary plane disable using ⋆ atomic


Synopsis
========

.. c:function:: int drm_atomic_helper_disable_plane( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to disable


Description
===========

Provides a default plane disable handler using the atomic driver interface.


RETURNS
=======

Zero on success, error code on failure
