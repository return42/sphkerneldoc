
.. _API---drm-atomic-helper-connector-duplicate-state:

=============================================
__drm_atomic_helper_connector_duplicate_state
=============================================

*man __drm_atomic_helper_connector_duplicate_state(9)*

*4.6.0-rc1*

copy atomic connector state


Synopsis
========

.. c:function:: void __drm_atomic_helper_connector_duplicate_state( struct drm_connector * connector, struct drm_connector_state * state )

Arguments
=========

``connector``
    connector object

``state``
    atomic connector state


Description
===========

Copies atomic state from a connector's current state. This is useful for drivers that subclass the connector state.
