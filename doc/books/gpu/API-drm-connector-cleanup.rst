
.. _API-drm-connector-cleanup:

=====================
drm_connector_cleanup
=====================

*man drm_connector_cleanup(9)*

*4.6.0-rc1*

cleans up an initialised connector


Synopsis
========

.. c:function:: void drm_connector_cleanup( struct drm_connector * connector )

Arguments
=========

``connector``
    connector to cleanup


Description
===========

Cleans up the connector but doesn't free the object.
