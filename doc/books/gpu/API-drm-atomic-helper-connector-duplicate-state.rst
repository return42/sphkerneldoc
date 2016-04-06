
.. _API-drm-atomic-helper-connector-duplicate-state:

===========================================
drm_atomic_helper_connector_duplicate_state
===========================================

*man drm_atomic_helper_connector_duplicate_state(9)*

*4.6.0-rc1*

default state duplicate hook


Synopsis
========

.. c:function:: struct drm_connector_state ⋆ drm_atomic_helper_connector_duplicate_state( struct drm_connector * connector )

Arguments
=========

``connector``
    drm connector


Description
===========

Default connector state duplicate hook for drivers which don't have their own subclassed connector state structure.
