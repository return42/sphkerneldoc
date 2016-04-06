
.. _API-drm-atomic-helper-connector-destroy-state:

=========================================
drm_atomic_helper_connector_destroy_state
=========================================

*man drm_atomic_helper_connector_destroy_state(9)*

*4.6.0-rc1*

default state destroy hook


Synopsis
========

.. c:function:: void drm_atomic_helper_connector_destroy_state( struct drm_connector * connector, struct drm_connector_state * state )

Arguments
=========

``connector``
    drm connector

``state``
    connector state object to release


Description
===========

Default connector state destroy hook for drivers which don't have their own subclassed connector state structure.
