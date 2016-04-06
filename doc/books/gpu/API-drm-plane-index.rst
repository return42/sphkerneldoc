
.. _API-drm-plane-index:

===============
drm_plane_index
===============

*man drm_plane_index(9)*

*4.6.0-rc1*

find the index of a registered plane


Synopsis
========

.. c:function:: unsigned int drm_plane_index( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to find index for


Description
===========

Given a registered plane, return the index of that CRTC within a DRM device's list of planes.
