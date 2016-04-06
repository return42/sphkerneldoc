
.. _API-drm-get-edid:

============
drm_get_edid
============

*man drm_get_edid(9)*

*4.6.0-rc1*

get EDID data, if available


Synopsis
========

.. c:function:: struct edid ⋆ drm_get_edid( struct drm_connector * connector, struct i2c_adapter * adapter )

Arguments
=========

``connector``
    connector we're probing

``adapter``
    I2C adapter to use for DDC


Description
===========

Poke the given I2C channel to grab EDID data if possible. If found, attach it to the connector.


Return
======

Pointer to valid EDID or NULL if we couldn't find any.
