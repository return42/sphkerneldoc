
.. _API-drm-add-modes-noedid:

====================
drm_add_modes_noedid
====================

*man drm_add_modes_noedid(9)*

*4.6.0-rc1*

add modes for the connectors without EDID


Synopsis
========

.. c:function:: int drm_add_modes_noedid( struct drm_connector * connector, int hdisplay, int vdisplay )

Arguments
=========

``connector``
    connector we're probing

``hdisplay``
    the horizontal display limit

``vdisplay``
    the vertical display limit


Description
===========

Add the specified modes to the connector's mode list. Only when the hdisplay/vdisplay is not beyond the given limit, it will be added.


Return
======

The number of modes added or 0 if we couldn't find any.
