.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/libfc.h

.. _`fc_lport_state`:

enum fc_lport_state
===================

.. c:type:: enum fc_lport_state

    Local port states

.. _`fc_lport_state.definition`:

Definition
----------

.. code-block:: c

    enum fc_lport_state {
        LPORT_ST_DISABLED,
        LPORT_ST_FLOGI,
        LPORT_ST_DNS,
        LPORT_ST_RNN_ID,
        LPORT_ST_RSNN_NN,
        LPORT_ST_RSPN_ID,
        LPORT_ST_RFT_ID,
        LPORT_ST_RFF_ID,
        LPORT_ST_FDMI,
        LPORT_ST_RHBA,
        LPORT_ST_RPA,
        LPORT_ST_DHBA,
        LPORT_ST_DPRT,
        LPORT_ST_SCR,
        LPORT_ST_READY,
        LPORT_ST_LOGO,
        LPORT_ST_RESET
    };

.. _`fc_lport_state.constants`:

Constants
---------

LPORT_ST_DISABLED
    Disabled

LPORT_ST_FLOGI
    Fabric login (FLOGI) sent

LPORT_ST_DNS
    Waiting for name server remote port to become ready

LPORT_ST_RNN_ID
    *undescribed*

LPORT_ST_RSNN_NN
    *undescribed*

LPORT_ST_RSPN_ID
    *undescribed*

LPORT_ST_RFT_ID
    Register Fibre Channel types by ID (RFT_ID) sent

LPORT_ST_RFF_ID
    Register FC-4 Features by ID (RFF_ID) sent

LPORT_ST_FDMI
    Waiting for mgmt server rport to become ready

LPORT_ST_RHBA
    *undescribed*

LPORT_ST_RPA
    *undescribed*

LPORT_ST_DHBA
    *undescribed*

LPORT_ST_DPRT
    *undescribed*

LPORT_ST_SCR
    State Change Register (SCR) sent

LPORT_ST_READY
    Ready for use

LPORT_ST_LOGO
    Local port logout (LOGO) sent

LPORT_ST_RESET
    Local port reset

.. _`fc_rport_state`:

enum fc_rport_state
===================

.. c:type:: enum fc_rport_state

    Remote port states

.. _`fc_rport_state.definition`:

Definition
----------

.. code-block:: c

    enum fc_rport_state {
        RPORT_ST_INIT,
        RPORT_ST_FLOGI,
        RPORT_ST_PLOGI_WAIT,
        RPORT_ST_PLOGI,
        RPORT_ST_PRLI,
        RPORT_ST_RTV,
        RPORT_ST_READY,
        RPORT_ST_ADISC,
        RPORT_ST_DELETE
    };

.. _`fc_rport_state.constants`:

Constants
---------

RPORT_ST_INIT
    Initialized

RPORT_ST_FLOGI
    Waiting for FLOGI completion for point-to-multipoint

RPORT_ST_PLOGI_WAIT
    Waiting for peer to login for point-to-multipoint

RPORT_ST_PLOGI
    Waiting for PLOGI completion

RPORT_ST_PRLI
    Waiting for PRLI completion

RPORT_ST_RTV
    Waiting for RTV completion

RPORT_ST_READY
    Ready for use

RPORT_ST_ADISC
    Discover Address sent

RPORT_ST_DELETE
    Remote port being deleted

.. _`fc_disc_port`:

struct fc_disc_port
===================

.. c:type:: struct fc_disc_port

    temporary discovery port to hold rport identifiers

.. _`fc_disc_port.definition`:

Definition
----------

.. code-block:: c

    struct fc_disc_port {
        struct fc_lport *lp;
        struct list_head peers;
        struct work_struct rport_work;
        u32 port_id;
    }

.. _`fc_disc_port.members`:

Members
-------

lp
    Fibre Channel host port instance

peers
    Node for list management during discovery and RSCN processing

rport_work
    Work struct for starting the rport state machine

port_id
    Port ID of the discovered port

.. _`fc_rport_event`:

enum fc_rport_event
===================

.. c:type:: enum fc_rport_event

    Remote port events

.. _`fc_rport_event.definition`:

Definition
----------

