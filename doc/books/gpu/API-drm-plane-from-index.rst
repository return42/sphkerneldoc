
.. _API-drm-plane-from-index:

====================
drm_plane_from_index
====================

*man drm_plane_from_index(9)*

*4.6.0-rc1*

find the registered plane at an index


Synopsis
========

.. c:function:: struct drm_plane ⋆ drm_plane_from_index( struct drm_device * dev, int idx )

Arguments
=========

``dev``
    DRM device

``idx``
    index of registered plane to find for


Description
===========

Given a plane index, return the registered plane from DRM device's list of planes with matching index.
