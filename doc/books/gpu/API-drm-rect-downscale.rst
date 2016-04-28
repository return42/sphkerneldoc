.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-downscale:

==================
drm_rect_downscale
==================

*man drm_rect_downscale(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