.. code-block:: c

    enum fc_rport_event {
        RPORT_EV_NONE,
        RPORT_EV_READY,
        RPORT_EV_FAILED,
        RPORT_EV_STOP,
        RPORT_EV_LOGO
    };

.. _`fc_rport_event.constants`:

Constants
---------

RPORT_EV_NONE
    No event

RPORT_EV_READY
    Remote port is ready for use

RPORT_EV_FAILED
    State machine failed, remote port is not ready

RPORT_EV_STOP
    Remote port has been stopped

RPORT_EV_LOGO
    Remote port logout (LOGO) sent

.. _`fc_rport_operations`:

struct fc_rport_operations
==========================

.. c:type:: struct fc_rport_operations

    Operations for a remote port

.. _`fc_rport_operations.definition`:

Definition
----------

.. code-block:: c

    struct fc_rport_operations {
        void (*event_callback)(struct fc_lport *, struct fc_rport_priv *,enum fc_rport_event);
    }

.. _`fc_rport_operations.members`:

Members
-------

event_callback
    Function to be called for remote port events

.. _`fc_rport_libfc_priv`:

struct fc_rport_libfc_priv
==========================

.. c:type:: struct fc_rport_libfc_priv

    libfc internal information about a remote port

.. _`fc_rport_libfc_priv.definition`:

Definition
----------

.. code-block:: c

    struct fc_rport_libfc_priv {
        struct fc_lport *local_port;
        enum fc_rport_state rp_state;
        u16 flags;
    #define FC_RP_FLAGS_REC_SUPPORTED (1 << 0)
    #define FC_RP_FLAGS_RETRY (1 << 1)
    #define FC_RP_STARTED (1 << 2)
    #define FC_RP_FLAGS_CONF_REQ (1 << 3)
        unsigned int e_d_tov;
        unsigned int r_a_tov;
    }

.. _`fc_rport_libfc_priv.members`:

Members
-------

local_port
    The associated local port

rp_state
    Indicates READY for I/O or DELETE when blocked

flags
    REC and RETRY supported flags

e_d_tov
    Error detect timeout value (in msec)

r_a_tov
    Resource allocation timeout value (in msec)

.. _`fc_rport_priv`:

struct fc_rport_priv
====================

.. c:type:: struct fc_rport_priv

    libfc remote port and discovery info

.. _`fc_rport_priv.definition`:

Definition
----------

.. code-block:: c

    struct fc_rport_priv {
        struct fc_lport *local_port;
        struct fc_rport *rport;
        struct kref kref;
        enum fc_rport_state rp_state;
        struct fc_rport_identifiers ids;
        u16 flags;
        u16 max_seq;
        u16 disc_id;
        u16 maxframe_size;
        unsigned int retries;
        unsigned int major_retries;
        unsigned int e_d_tov;
        unsigned int r_a_tov;
        struct mutex rp_mutex;
        struct delayed_work retry_work;
        enum fc_rport_event event;
        struct fc_rport_operations *ops;
        struct list_head peers;
        struct work_struct event_work;
        u32 supported_classes;
        u16 prli_count;
        struct rcu_head rcu;
        u16 sp_features;
        u8 spp_type;
        void (*lld_event_callback)(struct fc_lport *,struct fc_rport_priv *,enum fc_rport_event);
    }

.. _`fc_rport_priv.members`:

Members
-------

local_port
    The associated local port

rport
    The FC transport remote port

kref
    Reference counter

rp_state
    Enumeration that tracks progress of PLOGI, PRLI,
    and RTV exchanges

ids
    The remote port identifiers and roles

flags
    STARTED, REC and RETRY_SUPPORTED flags

max_seq
    Maximum number of concurrent sequences

disc_id
    The discovery identifier

maxframe_size
    The maximum frame size

retries
    The retry count for the current state

major_retries
    The retry count for the entire PLOGI/PRLI state machine

e_d_tov
    Error detect timeout value (in msec)

r_a_tov
    Resource allocation timeout value (in msec)

rp_mutex
    The mutex that protects the remote port

retry_work
    Handle for retries

event
    *undescribed*

ops
    *undescribed*

peers
    *undescribed*

event_work
    *undescribed*

supported_classes
    *undescribed*

prli_count
    Count of open PRLI sessions in providers

rcu
    Structure used for freeing in an RCU-safe manner

