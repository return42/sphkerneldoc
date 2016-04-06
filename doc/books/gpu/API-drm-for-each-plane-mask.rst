
.. _API-drm-for-each-plane-mask:

=======================
drm_for_each_plane_mask
=======================

*man drm_for_each_plane_mask(9)*

*4.6.0-rc1*

iterate over planes specified by bitmask


Synopsis
========

.. c:function:: drm_for_each_plane_mask( plane, dev, plane_mask )

Arguments
=========

``plane``
    the loop cursor

``dev``
    the DRM device

``plane_mask``
    bitmask of plane indices


Description
===========

Iterate over all planes specified by bitmask.
