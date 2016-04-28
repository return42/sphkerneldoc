.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-connector-set-tile-property:

====================================
drm_mode_connector_set_tile_property
====================================

*man drm_mode_connector_set_tile_property(9)*

*4.6.0-rc5*

set tile property on connector


Synopsis
========

.. c:function:: int drm_mode_connector_set_tile_property( struct drm_connector * connector )

Arguments
=========

``connector``
    connector to set property on.


Description
===========

This looks up the tile information for a connector, and creates a
property for userspace to parse if it exists. The property is of the
form of 8 integers using ':' as a separator.


Returns
=======

Zero on success, errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