sp_features
    *undescribed*

spp_type
    *undescribed*

lld_event_callback
    *undescribed*

.. _`fc_stats`:

struct fc_stats
===============

.. c:type:: struct fc_stats

    fc stats structure

.. _`fc_stats.definition`:

Definition
----------

.. code-block:: c

    struct fc_stats {
        u64 SecondsSinceLastReset;
        u64 TxFrames;
        u64 TxWords;
        u64 RxFrames;
        u64 RxWords;
        u64 ErrorFrames;
        u64 DumpedFrames;
        u64 FcpPktAllocFails;
        u64 FcpPktAborts;
        u64 FcpFrameAllocFails;
        u64 LinkFailureCount;
        u64 LossOfSignalCount;
        u64 InvalidTxWordCount;
        u64 InvalidCRCCount;
        u64 InputRequests;
        u64 OutputRequests;
        u64 ControlRequests;
        u64 InputBytes;
        u64 OutputBytes;
        u64 VLinkFailureCount;
        u64 MissDiscAdvCount;
    }

.. _`fc_stats.members`:

Members
-------

SecondsSinceLastReset
    Seconds since the last reset

TxFrames
    Number of transmitted frames

TxWords
    Number of transmitted words

RxFrames
    Number of received frames

RxWords
    Number of received words

ErrorFrames
    Number of received error frames

DumpedFrames
    Number of dumped frames

FcpPktAllocFails
    Number of fcp packet allocation failures

FcpPktAborts
    Number of fcp packet aborts

FcpFrameAllocFails
    Number of fcp frame allocation failures

LinkFailureCount
    Number of link failures

LossOfSignalCount
    Number for signal losses

InvalidTxWordCount
    Number of invalid transmitted words

InvalidCRCCount
    Number of invalid CRCs

InputRequests
    Number of input requests

OutputRequests
    Number of output requests

ControlRequests
    Number of control requests

InputBytes
    Number of received bytes

OutputBytes
    Number of transmitted bytes

VLinkFailureCount
    Number of virtual link failures

MissDiscAdvCount
    Number of missing FIP discovery advertisement

.. _`fc_seq_els_data`:

struct fc_seq_els_data
======================

.. c:type:: struct fc_seq_els_data

    ELS data used for passing ELS specific responses

.. _`fc_seq_els_data.definition`:

Definition
----------

.. code-block:: c

    struct fc_seq_els_data {
        enum fc_els_rjt_reason reason;
        enum fc_els_rjt_explan explan;
    }

.. _`fc_seq_els_data.members`:

Members
-------

reason
    The reason for rejection

explan
    The explanation of the rejection

.. _`fc_seq_els_data.description`:

Description
-----------

Mainly used by the exchange manager layer.

.. _`fc_fcp_pkt`:

struct fc_fcp_pkt
=================

.. c:type:: struct fc_fcp_pkt

    FCP request structure (one for each scsi_cmnd request)

.. _`fc_fcp_pkt.definition`:

Definition
----------

.. code-block:: c

    struct fc_fcp_pkt {
        spinlock_t scsi_pkt_lock;
        atomic_t ref_cnt;
        u32 data_len;
        struct scsi_cmnd *cmd;
        struct list_head list;
        struct fc_lport *lp;
        u8 state;
        u8 cdb_status;
        u8 status_code;
        u8 scsi_comp_flags;
        u32 io_status;
        u32 req_flags;
        u32 scsi_resid;
        size_t xfer_len;
        struct fcp_cmnd cdb_cmd;
        u32 xfer_contig_end;
        u16 max_payload;
        u16 xfer_ddp;
        struct fc_rport *rport;
        struct fc_seq *seq_ptr;
        struct timer_list timer;
        int wait_for_comp;
        u32 recov_retry;
        struct fc_seq *recov_seq;
        struct completion tm_done;
    }

.. _`fc_fcp_pkt.members`:

Members
-------

scsi_pkt_lock
    Lock to protect the SCSI packet (must be taken before the
    host_lock if both are to be held at the same time)

ref_cnt
    Reference count

data_len
    The length of the data

cmd
    The SCSI command (set and clear with the host_lock held)

list
    Tracks queued commands (accessed with the host_lock held)

lp
    The associated local port

