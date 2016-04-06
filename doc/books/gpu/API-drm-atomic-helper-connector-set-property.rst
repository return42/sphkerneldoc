
.. _API-drm-atomic-helper-connector-set-property:

========================================
drm_atomic_helper_connector_set_property
========================================

*man drm_atomic_helper_connector_set_property(9)*

*4.6.0-rc1*

helper for connector properties


Synopsis
========

.. c:function:: int drm_atomic_helper_connector_set_property( struct drm_connector * connector, struct drm_property * property, uint64_t val )

Arguments
=========

``connector``
    DRM connector

``property``
    DRM property

``val``
    value of property


Description
===========

Provides a default connector set_property handler using the atomic driver interface.


RETURNS
=======

Zero on success, error code on failure
