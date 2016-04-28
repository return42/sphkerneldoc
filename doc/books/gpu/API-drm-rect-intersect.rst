.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-intersect:

==================
drm_rect_intersect
==================

*man drm_rect_intersect(9)*

*4.6.0-rc5*

intersect two rectangles


Synopsis
========

.. c:function:: bool drm_rect_intersect( struct drm_rect * r1, const struct drm_rect * r2 )

Arguments
=========

``r1``
    first rectangle

``r2``
    second rectangle


Description
===========

Calculate the intersection of rectangles ``r1`` and ``r2``. ``r1`` will
be overwritten with the intersection.


RETURNS
=======

``true`` if rectangle ``r1`` is still visible after the operation,
``false`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
