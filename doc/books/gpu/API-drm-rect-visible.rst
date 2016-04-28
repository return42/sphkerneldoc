.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-visible:

================
drm_rect_visible
================

*man drm_rect_visible(9)*

*4.6.0-rc5*

determine if the the rectangle is visible


Synopsis
========

.. c:function:: bool drm_rect_visible( const struct drm_rect * r )

Arguments
=========

``r``
    rectangle whose visibility is returned


RETURNS
=======

``true`` if the rectangle is visible, ``false`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