state
    The state of the I/O

cdb_status
    CDB status

status_code
    FCP I/O status

scsi_comp_flags
    Completion flags (bit 3 Underrun bit 2: overrun)

io_status
    SCSI result (upper 24 bits)

req_flags
    Request flags (bit 0: read bit:1 write)

scsi_resid
    SCSI residule length

xfer_len
    The transfer length

cdb_cmd
    The CDB command

xfer_contig_end
    The offset into the buffer if the buffer is contiguous
    (Tx and Rx)

max_payload
    The maximum payload size (in bytes)

xfer_ddp
    Indicates if this transfer used DDP (XID of the exchange
    will be set here if DDP was setup)

rport
    The remote port that the SCSI command is targeted at

seq_ptr
    The sequence that will carry the SCSI command

timer
    The command timer

wait_for_comp
    Indicator to wait for completion of the I/O (in jiffies)

recov_retry
    Number of recovery retries

recov_seq
    The sequence for REC or SRR

tm_done
    Completion indicator

.. _`fc_seq`:

struct fc_seq
=============

.. c:type:: struct fc_seq

    FC sequence

.. _`fc_seq.definition`:

Definition
----------

.. code-block:: c

    struct fc_seq {
        u8 id;
        u16 ssb_stat;
        u16 cnt;
        u32 rec_data;
    }

.. _`fc_seq.members`:

Members
-------

id
    The sequence ID

ssb_stat
    Status flags for the sequence status block (SSB)

cnt
    Number of frames sent so far

rec_data
    FC-4 value for REC

.. _`fc_exch`:

struct fc_exch
==============

.. c:type:: struct fc_exch

    Fibre Channel Exchange

.. _`fc_exch.definition`:

Definition
----------

.. code-block:: c

    struct fc_exch {
        spinlock_t ex_lock;
        atomic_t ex_refcnt;
        enum fc_class class;
        struct fc_exch_mgr *em;
        struct fc_exch_pool *pool;
        struct list_head ex_list;
        struct fc_lport *lp;
        u32 esb_stat;
        u8 state;
        u8 fh_type;
        u8 seq_id;
        u8 encaps;
        u16 xid;
        u16 oxid;
        u16 rxid;
        u32 oid;
        u32 sid;
        u32 did;
        u32 r_a_tov;
        u32 f_ctl;
        struct fc_seq seq;
        int resp_active;
        struct task_struct *resp_task;
        wait_queue_head_t resp_wq;
        void (*resp)(struct fc_seq *, struct fc_frame *, void *);
        void *arg;
        void (*destructor)(struct fc_seq *, void *);
        struct delayed_work timeout_work;
    }

.. _`fc_exch.members`:

Members
-------

ex_lock
    Lock that protects the exchange

ex_refcnt
    Reference count

class
    The class of service

em
    Exchange manager

pool
    Exchange pool

ex_list
    Handle used by the EM to track free exchanges

lp
    The local port that this exchange is on

esb_stat
    ESB exchange status

state
    The exchange's state

fh_type
    The frame type

seq_id
    The next sequence ID to use

encaps
    encapsulation information for lower-level driver

xid
    The exchange ID

oxid
    Originator's exchange ID

rxid
    Responder's exchange ID

oid
    Originator's FCID

sid
    Source FCID

did
    Destination FCID

r_a_tov
    Resouce allocation time out value (in msecs)

f_ctl
    F_CTL flags for the sequence

seq
    The sequence in use on this exchange

resp_active
    Number of tasks that are concurrently executing @\ :c:func:`resp`\ .

resp_task
    If \ ``resp_active``\  > 0, either the task executing @\ :c:func:`resp`\ , the
    task that has been interrupted to execute the soft-IRQ
    executing @\ :c:func:`resp`\  or NULL if more than one task is executing
    \ ``resp``\  concurrently.

resp_wq
    Waitqueue for the tasks waiting on \ ``resp_active``\ .

resp
    Callback for responses on this exchange

arg
    Passed as a void pointer to the \ :c:func:`resp`\  callback

destructor
    Called when destroying the exchange

timeout_work
    Handle for timeout handler

.. _`fc_exch.locking-notes`:

Locking notes
-------------

