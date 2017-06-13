.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/iser/iscsi_iser.h

.. _`iser_data_buf`:

struct iser_data_buf
====================

.. c:type:: struct iser_data_buf

    iSER data buffer

.. _`iser_data_buf.definition`:

Definition
----------

.. code-block:: c

    struct iser_data_buf {
        struct scatterlist *sg;
        int size;
        unsigned long data_len;
        unsigned int dma_nents;
    }

.. _`iser_data_buf.members`:

Members
-------

sg
    pointer to the sg list

size
    num entries of this sg

data_len
    total beffer byte len

dma_nents
    returned by dma_map_sg

.. _`iser_mem_reg`:

struct iser_mem_reg
===================

.. c:type:: struct iser_mem_reg

    iSER memory registration info

.. _`iser_mem_reg.definition`:

Definition
----------

.. code-block:: c

    struct iser_mem_reg {
        struct ib_sge sge;
        u32 rkey;
        void *mem_h;
    }

.. _`iser_mem_reg.members`:

Members
-------

sge
    memory region sg element

rkey
    memory region remote key

mem_h
    pointer to registration context (FMR/Fastreg)

.. _`iser_tx_desc`:

struct iser_tx_desc
===================

.. c:type:: struct iser_tx_desc

    iSER TX descriptor

.. _`iser_tx_desc.definition`:

Definition
----------

.. code-block:: c

    struct iser_tx_desc {
        struct iser_ctrl iser_header;
        struct iscsi_hdr iscsi_header;
        enum iser_desc_type type;
        u64 dma_addr;
        struct ib_sge tx_sg[2];
        int num_sge;
        struct ib_cqe cqe;
        bool mapped;
        u8 wr_idx;
        union iser_wr wrs[ISER_MAX_WRS];
        struct iser_mem_reg data_reg;
        struct iser_mem_reg prot_reg;
        struct ib_sig_attrs sig_attrs;
    }

.. _`iser_tx_desc.members`:

Members
-------

iser_header
    iser header

iscsi_header
    iscsi header

type
    command/control/dataout

dma_addr
    *undescribed*

tx_sg
    sg[0] points to iser/iscsi headers
    sg[1] optionally points to either of immediate data
    unsolicited data-out or control

num_sge
    number sges used on this TX task

cqe
    *undescribed*

mapped
    Is the task header mapped

wr_idx
    Current WR index

wrs
    Array of WRs per task

data_reg
    Data buffer registration details

prot_reg
    Protection buffer registration details

sig_attrs
    Signature attributes

.. _`iser_rx_desc`:

struct iser_rx_desc
===================

.. c:type:: struct iser_rx_desc

    iSER RX descriptor

.. _`iser_rx_desc.definition`:

Definition
----------

.. code-block:: c

    struct iser_rx_desc {
        struct iser_ctrl iser_header;
        struct iscsi_hdr iscsi_header;
        char data[ISER_RECV_DATA_SEG_LEN];
        u64 dma_addr;
        struct ib_sge rx_sg;
        struct ib_cqe cqe;
        char pad[ISER_RX_PAD_SIZE];
    }

.. _`iser_rx_desc.members`:

Members
-------

iser_header
    iser header

iscsi_header
    iscsi header

data
    received data segment

dma_addr
    receive buffer dma address

rx_sg
    ib_sge of receive buffer

cqe
    *undescribed*

pad
    for sense data TODO: Modify to maximum sense length supported

.. _`iser_login_desc`:

struct iser_login_desc
======================

.. c:type:: struct iser_login_desc

    iSER login descriptor

.. _`iser_login_desc.definition`:

Definition
----------

.. code-block:: c

    struct iser_login_desc {
        void *req;
        void *rsp;
        u64 req_dma;
        u64 rsp_dma;
        struct ib_sge sge;
        struct ib_cqe cqe;
    }

.. _`iser_login_desc.members`:

Members
-------

req
    pointer to login request buffer

rsp
    *undescribed*

req_dma
    DMA address of login request buffer

rsp_dma
    DMA address of login response buffer

sge
    IB sge for login post recv

cqe
    completion handler

.. _`iser_comp`:

struct iser_comp
================

.. c:type:: struct iser_comp

    iSER completion context

.. _`iser_comp.definition`:

Definition
----------

.. code-block:: c

    struct iser_comp {
        struct ib_cq *cq;
        int active_qps;
    }

.. _`iser_comp.members`:

Members
-------

cq
    completion queue

active_qps
    Number of active QPs attached
    to completion context

.. _`iser_reg_ops`:

struct iser_reg_ops
===================

.. c:type:: struct iser_reg_ops

    Memory registration operations per-device registration schemes

