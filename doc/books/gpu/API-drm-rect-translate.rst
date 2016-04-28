.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-translate:

==================
drm_rect_translate
==================

*man drm_rect_translate(9)*

*4.6.0-rc5*

translate the rectangle


Synopsis
========

.. c:function:: void drm_rect_translate( struct drm_rect * r, int dx, int dy )

Arguments
=========

``r``
    rectangle to be tranlated

``dx``
    horizontal translation

``dy``
    vertical translation


Description
===========

Move rectangle ``r`` by ``dx`` in the horizontal direction, and by
``dy`` in the vertical direction.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
