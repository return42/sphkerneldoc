.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-mst-topology-mgr-set-mst:

===============================
drm_dp_mst_topology_mgr_set_mst
===============================

*man drm_dp_mst_topology_mgr_set_mst(9)*

*4.6.0-rc5*

Set the MST state for a topology manager


Synopsis
========

.. c:function:: int drm_dp_mst_topology_mgr_set_mst( struct drm_dp_mst_topology_mgr * mgr, bool mst_state )

Arguments
=========

``mgr``
    manager to set state for

``mst_state``
    true to enable MST on this connector - false to disable.


Description
===========

This is called by the driver when it detects an MST capable device
plugged into a DP MST capable port, or when a DP MST capable device is
unplugged.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