.. _`iser_reg_ops.definition`:

Definition
----------

.. code-block:: c

    struct iser_reg_ops {
        int (*alloc_reg_res)(struct ib_conn *ib_conn,unsigned cmds_max,unsigned int size);
        void (*free_reg_res)(struct ib_conn *ib_conn);
        int (*reg_mem)(struct iscsi_iser_task *iser_task,struct iser_data_buf *mem,struct iser_reg_resources *rsc,struct iser_mem_reg *reg);
        void (*unreg_mem)(struct iscsi_iser_task *iser_task,enum iser_data_dir cmd_dir);
        struct iser_fr_desc * (*reg_desc_get)(struct ib_conn *ib_conn);
        void (*reg_desc_put)(struct ib_conn *ib_conn,struct iser_fr_desc *desc);
    }

.. _`iser_reg_ops.members`:

Members
-------

alloc_reg_res
    Allocate registration resources

free_reg_res
    Free registration resources

reg_mem
    *undescribed*

unreg_mem
    Un-register memory buffers

reg_desc_get
    Get a registration descriptor for pool

reg_desc_put
    Get a registration descriptor to pool

.. _`iser_device`:

struct iser_device
==================

.. c:type:: struct iser_device

    iSER device handle

.. _`iser_device.definition`:

Definition
----------

.. code-block:: c

    struct iser_device {
        struct ib_device *ib_device;
        struct ib_pd *pd;
        struct ib_event_handler event_handler;
        struct list_head ig_list;
        int refcount;
        int comps_used;
        struct iser_comp *comps;
        const struct iser_reg_ops *reg_ops;
        bool remote_inv_sup;
    }

.. _`iser_device.members`:

Members
-------

ib_device
    RDMA device

pd
    Protection Domain for this device

event_handler
    IB events handle routine

ig_list
    entry in devices list

refcount
    Reference counter, dominated by open iser connections

comps_used
    Number of completion contexts used, Min between online
    cpus and device max completion vectors

comps
    Dinamically allocated array of completion handlers

reg_ops
    Registration ops

remote_inv_sup
    Remote invalidate is supported on this device

.. _`iser_reg_resources`:

struct iser_reg_resources
=========================

.. c:type:: struct iser_reg_resources

    Fast registration recources

.. _`iser_reg_resources.definition`:

Definition
----------

.. code-block:: c

    struct iser_reg_resources {
        union {unnamed_union};
        struct iser_page_vec *page_vec;
        u8 mr_valid:1;
    }

.. _`iser_reg_resources.members`:

Members
-------

{unnamed_union}
    anonymous


page_vec
    fast reg page list used by fmr pool

mr_valid
    is mr valid indicator

.. _`iser_pi_context`:

struct iser_pi_context
======================

.. c:type:: struct iser_pi_context

    Protection information context

.. _`iser_pi_context.definition`:

Definition
----------

.. code-block:: c

    struct iser_pi_context {
        struct iser_reg_resources rsc;
        struct ib_mr *sig_mr;
        u8 sig_mr_valid:1;
        u8 sig_protected:1;
    }

.. _`iser_pi_context.members`:

Members
-------

rsc
    protection buffer registration resources

sig_mr
    signature enable memory region

sig_mr_valid
    is sig_mr valid indicator

sig_protected
    is region protected indicator

.. _`iser_fr_desc`:

struct iser_fr_desc
===================

.. c:type:: struct iser_fr_desc

    Fast registration descriptor

.. _`iser_fr_desc.definition`:

Definition
----------

.. code-block:: c

    struct iser_fr_desc {
        struct list_head list;
        struct iser_reg_resources rsc;
        struct iser_pi_context *pi_ctx;
        struct list_head all_list;
    }

.. _`iser_fr_desc.members`:

Members
-------

list
    entry in connection fastreg pool

rsc
    data buffer registration resources

pi_ctx
    protection information context

all_list
    *undescribed*

.. _`iser_fr_pool`:

struct iser_fr_pool
===================

.. c:type:: struct iser_fr_pool

    connection fast registration pool

.. _`iser_fr_pool.definition`:

Definition
----------

.. code-block:: c

    struct iser_fr_pool {
        struct list_head list;
        spinlock_t lock;
        int size;
        struct list_head all_list;
    }

.. _`iser_fr_pool.members`:

Members
-------

list
    list of fastreg descriptors

lock
    protects fmr/fastreg pool

size
    size of the pool

all_list
    *undescribed*

.. _`ib_conn`:

struct ib_conn
==============

.. c:type:: struct ib_conn

    Infiniband related objects

.. _`ib_conn.definition`:

Definition
----------

