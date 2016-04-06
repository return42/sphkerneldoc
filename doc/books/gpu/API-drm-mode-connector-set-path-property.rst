
.. _API-drm-mode-connector-set-path-property:

====================================
drm_mode_connector_set_path_property
====================================

*man drm_mode_connector_set_path_property(9)*

*4.6.0-rc1*

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

This creates a property to expose to userspace to specify a connector path. This is mainly used for DisplayPort MST where connectors have a topology and we want to allow userspace
to give them more meaningful names.


Returns
=======

Zero on success, negative errno on failure.
