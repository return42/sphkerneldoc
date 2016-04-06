
.. _API-drm-get-subpixel-order-name:

===========================
drm_get_subpixel_order_name
===========================

*man drm_get_subpixel_order_name(9)*

*4.6.0-rc1*

return a string for a given subpixel enum


Synopsis
========

.. c:function:: const char ⋆ drm_get_subpixel_order_name( enum subpixel_order order )

Arguments
=========

``order``
    enum of subpixel_order


Description
===========

Note you could abuse this and return something out of bounds, but that would be a caller error. No unscrubbed user data should make it here.
