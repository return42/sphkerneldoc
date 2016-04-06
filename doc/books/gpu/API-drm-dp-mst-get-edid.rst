
.. _API-drm-dp-mst-get-edid:

===================
drm_dp_mst_get_edid
===================

*man drm_dp_mst_get_edid(9)*

*4.6.0-rc1*

get EDID for an MST port


Synopsis
========

.. c:function:: struct edid ⋆ drm_dp_mst_get_edid( struct drm_connector * connector, struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port )

Arguments
=========

``connector``
    toplevel connector to get EDID for

``mgr``
    manager for this port

``port``
    unverified pointer to a port.


Description
===========

This returns an EDID for the port connected to a connector, It validates the pointer still exists so the caller doesn't require a reference.
