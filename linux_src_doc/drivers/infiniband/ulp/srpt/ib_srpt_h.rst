.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/srpt/ib_srpt.h

.. _`srpt_command_state`:

enum srpt_command_state
=======================

.. c:type:: enum srpt_command_state

    SCSI command state managed by SRPT

.. _`srpt_command_state.definition`:

Definition
----------

.. code-block:: c

    enum srpt_command_state {
        SRPT_STATE_NEW,
        SRPT_STATE_NEED_DATA,
        SRPT_STATE_DATA_IN,
        SRPT_STATE_CMD_RSP_SENT,
        SRPT_STATE_MGMT,
        SRPT_STATE_MGMT_RSP_SENT,
        SRPT_STATE_DONE
    };

.. _`srpt_command_state.constants`:

Constants
---------

SRPT_STATE_NEW
    New command arrived and is being processed.

SRPT_STATE_NEED_DATA
    Processing a write or bidir command and waiting
    for data arrival.

SRPT_STATE_DATA_IN
    Data for the write or bidir command arrived and is
    being processed.

SRPT_STATE_CMD_RSP_SENT
    SRP_RSP for SRP_CMD has been sent.

SRPT_STATE_MGMT
    Processing a SCSI task management command.

SRPT_STATE_MGMT_RSP_SENT
    SRP_RSP for SRP_TSK_MGMT has been sent.

SRPT_STATE_DONE
    Command processing finished successfully, command
    processing has been aborted or command processing
    failed.

.. _`srpt_ioctx`:

struct srpt_ioctx
=================

.. c:type:: struct srpt_ioctx

    shared SRPT I/O context information

.. _`srpt_ioctx.definition`:

Definition
----------

.. code-block:: c

    struct srpt_ioctx {
        struct ib_cqe cqe;
        void *buf;
        dma_addr_t dma;
        uint32_t index;
    }

.. _`srpt_ioctx.members`:

Members
-------

cqe
    Completion queue element.

buf
    Pointer to the buffer.

dma
    DMA address of the buffer.

index
    Index of the I/O context in its ioctx_ring array.

.. _`srpt_recv_ioctx`:

struct srpt_recv_ioctx
======================

.. c:type:: struct srpt_recv_ioctx

    SRPT receive I/O context

.. _`srpt_recv_ioctx.definition`:

Definition
----------

.. code-block:: c

    struct srpt_recv_ioctx {
        struct srpt_ioctx ioctx;
        struct list_head wait_list;
    }

.. _`srpt_recv_ioctx.members`:

Members
-------

ioctx
    See above.

wait_list
    Node for insertion in srpt_rdma_ch.cmd_wait_list.

.. _`srpt_send_ioctx`:

struct srpt_send_ioctx
======================

.. c:type:: struct srpt_send_ioctx

    SRPT send I/O context

.. _`srpt_send_ioctx.definition`:

Definition
----------

.. code-block:: c

    struct srpt_send_ioctx {
        struct srpt_ioctx ioctx;
        struct srpt_rdma_ch *ch;
        struct srpt_rw_ctx s_rw_ctx;
        struct srpt_rw_ctx *rw_ctxs;
        struct ib_cqe rdma_cqe;
        struct list_head free_list;
        enum srpt_command_state state;
        struct se_cmd cmd;
        u8 n_rdma;
        u8 n_rw_ctx;
        bool queue_status_only;
        u8 sense_data[TRANSPORT_SENSE_BUFFER];
    }

.. _`srpt_send_ioctx.members`:

Members
-------

ioctx
    See above.

ch
    Channel pointer.

s_rw_ctx
    \ ``rw_ctxs``\  points here if only a single rw_ctx is needed.

rw_ctxs
    RDMA read/write contexts.

rdma_cqe
    RDMA completion queue element.

free_list
    Node in srpt_rdma_ch.free_list.

state
    I/O context state.

cmd
    Target core command data structure.

n_rdma
    Number of work requests needed to transfer this ioctx.

n_rw_ctx
    Size of rw_ctxs array.

queue_status_only
    Send a SCSI status back to the initiator but no data.

sense_data
    Sense data to be sent to the initiator.

.. _`rdma_ch_state`:

enum rdma_ch_state
==================

.. c:type:: enum rdma_ch_state

    SRP channel state

