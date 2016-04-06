
.. _API-drm-rect-downscale:

==================
drm_rect_downscale
==================

*man drm_rect_downscale(9)*

*4.6.0-rc1*

downscale a rectangle


Synopsis
========

.. c:function:: void drm_rect_downscale( struct drm_rect * r, int horz, int vert )

Arguments
=========

``r``
    rectangle to be downscaled

``horz``
    horizontal downscale factor

``vert``
    vertical downscale factor


Description
===========

Divide the coordinates of rectangle ``r`` by ``horz`` and ``vert``.
