
.. _API-drm-mode-connector-update-edid-property:

=======================================
drm_mode_connector_update_edid_property
=======================================

*man drm_mode_connector_update_edid_property(9)*

*4.6.0-rc1*

update the edid property of a connector


Synopsis
========

.. c:function:: int drm_mode_connector_update_edid_property( struct drm_connector * connector, const struct edid * edid )

Arguments
=========

``connector``
    drm connector

``edid``
    new value of the edid property


Description
===========

This function creates a new blob modeset object and assigns its id to the connector's edid property.


Returns
=======

Zero on success, negative errno on failure.
