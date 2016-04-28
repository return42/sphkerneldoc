.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-get-tile-group:

=======================
drm_mode_get_tile_group
=======================

*man drm_mode_get_tile_group(9)*

*4.6.0-rc5*

get a reference to an existing tile group


Synopsis
========

.. c:function:: struct drm_tile_group * drm_mode_get_tile_group( struct drm_device * dev, char topology[8] )

Arguments
=========

``dev``
    DRM device

``topology[8]``
    8-bytes unique per monitor.


Description
===========

Use the unique bytes to get a reference to an existing tile group.


RETURNS
=======

tile group or NULL if not found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