The ex_lock protects following items:
state, esb_stat, f_ctl, seq.ssb_stat
seq_id
sequence allocation

.. _`fc_disc`:

struct fc_disc
==============

.. c:type:: struct fc_disc

    Discovery context

.. _`fc_disc.definition`:

Definition
----------

.. code-block:: c

    struct fc_disc {
        unsigned char retry_count;
        unsigned char pending;
        unsigned char requested;
        unsigned short seq_count;
        unsigned char buf_len;
        u16 disc_id;
        struct list_head rports;
        void *priv;
        struct mutex disc_mutex;
        struct fc_gpn_ft_resp partial_buf;
        struct delayed_work disc_work;
        void (*disc_callback)(struct fc_lport *,enum fc_disc_event);
    }

.. _`fc_disc.members`:

Members
-------

retry_count
    Number of retries

pending
    1 if discovery is pending, 0 if not

requested
    1 if discovery has been requested, 0 if not

seq_count
    Number of sequences used for discovery

buf_len
    Length of the discovery buffer

disc_id
    Discovery ID

rports
    List of discovered remote ports

priv
    Private pointer for use by discovery code

disc_mutex
    Mutex that protects the discovery context

partial_buf
    Partial name buffer (if names are returned
    in multiple frames)

disc_work
    handle for delayed work context

disc_callback
    Callback routine called when discovery completes

.. _`fc_lport`:

struct fc_lport
===============

.. c:type:: struct fc_lport

    Local port

.. _`fc_lport.definition`:

Definition
----------

.. code-block:: c

    struct fc_lport {
        struct Scsi_Host *host;
        struct list_head ema_list;
        struct fc_rport_priv *dns_rdata;
        struct fc_rport_priv *ms_rdata;
        struct fc_rport_priv *ptp_rdata;
        void *scsi_priv;
        struct fc_disc disc;
        struct list_head vports;
        struct fc_vport *vport;
        struct libfc_function_template tt;
        u8 link_up;
        u8 qfull;
        enum fc_lport_state state;
        unsigned long boot_time;
        struct fc_host_statistics host_stats;
        struct fc_stats __percpu *stats;
        u8 retry_count;
        u32 port_id;
        u64 wwpn;
        u64 wwnn;
        unsigned int service_params;
        unsigned int e_d_tov;
        unsigned int r_a_tov;
        struct fc_els_rnid_gen rnid_gen;
        u32 sg_supp:1;
        u32 seq_offload:1;
        u32 crc_offload:1;
        u32 lro_enabled:1;
        u32 does_npiv:1;
        u32 npiv_enabled:1;
        u32 point_to_multipoint:1;
        u32 fdmi_enabled:1;
        u32 mfs;
        u8 max_retry_count;
        u8 max_rport_retry_count;
        u16 rport_priv_size;
        u16 link_speed;
        u16 link_supported_speeds;
        u16 lro_xid;
        unsigned int lso_max;
        struct fc_ns_fts fcts;
        struct mutex lp_mutex;
        struct list_head list;
        struct delayed_work retry_work;
        void  *prov[FC_FC4_PROV_SIZE];
        struct list_head lport_list;
    }

.. _`fc_lport.members`:

Members
-------

host
    The SCSI host associated with a local port

ema_list
    Exchange manager anchor list

dns_rdata
    The directory server remote port

ms_rdata
    The management server remote port

ptp_rdata
    Point to point remote port

scsi_priv
    FCP layer internal data

disc
    Discovery context

vports
    Child vports if N_Port

vport
    Parent vport if VN_Port

tt
    Libfc function template

link_up
    Link state (1 = link up, 0 = link down)

qfull
    Queue state (1 queue is full, 0 queue is not full)

state
    Identifies the state

boot_time
    Timestamp indicating when the local port came online

host_stats
    SCSI host statistics

stats
    FC local port stats (TODO separate libfc LLD stats)

retry_count
    Number of retries in the current state

port_id
    FC Port ID

wwpn
    World Wide Port Name

wwnn
    World Wide Node Name

service_params
    Common service parameters

e_d_tov
    Error detection timeout value

r_a_tov
    Resouce allocation timeout value

rnid_gen
    RNID information

sg_supp
    Indicates if scatter gather is supported

seq_offload
    Indicates if sequence offload is supported

