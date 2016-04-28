.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-connector-set-path-property:

====================================
drm_mode_connector_set_path_property
====================================

*man drm_mode_connector_set_path_property(9)*

*4.6.0-rc5*

set tile property on connector


Synopsis
========

.. c:function:: int drm_mode_connector_set_path_property( struct drm_connector * connector, const char * path )

Arguments
=========

``connector``
    connector to set property on.

``path``
    path to use for property; must not be NULL.


Description
===========

This creates a property to expose to userspace to specify a connector
path. This is mainly used for DisplayPort MST where connectors have a
topology and we want to allow userspace to give them more meaningful
names.


Returns
=======

Zero on success, negative errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
