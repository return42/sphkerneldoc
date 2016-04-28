.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-debug-print:

====================
drm_rect_debug_print
====================

*man drm_rect_debug_print(9)*

*4.6.0-rc5*

print the rectangle information


Synopsis
========

.. c:function:: void drm_rect_debug_print( const char * prefix, const struct drm_rect * r, bool fixed_point )

Arguments
=========

``prefix``
    prefix string

``r``
    rectangle to print

``fixed_point``
    rectangle is in 16.16 fixed point format


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
