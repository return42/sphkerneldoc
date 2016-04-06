
.. _API-drm-rect-adjust-size:

====================
drm_rect_adjust_size
====================

*man drm_rect_adjust_size(9)*

*4.6.0-rc1*

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

Change the size of rectangle ``r`` by ``dw`` in the horizontal direction, and by ``dh`` in the vertical direction, while keeping the center of ``r`` stationary.

Positive ``dw`` and ``dh`` increase the size, negative values decrease it.
