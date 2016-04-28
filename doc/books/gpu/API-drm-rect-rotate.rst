.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-rotate:

===============
drm_rect_rotate
===============

*man drm_rect_rotate(9)*

*4.6.0-rc5*

Rotate the rectangle


Synopsis
========

.. c:function:: void drm_rect_rotate( struct drm_rect * r, int width, int height, unsigned int rotation )

Arguments
=========

``r``
    rectangle to be rotated

``width``
    Width of the coordinate space

``height``
    Height of the coordinate space

``rotation``
    Transformation to be applied


Description
===========

Apply ``rotation`` to the coordinates of rectangle ``r``.

``width`` and ``height`` combined with ``rotation`` define the location
of the new origin.

``width`` correcsponds to the horizontal and ``height`` to the vertical
axis of the untransformed coordinate space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
