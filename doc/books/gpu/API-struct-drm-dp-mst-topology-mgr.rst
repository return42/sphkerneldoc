.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-dp-mst-topology-mgr:

==============================
struct drm_dp_mst_topology_mgr
==============================

*man struct drm_dp_mst_topology_mgr(9)*

*4.6.0-rc5*

DisplayPort MST manager


Synopsis
========

.. code-block:: c

    struct drm_dp_mst_topology_mgr {
      struct device * dev;
      const struct drm_dp_mst_topology_cbs * cbs;
      struct drm_dp_aux * aux;
      int max_payloads;
      int conn_base_id;
      struct drm_dp_sideband_msg_rx down_rep_recv;
      struct drm_dp_sideband_msg_rx up_req_recv;
      struct mutex lock;
      bool mst_state;
      struct drm_dp_mst_branch * mst_primary;
      u8 dpcd[DP_RECEIVER_CAP_SIZE];
      int pbn_div;
    };


Members
=======

dev
    device pointer for adding i2c devices etc.

cbs
    callbacks for connector addition and destruction.
    ``max_dpcd_transaction_bytes`` - maximum number of bytes to
    read/write in one go.

aux
    aux channel for the DP connector.

max_payloads
    maximum number of payloads the GPU can generate.

conn_base_id
    DRM connector ID this mgr is connected to.

down_rep_recv
    msg receiver state for down replies.

up_req_recv
    msg receiver state for up requests.

lock
    protects mst state, primary, dpcd.

mst_state
    if this manager is enabled for an MST capable port.

mst_primary
    pointer to the primary branch device.

dpcd[DP_RECEIVER_CAP_SIZE]
    cache of DPCD for primary port.

pbn_div
    PBN to slots divisor.


Description
===========

This struct represents the toplevel displayport MST topology manager.
There should be one instance of this for every MST capable DP connector
on the GPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
