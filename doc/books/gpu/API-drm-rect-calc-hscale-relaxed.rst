
.. _API-drm-rect-calc-hscale-relaxed:

============================
drm_rect_calc_hscale_relaxed
============================

*man drm_rect_calc_hscale_relaxed(9)*

*4.6.0-rc1*

calculate the horizontal scaling factor


Synopsis
========

.. c:function:: int drm_rect_calc_hscale_relaxed( struct drm_rect * src, struct drm_rect * dst, int min_hscale, int max_hscale )

Arguments
=========

``src``
    source window rectangle

``dst``
    destination window rectangle

``min_hscale``
    minimum allowed horizontal scaling factor

``max_hscale``
    maximum allowed horizontal scaling factor


Description
===========

Calculate the horizontal scaling factor as (``src`` width) / (``dst`` width).

If the calculated scaling factor is below ``min_vscale``, decrease the height of rectangle ``dst`` to compensate.

If the calculated scaling factor is above ``max_vscale``, decrease the height of rectangle ``src`` to compensate.


RETURNS
=======

The horizontal scaling factor.
