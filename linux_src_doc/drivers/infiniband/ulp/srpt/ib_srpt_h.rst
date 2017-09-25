.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/srpt/ib_srpt.h

.. _`srpt_command_state`:

enum srpt_command_state
=======================

.. c:type:: enum srpt_command_state

    SCSI command state managed by SRPT.

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

    Shared SRPT I/O context information.

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
    *undescribed*

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

    SRPT receive I/O context.

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

    SRPT send I/O context.

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
        spinlock_t spinlock;
        enum srpt_command_state state;
        struct se_cmd cmd;
        struct completion tx_done;
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
    *undescribed*

rw_ctxs
    *undescribed*

rdma_cqe
    *undescribed*

free_list
    *undescribed*

spinlock
    Protects 'state'.

state
    I/O context state.

cmd
    Target core command data structure.

tx_done
    *undescribed*

n_rdma
    *undescribed*

n_rw_ctx
    *undescribed*

queue_status_only
    *undescribed*

sense_data
    SCSI sense data.

.. _`rdma_ch_state`:

enum rdma_ch_state
==================

.. c:type:: enum rdma_ch_state

    SRP channel state.

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

    RDMA channel.

.. _`srpt_rdma_ch.definition`:

Definition
----------

.. code-block:: c

    struct srpt_rdma_ch {
        struct ib_cm_id *cm_id;
        struct ib_qp *qp;
        struct ib_cq *cq;
        struct ib_cqe zw_cqe;
        struct kref kref;
        int rq_size;
        u32 rsp_size;
        atomic_t sq_wr_avail;
        struct srpt_port *sport;
        u8 i_port_id[16];
        u8 t_port_id[16];
        int max_ti_iu_len;
        atomic_t req_lim;
        atomic_t req_lim_delta;
        spinlock_t spinlock;
        struct list_head free_list;
        enum rdma_ch_state state;
        struct srpt_send_ioctx **ioctx_ring;
        struct list_head list;
        struct list_head cmd_wait_list;
        struct se_session *sess;
        u8 sess_name[36];
        u8 ini_guid[24];
        struct work_struct release_work;
        struct completion *release_done;
    }

.. _`srpt_rdma_ch.members`:

Members
-------

cm_id
    IB CM ID associated with the channel.

qp
    IB queue pair used for communicating over this channel.

cq
    IB completion queue for this channel.

zw_cqe
    *undescribed*

kref
    *undescribed*

rq_size
    IB receive queue size.
    \ ``rsp_size``\        IB response message size in bytes.

rsp_size
    *undescribed*

sq_wr_avail
    number of work requests available in the send queue.

sport
    pointer to the information of the HCA port used by this
    channel.

i_port_id
    128-bit initiator port identifier copied from SRP_LOGIN_REQ.

t_port_id
    128-bit target port identifier copied from SRP_LOGIN_REQ.

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

list
    Node for insertion in the srpt_device.rch_list list.

cmd_wait_list
    List of SCSI commands that arrived before the RTU event. This
    list contains struct srpt_ioctx elements and is protected
    against concurrent modification by the cm_id spinlock.

sess
    Session information associated with this SRP channel.

sess_name
    Session name.

ini_guid
    Initiator port GUID.

release_work
    Allows scheduling of \ :c:func:`srpt_release_channel`\ .

release_done
    Enables waiting for \ :c:func:`srpt_release_channel`\  completion.

.. _`srpt_port_attrib`:

struct srpt_port_attrib
=======================

.. c:type:: struct srpt_port_attrib

    Attributes for SRPT port

.. _`srpt_port_attrib.definition`:

Definition
----------

.. code-block:: c

    struct srpt_port_attrib {
        u32 srp_max_rdma_size;
        u32 srp_max_rsp_size;
        u32 srp_sq_size;
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

.. _`srpt_port`:

struct srpt_port
================

.. c:type:: struct srpt_port

    Information associated by SRPT with a single IB port.

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
    *undescribed*

.. _`srpt_device`:

struct srpt_device
==================

.. c:type:: struct srpt_device

    Information associated by SRPT with a single HCA.

.. _`srpt_device.definition`:

Definition
----------

.. code-block:: c

    struct srpt_device {
        struct ib_device *device;
        struct ib_pd *pd;
        struct ib_srq *srq;
        struct ib_cm_id *cm_id;
        int srq_size;
        struct srpt_recv_ioctx **ioctx_ring;
        struct list_head rch_list;
        wait_queue_head_t ch_releaseQ;
        struct mutex mutex;
        struct srpt_port port[2];
        struct ib_event_handler event_handler;
        struct list_head list;
    }

.. _`srpt_device.members`:

Members
-------

device
    Backpointer to the struct ib_device managed by the IB core.

pd
    IB protection domain.

srq
    Per-HCA SRQ (shared receive queue).

cm_id
    Connection identifier.

srq_size
    SRQ size.

ioctx_ring
    Per-HCA SRQ.

rch_list
    Per-device channel list -- see also srpt_rdma_ch.list.

ch_releaseQ
    Enables waiting for removal from rch_list.

mutex
    Protects rch_list.

port
    Information about the ports owned by this HCA.

event_handler
    Per-HCA asynchronous IB event handler.

list
    Node in srpt_dev_list.

.. This file was automatic generated / don't edit.

