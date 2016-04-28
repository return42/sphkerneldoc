.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-calc-vscale:

====================
drm_rect_calc_vscale
====================

*man drm_rect_calc_vscale(9)*

*4.6.0-rc5*

calculate the vertical scaling factor


Synopsis
========

.. c:function:: int drm_rect_calc_vscale( const struct drm_rect * src, const struct drm_rect * dst, int min_vscale, int max_vscale )

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

Calculate the vertical scaling factor as (``src`` height) / (``dst``
height).


RETURNS
=======

The vertical scaling factor, or errno of out of limits.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
