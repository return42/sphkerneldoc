
.. _API-drm-dp-mst-reset-vcpi-slots:

===========================
drm_dp_mst_reset_vcpi_slots
===========================

*man drm_dp_mst_reset_vcpi_slots(9)*

*4.6.0-rc1*

Reset number of slots to 0 for VCPI


Synopsis
========

.. c:function:: void drm_dp_mst_reset_vcpi_slots( struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port )

Arguments
=========

``mgr``
    manager for this port

``port``
    unverified pointer to a port.


Description
===========

This just resets the number of slots for the ports VCPI for later programming.
