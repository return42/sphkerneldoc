.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_dp_mst_helper.h

.. _`drm_dp_vcpi`:

struct drm_dp_vcpi
==================

.. c:type:: struct drm_dp_vcpi

    Virtual Channel Payload Identifier

.. _`drm_dp_vcpi.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_vcpi {
        int vcpi;
        int pbn;
        int aligned_pbn;
        int num_slots;
    }

.. _`drm_dp_vcpi.members`:

Members
-------

vcpi
    Virtual channel ID.

pbn
    Payload Bandwidth Number for this channel

aligned_pbn
    PBN aligned with slot size

num_slots
    number of slots for this PBN

.. _`drm_dp_mst_port`:

struct drm_dp_mst_port
======================

.. c:type:: struct drm_dp_mst_port

    MST port

.. _`drm_dp_mst_port.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_mst_port {
        struct kref kref;
        u8 port_num;
        bool input;
        bool mcs;
        bool ddps;
        u8 pdt;
        bool ldps;
        u8 dpcd_rev;
        u8 num_sdp_streams;
        u8 num_sdp_stream_sinks;
        uint16_t available_pbn;
        struct list_head next;
        struct drm_dp_mst_branch *mstb;
        struct drm_dp_aux aux;
        struct drm_dp_mst_branch *parent;
        struct drm_dp_vcpi vcpi;
        struct drm_connector *connector;
        struct drm_dp_mst_topology_mgr *mgr;
        struct edid *cached_edid;
        bool has_audio;
    }

.. _`drm_dp_mst_port.members`:

Members
-------

kref
    reference count for this port.

port_num
    port number

input
    if this port is an input port.

mcs
    message capability status - DP 1.2 spec.

ddps
    DisplayPort Device Plug Status - DP 1.2

pdt
    Peer Device Type

ldps
    Legacy Device Plug Status

dpcd_rev
    DPCD revision of device on this port

num_sdp_streams
    Number of simultaneous streams

num_sdp_stream_sinks
    Number of stream sinks

available_pbn
    Available bandwidth for this port.

next
    link to next port on this branch device

mstb
    branch device attach below this port

aux
    i2c aux transport to talk to device connected to this port.

parent
    branch device parent of this port

vcpi
    Virtual Channel Payload info for this port.

connector
    DRM connector this port is connected to.

mgr
    topology manager this port lives under.

cached_edid
    *undescribed*

has_audio
    *undescribed*

.. _`drm_dp_mst_port.description`:

Description
-----------

This structure represents an MST port endpoint on a device somewhere
in the MST topology.

.. _`drm_dp_mst_branch`:

struct drm_dp_mst_branch
========================

.. c:type:: struct drm_dp_mst_branch

    MST branch device.

.. _`drm_dp_mst_branch.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_mst_branch {
        struct kref kref;
        u8 rad[8];
        u8 lct;
        int num_ports;
        int msg_slots;
        struct list_head ports;
        struct drm_dp_mst_port *port_parent;
        struct drm_dp_mst_topology_mgr *mgr;
        struct drm_dp_sideband_msg_tx  *tx_slots[2];
        int last_seqno;
        bool link_address_sent;
        u8 guid[16];
    }

.. _`drm_dp_mst_branch.members`:

Members
-------

kref
    reference count for this port.

rad
    Relative Address to talk to this branch device.

lct
    Link count total to talk to this branch device.

num_ports
    number of ports on the branch.

msg_slots
    one bit per transmitted msg slot.

ports
    linked list of ports on this branch.

port_parent
    pointer to the port parent, NULL if toplevel.

mgr
    topology manager for this branch device.

tx_slots
    transmission slots for this device.

last_seqno
    last sequence number used to talk to this.

link_address_sent
    if a link address message has been sent to this device yet.

guid
    guid for DP 1.2 branch device. port under this branch can be
    identified by port #.

.. _`drm_dp_mst_branch.description`:

Description
-----------

This structure represents an MST branch device, there is one
primary branch device at the root, along with any other branches connected
to downstream port of parent branches.

.. _`drm_dp_mst_topology_mgr`:

struct drm_dp_mst_topology_mgr
==============================

.. c:type:: struct drm_dp_mst_topology_mgr

    DisplayPort MST manager

.. _`drm_dp_mst_topology_mgr.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_mst_topology_mgr {
        struct device *dev;
        const struct drm_dp_mst_topology_cbs *cbs;
        int max_dpcd_transaction_bytes;
        struct drm_dp_aux *aux;
        int max_payloads;
        int conn_base_id;
        struct drm_dp_sideband_msg_rx down_rep_recv;
        struct drm_dp_sideband_msg_rx up_req_recv;
        struct mutex lock;
        bool mst_state;
        struct drm_dp_mst_branch *mst_primary;
        u8 dpcd[DP_RECEIVER_CAP_SIZE];
        u8 sink_count;
        int pbn_div;
        int total_slots;
        int avail_slots;
        int total_pbn;
        struct mutex qlock;
        struct list_head tx_msg_downq;
        bool tx_down_in_progress;
        struct mutex payload_lock;
        struct drm_dp_vcpi **proposed_vcpis;
        struct drm_dp_payload *payloads;
        unsigned long payload_mask;
        unsigned long vcpi_mask;
        wait_queue_head_t tx_waitq;
        struct work_struct work;
        struct work_struct tx_work;
        struct list_head destroy_connector_list;
        struct mutex destroy_connector_lock;
        struct work_struct destroy_connector_work;
    }

.. _`drm_dp_mst_topology_mgr.members`:

Members
-------

dev
    device pointer for adding i2c devices etc.

cbs
    callbacks for connector addition and destruction.
    \ ``max_dpcd_transaction_bytes``\  - maximum number of bytes to read/write in one go.

max_dpcd_transaction_bytes
    *undescribed*

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

dpcd
    cache of DPCD for primary port.

sink_count
    *undescribed*

pbn_div
    PBN to slots divisor.

total_slots
    *undescribed*

avail_slots
    *undescribed*

total_pbn
    *undescribed*

qlock
    *undescribed*

tx_msg_downq
    *undescribed*

tx_down_in_progress
    *undescribed*

payload_lock
    *undescribed*

proposed_vcpis
    *undescribed*

payloads
    *undescribed*

payload_mask
    *undescribed*

vcpi_mask
    *undescribed*

tx_waitq
    *undescribed*

work
    *undescribed*

tx_work
    *undescribed*

destroy_connector_list
    *undescribed*

destroy_connector_lock
    *undescribed*

destroy_connector_work
    *undescribed*

.. _`drm_dp_mst_topology_mgr.description`:

Description
-----------

This struct represents the toplevel displayport MST topology manager.
There should be one instance of this for every MST capable DP connector
on the GPU.

.. This file was automatic generated / don't edit.

