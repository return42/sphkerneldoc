.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-get-subpixel-order-name:

===========================
drm_get_subpixel_order_name
===========================

*man drm_get_subpixel_order_name(9)*

*4.6.0-rc5*

return a string for a given subpixel enum


Synopsis
========

.. c:function:: const char * drm_get_subpixel_order_name( enum subpixel_order order )

Arguments
=========

``order``
    enum of subpixel_order


Description
===========

Note you could abuse this and return something out of bounds, but that
would be a caller error. No unscrubbed user data should make it here.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
