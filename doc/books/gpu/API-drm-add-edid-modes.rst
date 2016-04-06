
.. _API-drm-add-edid-modes:

==================
drm_add_edid_modes
==================

*man drm_add_edid_modes(9)*

*4.6.0-rc1*

add modes from EDID data, if available


Synopsis
========

.. c:function:: int drm_add_edid_modes( struct drm_connector * connector, struct edid * edid )

Arguments
=========

``connector``
    connector we're probing

``edid``
    EDID data


Description
===========

Add the specified modes to the connector's mode list.


Return
======

The number of modes added or 0 if we couldn't find any.
