.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-rotate-inv:

===================
drm_rect_rotate_inv
===================

*man drm_rect_rotate_inv(9)*

*4.6.0-rc5*

Inverse rotate the rectangle


Synopsis
========

.. c:function:: void drm_rect_rotate_inv( struct drm_rect * r, int width, int height, unsigned int rotation )

Arguments
=========

``r``
    rectangle to be rotated

``width``
    Width of the coordinate space

``height``
    Height of the coordinate space

``rotation``
    Transformation whose inverse is to be applied


Description
===========

Apply the inverse of ``rotation`` to the coordinates of rectangle ``r``.

``width`` and ``height`` combined with ``rotation`` define the location
of the new origin.

``width`` correcsponds to the horizontal and ``height`` to the vertical
axis of the original untransformed coordinate space, so that you never
have to flip them when doing a rotatation and its inverse. That is, if
you do:

drm_rotate( ``r``, width, height, rotation); drm_rotate_inv( ``r``,
width, height, rotation);

you will always get back the original rectangle.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
