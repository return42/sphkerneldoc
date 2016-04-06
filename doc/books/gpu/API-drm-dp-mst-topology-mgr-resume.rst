
.. _API-drm-dp-mst-topology-mgr-resume:

==============================
drm_dp_mst_topology_mgr_resume
==============================

*man drm_dp_mst_topology_mgr_resume(9)*

*4.6.0-rc1*

resume the MST manager


Synopsis
========

.. c:function:: int drm_dp_mst_topology_mgr_resume( struct drm_dp_mst_topology_mgr * mgr )

Arguments
=========

``mgr``
    manager to resume


Description
===========

This will fetch DPCD and see if the device is still there, if it is, it will rewrite the MSTM control bits, and return.

if the device fails this returns -1, and the driver should do a full MST reprobe, in case we were undocked.
