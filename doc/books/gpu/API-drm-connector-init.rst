
.. _API-drm-connector-init:

==================
drm_connector_init
==================

*man drm_connector_init(9)*

*4.6.0-rc1*

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

Initialises a preallocated connector. Connectors should be subclassed as part of driver connector objects.


Returns
=======

Zero on success, error code on failure.
