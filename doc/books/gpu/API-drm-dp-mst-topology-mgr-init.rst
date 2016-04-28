.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-mst-topology-mgr-init:

============================
drm_dp_mst_topology_mgr_init
============================

*man drm_dp_mst_topology_mgr_init(9)*

*4.6.0-rc5*

initialise a topology manager


Synopsis
========

.. c:function:: int drm_dp_mst_topology_mgr_init( struct drm_dp_mst_topology_mgr * mgr, struct device * dev, struct drm_dp_aux * aux, int max_dpcd_transaction_bytes, int max_payloads, int conn_base_id )

Arguments
=========

``mgr``
    manager struct to initialise

``dev``
    device providing this structure - for i2c addition.

``aux``
    DP helper aux channel to talk to this device

``max_dpcd_transaction_bytes``
    hw specific DPCD transaction limit

``max_payloads``
    maximum number of payloads this GPU can source

``conn_base_id``
    the connector object ID the MST device is connected to.


Description
===========

Return 0 for success, or negative error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