.. code-block:: c

    struct ib_conn {
        struct rdma_cm_id *cma_id;
        struct ib_qp *qp;
        int post_recv_buf_count;
        u8 sig_count;
        struct ib_recv_wr rx_wr[ISER_MIN_POSTED_RX];
        struct iser_device *device;
        struct iser_comp *comp;
        struct iser_fr_pool fr_pool;
        bool pi_support;
        struct ib_cqe reg_cqe;
    }

.. _`ib_conn.members`:

Members
-------

cma_id
    rdma_cm connection maneger handle

qp
    Connection Queue-pair

post_recv_buf_count
    post receive counter

sig_count
    send work request signal count

rx_wr
    receive work request for batch posts

device
    reference to iser device

comp
    iser completion context

fr_pool
    connection fast registration poool

pi_support
    Indicate device T10-PI support

reg_cqe
    *undescribed*

.. _`iser_conn`:

struct iser_conn
================

.. c:type:: struct iser_conn

    iSER connection context

.. _`iser_conn.definition`:

Definition
----------

.. code-block:: c

    struct iser_conn {
        struct ib_conn ib_conn;
        struct iscsi_conn *iscsi_conn;
        struct iscsi_endpoint *ep;
        enum iser_conn_state state;
        unsigned qp_max_recv_dtos;
        unsigned qp_max_recv_dtos_mask;
        unsigned min_posted_rx;
        u16 max_cmds;
        char name[ISER_OBJECT_NAME_SIZE];
        struct work_struct release_work;
        struct mutex state_mutex;
        struct completion stop_completion;
        struct completion ib_completion;
        struct completion up_completion;
        struct list_head conn_list;
        struct iser_login_desc login_desc;
        unsigned int rx_desc_head;
        struct iser_rx_desc *rx_descs;
        u32 num_rx_descs;
        unsigned short scsi_sg_tablesize;
        bool snd_w_inv;
    }

.. _`iser_conn.members`:

Members
-------

ib_conn
    connection RDMA resources

iscsi_conn
    link to matching iscsi connection

ep
    transport handle

state
    connection logical state

qp_max_recv_dtos
    maximum number of data outs, corresponds
    to max number of post recvs

qp_max_recv_dtos_mask
    (qp_max_recv_dtos - 1)

min_posted_rx
    (qp_max_recv_dtos >> 2)

max_cmds
    maximum cmds allowed for this connection

name
    connection peer portal

release_work
    deffered work for release job

state_mutex
    protects iser onnection state

stop_completion
    conn_stop completion

ib_completion
    RDMA cleanup completion

up_completion
    connection establishment completed
    (state is ISER_CONN_UP)

conn_list
    entry in ig conn list

login_desc
    login descriptor

rx_desc_head
    head of rx_descs cyclic buffer

rx_descs
    rx buffers array (cyclic buffer)

num_rx_descs
    number of rx descriptors

scsi_sg_tablesize
    scsi host sg_tablesize

snd_w_inv
    *undescribed*

.. _`iscsi_iser_task`:

struct iscsi_iser_task
======================

.. c:type:: struct iscsi_iser_task

    iser task context

.. _`iscsi_iser_task.definition`:

Definition
----------

.. code-block:: c

    struct iscsi_iser_task {
        struct iser_tx_desc desc;
        struct iser_conn *iser_conn;
        enum iser_task_status status;
        struct scsi_cmnd *sc;
        int command_sent;
        int dir[ISER_DIRS_NUM];
        struct iser_mem_reg rdma_reg[ISER_DIRS_NUM];
        struct iser_data_buf data[ISER_DIRS_NUM];
        struct iser_data_buf prot[ISER_DIRS_NUM];
    }

.. _`iscsi_iser_task.members`:

Members
-------

desc
    TX descriptor

iser_conn
    link to iser connection

status
    current task status

sc
    link to scsi command

command_sent
    indicate if command was sent

dir
    iser data direction

rdma_reg
    task rdma registration desc

data
    iser data buffer desc

prot
    iser protection buffer desc

.. _`iser_global`:

struct iser_global
==================

.. c:type:: struct iser_global

    iSER global context

.. _`iser_global.definition`:

Definition
----------

.. code-block:: c

    struct iser_global {
        struct mutex device_list_mutex;
        struct list_head device_list;
        struct mutex connlist_mutex;
        struct list_head connlist;
        struct kmem_cache *desc_cache;
    }

.. _`iser_global.members`:

Members
-------

device_list_mutex
    protects device_list

device_list
    iser devices global list

connlist_mutex
    protects connlist

connlist
    iser connections global list

desc_cache
    kmem cache for tx dataout

.. This file was automatic generated / don't edit.