crc_offload
    Indicates if CRC offload is supported

lro_enabled
    Indicates if large receive offload is supported

does_npiv
    Supports multiple vports

npiv_enabled
    Switch/fabric allows NPIV

point_to_multipoint
    *undescribed*

fdmi_enabled
    *undescribed*

mfs
    The maximum Fibre Channel payload size

max_retry_count
    The maximum retry attempts

max_rport_retry_count
    The maximum remote port retry attempts

rport_priv_size
    Size needed by driver after struct fc_rport_priv

link_speed
    *undescribed*

link_supported_speeds
    *undescribed*

lro_xid
    The maximum XID for LRO

lso_max
    The maximum large offload send size

fcts
    FC-4 type mask

lp_mutex
    Mutex to protect the local port

list
    Linkage on list of vport peers

retry_work
    Handle to local port for delayed retry context

prov
    Pointers available for use by passive FC-4 providers

lport_list
    Linkage on module-wide list of local ports

.. _`fc4_prov`:

struct fc4_prov
===============

.. c:type:: struct fc4_prov

    FC-4 provider registration

.. _`fc4_prov.definition`:

Definition
----------

.. code-block:: c

    struct fc4_prov {
        int (*prli)(struct fc_rport_priv *, u32 spp_len,const struct fc_els_spp *spp_in,struct fc_els_spp *spp_out);
        void (*prlo)(struct fc_rport_priv *);
        void (*recv)(struct fc_lport *, struct fc_frame *);
        struct module *module;
    }

.. _`fc4_prov.members`:

Members
-------

prli
    Handler for incoming PRLI

prlo
    Handler for session reset

recv
    Handler for incoming request

module
    Pointer to module.  May be NULL.

.. _`fc_lport_test_ready`:

fc_lport_test_ready
===================

.. c:function:: int fc_lport_test_ready(struct fc_lport *lport)

    Determine if a local port is in the READY state

    :param struct fc_lport \*lport:
        The local port to test

.. _`fc_set_wwnn`:

fc_set_wwnn
===========

.. c:function:: void fc_set_wwnn(struct fc_lport *lport, u64 wwnn)

    Set the World Wide Node Name of a local port

    :param struct fc_lport \*lport:
        The local port whose WWNN is to be set

    :param u64 wwnn:
        The new WWNN

.. _`fc_set_wwpn`:

fc_set_wwpn
===========

.. c:function:: void fc_set_wwpn(struct fc_lport *lport, u64 wwnn)

    Set the World Wide Port Name of a local port

    :param struct fc_lport \*lport:
        The local port whose WWPN is to be set

    :param u64 wwnn:
        The new WWPN

.. _`fc_lport_state_enter`:

fc_lport_state_enter
====================

.. c:function:: void fc_lport_state_enter(struct fc_lport *lport, enum fc_lport_state state)

    Change a local port's state

    :param struct fc_lport \*lport:
        The local port whose state is to change

    :param enum fc_lport_state state:
        The new state

.. _`fc_lport_init_stats`:

fc_lport_init_stats
===================

.. c:function:: int fc_lport_init_stats(struct fc_lport *lport)

    Allocate per-CPU statistics for a local port

    :param struct fc_lport \*lport:
        The local port whose statistics are to be initialized

.. _`fc_lport_free_stats`:

fc_lport_free_stats
===================

.. c:function:: void fc_lport_free_stats(struct fc_lport *lport)

    Free memory for a local port's statistics

    :param struct fc_lport \*lport:
        The local port whose statistics are to be freed

.. _`lport_priv`:

lport_priv
==========

.. c:function:: void *lport_priv(const struct fc_lport *lport)

    Return the private data from a local port

    :param const struct fc_lport \*lport:
        The local port whose private data is to be retreived

.. _`libfc_host_alloc`:

libfc_host_alloc
================

.. c:function:: struct fc_lport *libfc_host_alloc(struct scsi_host_template *sht, int priv_size)

    Allocate a Scsi_Host with room for a local port and LLD private data

    :param struct scsi_host_template \*sht:
        The SCSI host template

    :param int priv_size:
        Size of private data

.. _`libfc_host_alloc.return`:

Return
------

libfc lport

.. This file was automatic generated / don't edit.

