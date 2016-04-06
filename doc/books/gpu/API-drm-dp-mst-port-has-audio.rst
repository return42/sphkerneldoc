
.. _API-drm-dp-mst-port-has-audio:

=========================
drm_dp_mst_port_has_audio
=========================

*man drm_dp_mst_port_has_audio(9)*

*4.6.0-rc1*

Check whether port has audio capability or not


Synopsis
========

.. c:function:: bool drm_dp_mst_port_has_audio( struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port )

Arguments
=========

``mgr``
    manager for this port

``port``
    unverified pointer to a port.


Description
===========

This returns whether the port supports audio or not.
