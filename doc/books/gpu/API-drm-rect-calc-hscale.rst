
.. _API-drm-rect-calc-hscale:

====================
drm_rect_calc_hscale
====================

*man drm_rect_calc_hscale(9)*

*4.6.0-rc1*

calculate the horizontal scaling factor


Synopsis
========

.. c:function:: int drm_rect_calc_hscale( const struct drm_rect * src, const struct drm_rect * dst, int min_hscale, int max_hscale )

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


RETURNS
=======

The horizontal scaling factor, or errno of out of limits.
