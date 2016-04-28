.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-for-each-plane-mask:

=======================
drm_for_each_plane_mask
=======================

*man drm_for_each_plane_mask(9)*

*4.6.0-rc5*

iterate over planes specified by bitmask


Synopsis
========

.. c:function:: drm_for_each_plane_mask( plane, dev, plane_mask )

Arguments
=========

``plane``
    the loop cursor

``dev``
    the DRM device

``plane_mask``
    bitmask of plane indices


Description
===========

Iterate over all planes specified by bitmask.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
