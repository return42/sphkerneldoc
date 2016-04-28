.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-equals:

===============
drm_rect_equals
===============

*man drm_rect_equals(9)*

*4.6.0-rc5*

determine if two rectangles are equal


Synopsis
========

.. c:function:: bool drm_rect_equals( const struct drm_rect * r1, const struct drm_rect * r2 )

Arguments
=========

``r1``
    first rectangle

``r2``
    second rectangle


RETURNS
=======

``true`` if the rectangles are equal, ``false`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
