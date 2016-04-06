
.. _API-drm-rect-debug-print:

====================
drm_rect_debug_print
====================

*man drm_rect_debug_print(9)*

*4.6.0-rc1*

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
