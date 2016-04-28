.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-connector-init:

==================
drm_connector_init
==================

*man drm_connector_init(9)*

*4.6.0-rc5*

Init a preallocated connector


Synopsis
========

.. c:function:: int drm_connector_init( struct drm_device * dev, struct drm_connector * connector, const struct drm_connector_funcs * funcs, int connector_type )

Arguments
=========

``dev``
    DRM device

``connector``
    the connector to init

``funcs``
    callbacks for this connector

``connector_type``
    user visible type of the connector


Description
===========

Initialises a preallocated connector. Connectors should be subclassed as
part of driver connector objects.


Returns
=======

Zero on success, error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
