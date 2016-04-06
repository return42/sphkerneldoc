
.. _API-drm-rect-calc-vscale-relaxed:

============================
drm_rect_calc_vscale_relaxed
============================

*man drm_rect_calc_vscale_relaxed(9)*

*4.6.0-rc1*

calculate the vertical scaling factor


Synopsis
========

.. c:function:: int drm_rect_calc_vscale_relaxed( struct drm_rect * src, struct drm_rect * dst, int min_vscale, int max_vscale )

Arguments
=========

``src``
    source window rectangle

``dst``
    destination window rectangle

``min_vscale``
    minimum allowed vertical scaling factor

``max_vscale``
    maximum allowed vertical scaling factor


Description
===========

Calculate the vertical scaling factor as (``src`` height) / (``dst`` height).

If the calculated scaling factor is below ``min_vscale``, decrease the height of rectangle ``dst`` to compensate.

If the calculated scaling factor is above ``max_vscale``, decrease the height of rectangle ``src`` to compensate.


RETURNS
=======

The vertical scaling factor.
