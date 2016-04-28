.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-adjust-size:

====================
drm_rect_adjust_size
====================

*man drm_rect_adjust_size(9)*

*4.6.0-rc5*

adjust the size of the rectangle


Synopsis
========

.. c:function:: void drm_rect_adjust_size( struct drm_rect * r, int dw, int dh )

Arguments
=========

``r``
    rectangle to be adjusted

``dw``
    horizontal adjustment

``dh``
    vertical adjustment


Description
===========

Change the size of rectangle ``r`` by ``dw`` in the horizontal
direction, and by ``dh`` in the vertical direction, while keeping the
center of ``r`` stationary.

Positive ``dw`` and ``dh`` increase the size, negative values decrease
it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
