
.. _API-drm-dp-mst-topology-mgr-suspend:

===============================
drm_dp_mst_topology_mgr_suspend
===============================

*man drm_dp_mst_topology_mgr_suspend(9)*

*4.6.0-rc1*

suspend the MST manager


Synopsis
========

.. c:function:: void drm_dp_mst_topology_mgr_suspend( struct drm_dp_mst_topology_mgr * mgr )

Arguments
=========

``mgr``
    manager to suspend


Description
===========

This function tells the MST device that we can't handle UP messages anymore. This should stop it from sending any since we are suspended.