.. _`rdma_ch_state.definition`:

Definition
----------

.. code-block:: c

    enum rdma_ch_state {
        CH_CONNECTING,
        CH_LIVE,
        CH_DISCONNECTING,
        CH_DRAINING,
        CH_DISCONNECTED
    };

.. _`rdma_ch_state.constants`:

Constants
---------

CH_CONNECTING
    QP is in RTR state; waiting for RTU.

CH_LIVE
    QP is in RTS state.

CH_DISCONNECTING
    DREQ has been sent and waiting for DREP or DREQ has
    been received.

CH_DRAINING
    DREP has been received or waiting for DREP timed out
    and last work request has been queued.

CH_DISCONNECTED
    Last completion has been received.

.. _`srpt_rdma_ch`:

struct srpt_rdma_ch
===================

.. c:type:: struct srpt_rdma_ch

    RDMA channel

.. _`srpt_rdma_ch.definition`:

Definition
----------

.. code-block:: c

    struct srpt_rdma_ch {
        struct srpt_nexus *nexus;
        struct ib_qp *qp;
        union {
            struct {
                struct ib_cm_id *cm_id;
            } ib_cm;
            struct {
                struct rdma_cm_id *cm_id;
            } rdma_cm;
        } ;
        struct ib_cq *cq;
        struct ib_cqe zw_cqe;
        struct rcu_head rcu;
        struct kref kref;
        int rq_size;
        u32 max_rsp_size;
        atomic_t sq_wr_avail;
        struct srpt_port *sport;
        int max_ti_iu_len;
        atomic_t req_lim;
        atomic_t req_lim_delta;
        spinlock_t spinlock;
        struct list_head free_list;
        enum rdma_ch_state state;
        struct srpt_send_ioctx **ioctx_ring;
        struct srpt_recv_ioctx **ioctx_recv_ring;
        struct list_head list;
        struct list_head cmd_wait_list;
        uint16_t pkey;
        bool using_rdma_cm;
        bool processing_wait_list;
        struct se_session *sess;
        u8 sess_name[40];
        struct work_struct release_work;
    }

.. _`srpt_rdma_ch.members`:

Members
-------

nexus
    I_T nexus this channel is associated with.

qp
    IB queue pair used for communicating over this channel.

{unnamed_union}
    anonymous

ib_cm
    *undescribed*

rdma_cm
    *undescribed*

cq
    IB completion queue for this channel.

zw_cqe
    Zero-length write CQE.

rcu
    RCU head.

kref
    kref for this channel.

rq_size
    IB receive queue size.

max_rsp_size
    Maximum size of an RSP response message in bytes.

sq_wr_avail
    number of work requests available in the send queue.

sport
    pointer to the information of the HCA port used by this
    channel.

max_ti_iu_len
    maximum target-to-initiator information unit length.

req_lim
    request limit: maximum number of requests that may be sent
    by the initiator without having received a response.

req_lim_delta
    Number of credits not yet sent back to the initiator.

spinlock
    Protects free_list and state.

free_list
    Head of list with free send I/O contexts.

state
    channel state. See also enum rdma_ch_state.

ioctx_ring
    Send ring.

ioctx_recv_ring
    Receive I/O context ring.

list
    Node in srpt_nexus.ch_list.

cmd_wait_list
    List of SCSI commands that arrived before the RTU event. This
    list contains struct srpt_ioctx elements and is protected
    against concurrent modification by the cm_id spinlock.

pkey
    P_Key of the IB partition for this SRP channel.

using_rdma_cm
    Whether the RDMA/CM or IB/CM is used for this channel.

processing_wait_list
    Whether or not cmd_wait_list is being processed.

sess
    Session information associated with this SRP channel.

sess_name
    Session name.

release_work
    Allows scheduling of \ :c:func:`srpt_release_channel`\ .

.. _`srpt_nexus`:

struct srpt_nexus
=================

.. c:type:: struct srpt_nexus

    I_T nexus

.. _`srpt_nexus.definition`:

Definition
----------

.. code-block:: c

    struct srpt_nexus {
        struct rcu_head rcu;
        struct list_head entry;
        struct list_head ch_list;
        u8 i_port_id[16];
        u8 t_port_id[16];
    }

.. _`srpt_nexus.members`:

