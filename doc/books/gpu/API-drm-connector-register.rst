
.. _API-drm-connector-register:

======================
drm_connector_register
======================

*man drm_connector_register(9)*

*4.6.0-rc1*

register a connector


Synopsis
========

.. c:function:: int drm_connector_register( struct drm_connector * connector )

Arguments
=========

``connector``
    the connector to register


Description
===========

Register userspace interfaces for a connector


Returns
=======

Zero on success, error code on failure.