Members
-------

rcu
    RCU head for this data structure.

entry
    srpt_port.nexus_list list node.

ch_list
    struct srpt_rdma_ch list. Protected by srpt_port.mutex.

i_port_id
    128-bit initiator port identifier copied from SRP_LOGIN_REQ.

t_port_id
    128-bit target port identifier copied from SRP_LOGIN_REQ.

.. _`srpt_port_attrib`:

struct srpt_port_attrib
=======================

.. c:type:: struct srpt_port_attrib

    attributes for SRPT port

.. _`srpt_port_attrib.definition`:

Definition
----------

.. code-block:: c

    struct srpt_port_attrib {
        u32 srp_max_rdma_size;
        u32 srp_max_rsp_size;
        u32 srp_sq_size;
        bool use_srq;
    }

.. _`srpt_port_attrib.members`:

Members
-------

srp_max_rdma_size
    Maximum size of SRP RDMA transfers for new connections.

srp_max_rsp_size
    Maximum size of SRP response messages in bytes.

srp_sq_size
    Shared receive queue (SRQ) size.

use_srq
    Whether or not to use SRQ.

.. _`srpt_port`:

struct srpt_port
================

.. c:type:: struct srpt_port

    information associated by SRPT with a single IB port

.. _`srpt_port.definition`:

Definition
----------

.. code-block:: c

    struct srpt_port {
        struct srpt_device *sdev;
        struct ib_mad_agent *mad_agent;
        bool enabled;
        u8 port_guid[24];
        u8 port_gid[64];
        u8 port;
        u32 sm_lid;
        u32 lid;
        union ib_gid gid;
        struct work_struct work;
        struct se_portal_group port_guid_tpg;
        struct se_wwn port_guid_wwn;
        struct se_portal_group port_gid_tpg;
        struct se_wwn port_gid_wwn;
        struct srpt_port_attrib port_attrib;
        wait_queue_head_t ch_releaseQ;
        struct mutex mutex;
        struct list_head nexus_list;
    }

.. _`srpt_port.members`:

Members
-------

sdev
    backpointer to the HCA information.

mad_agent
    per-port management datagram processing information.

enabled
    Whether or not this target port is enabled.

port_guid
    ASCII representation of Port GUID

port_gid
    ASCII representation of Port GID

port
    one-based port number.

sm_lid
    cached value of the port's sm_lid.

lid
    cached value of the port's lid.

gid
    cached value of the port's gid.

work
    work structure for refreshing the aforementioned cached values.

port_guid_tpg
    TPG associated with target port GUID.

port_guid_wwn
    WWN associated with target port GUID.

port_gid_tpg
    TPG associated with target port GID.

port_gid_wwn
    WWN associated with target port GID.

port_attrib
    Port attributes that can be accessed through configfs.

ch_releaseQ
    Enables waiting for removal from nexus_list.

mutex
    Protects nexus_list.

nexus_list
    Nexus list. See also srpt_nexus.entry.

.. _`srpt_device`:

struct srpt_device
==================

.. c:type:: struct srpt_device

    information associated by SRPT with a single HCA

.. _`srpt_device.definition`:

Definition
----------

.. code-block:: c

    struct srpt_device {
        struct ib_device *device;
        struct ib_pd *pd;
        u32 lkey;
        struct ib_srq *srq;
        struct ib_cm_id *cm_id;
        int srq_size;
        struct mutex sdev_mutex;
        bool use_srq;
        struct srpt_recv_ioctx **ioctx_ring;
        struct ib_event_handler event_handler;
        struct list_head list;
        struct srpt_port port[];
    }

.. _`srpt_device.members`:

Members
-------

device
    Backpointer to the struct ib_device managed by the IB core.

pd
    IB protection domain.

lkey
    L_Key (local key) with write access to all local memory.

srq
    Per-HCA SRQ (shared receive queue).

cm_id
    Connection identifier.

srq_size
    SRQ size.

sdev_mutex
    Serializes use_srq changes.

use_srq
    Whether or not to use SRQ.

ioctx_ring
    Per-HCA SRQ.

event_handler
    Per-HCA asynchronous IB event handler.

list
    Node in srpt_dev_list.

port
    Information about the ports owned by this HCA.

.. This file was automatic generated / don't edit.

