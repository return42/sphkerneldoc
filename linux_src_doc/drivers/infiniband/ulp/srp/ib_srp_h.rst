.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/srp/ib_srp.h

.. _`srp_rdma_ch`:

struct srp_rdma_ch
==================

.. c:type:: struct srp_rdma_ch


.. _`srp_rdma_ch.definition`:

Definition
----------

.. code-block:: c

    struct srp_rdma_ch {
        struct list_head free_tx;
        spinlock_t lock;
        s32 req_lim;
        struct srp_target_port *target ____cacheline_aligned_in_smp;
        struct ib_cq *send_cq;
        struct ib_cq *recv_cq;
        struct ib_qp *qp;
        union {
            struct ib_fmr_pool *fmr_pool;
            struct srp_fr_pool *fr_pool;
        } ;
        struct completion done;
        int status;
        union {
            struct ib_cm {
                struct sa_path_rec path;
                struct ib_sa_query *path_query;
                int path_query_id;
                struct ib_cm_id *cm_id;
            } ib_cm;
            struct rdma_cm {
                struct rdma_cm_id *cm_id;
            } rdma_cm;
        } ;
        struct srp_iu **tx_ring;
        struct srp_iu **rx_ring;
        struct srp_request *req_ring;
        int max_ti_iu_len;
        int comp_vector;
        u64 tsk_mgmt_tag;
        struct completion tsk_mgmt_done;
        u8 tsk_mgmt_status;
        bool connected;
    }

.. _`srp_rdma_ch.members`:

Members
-------

free_tx
    *undescribed*

lock
    *undescribed*

req_lim
    *undescribed*

____cacheline_aligned_in_smp
    *undescribed*

send_cq
    *undescribed*

recv_cq
    *undescribed*

qp
    *undescribed*

{unnamed_union}
    anonymous

fmr_pool
    *undescribed*

fr_pool
    *undescribed*

done
    *undescribed*

status
    *undescribed*

{unnamed_union}
    anonymous

ib_cm
    *undescribed*

rdma_cm
    *undescribed*

tx_ring
    *undescribed*

rx_ring
    *undescribed*

req_ring
    *undescribed*

max_ti_iu_len
    *undescribed*

comp_vector
    Completion vector used by this RDMA channel.

tsk_mgmt_tag
    *undescribed*

tsk_mgmt_done
    *undescribed*

tsk_mgmt_status
    *undescribed*

connected
    *undescribed*

.. _`srp_target_port`:

struct srp_target_port
======================

.. c:type:: struct srp_target_port


.. _`srp_target_port.definition`:

Definition
----------

.. code-block:: c

    struct srp_target_port {
        spinlock_t lock;
        u32 global_rkey;
        struct srp_rdma_ch *ch;
        struct net *net;
        u32 ch_count;
        u32 lkey;
        enum srp_target_state state;
        unsigned int max_iu_len;
        unsigned int cmd_sg_cnt;
        unsigned int indirect_size;
        bool allow_ext_sg;
        union ib_gid sgid;
        __be64 id_ext;
        __be64 ioc_guid;
        __be64 initiator_ext;
        u16 io_class;
        struct srp_host *srp_host;
        struct Scsi_Host *scsi_host;
        struct srp_rport *rport;
        char target_name[32];
        unsigned int scsi_id;
        unsigned int sg_tablesize;
        unsigned int target_can_queue;
        int mr_pool_size;
        int mr_per_cmd;
        int queue_size;
        int req_ring_size;
        int comp_vector;
        int tl_retry_count;
        bool using_rdma_cm;
        union {
            struct {
                __be64 service_id;
                union ib_gid orig_dgid;
                __be16 pkey;
            } ib_cm;
            struct {
                union {
                    struct sockaddr_in ip4;
                    struct sockaddr_in6 ip6;
                    struct sockaddr_storage ss;
                } src;
                union {
                    struct sockaddr_in ip4;
                    struct sockaddr_in6 ip6;
                    struct sockaddr_storage ss;
                } dst;
                bool src_specified;
            } rdma_cm;
        } ;
        u32 rq_tmo_jiffies;
        int zero_req_lim;
        struct work_struct tl_err_work;
        struct work_struct remove_work;
        struct list_head list;
        bool qp_in_error;
    }

.. _`srp_target_port.members`:

Members
-------

lock
    *undescribed*

global_rkey
    *undescribed*

ch
    *undescribed*

net
    *undescribed*

ch_count
    *undescribed*

lkey
    *undescribed*

state
    *undescribed*

max_iu_len
    *undescribed*

cmd_sg_cnt
    *undescribed*

indirect_size
    *undescribed*

allow_ext_sg
    *undescribed*

sgid
    *undescribed*

id_ext
    *undescribed*

ioc_guid
    *undescribed*

initiator_ext
    *undescribed*

io_class
    *undescribed*

srp_host
    *undescribed*

scsi_host
    *undescribed*

rport
    *undescribed*

target_name
    *undescribed*

scsi_id
    *undescribed*

sg_tablesize
    *undescribed*

target_can_queue
    *undescribed*

mr_pool_size
    *undescribed*

mr_per_cmd
    *undescribed*

queue_size
    *undescribed*

req_ring_size
    *undescribed*

comp_vector
    Completion vector used by the first RDMA channel created for
    this target port.

tl_retry_count
    *undescribed*

using_rdma_cm
    *undescribed*

{unnamed_union}
    anonymous

ib_cm
    *undescribed*

rdma_cm
    *undescribed*

rq_tmo_jiffies
    *undescribed*

zero_req_lim
    *undescribed*

tl_err_work
    *undescribed*

remove_work
    *undescribed*

list
    *undescribed*

qp_in_error
    *undescribed*

.. _`srp_fr_desc`:

struct srp_fr_desc
==================

.. c:type:: struct srp_fr_desc

    fast registration work request arguments

.. _`srp_fr_desc.definition`:

Definition
----------

.. code-block:: c

    struct srp_fr_desc {
        struct list_head entry;
        struct ib_mr *mr;
    }

.. _`srp_fr_desc.members`:

Members
-------

entry
    Entry in srp_fr_pool.free_list.

mr
    Memory region.

.. _`srp_fr_pool`:

struct srp_fr_pool
==================

.. c:type:: struct srp_fr_pool

    pool of fast registration descriptors

.. _`srp_fr_pool.definition`:

Definition
----------

.. code-block:: c

    struct srp_fr_pool {
        int size;
        int max_page_list_len;
        spinlock_t lock;
        struct list_head free_list;
        struct srp_fr_desc desc[0];
    }

.. _`srp_fr_pool.members`:

Members
-------

size
    Number of descriptors in this pool.

max_page_list_len
    Maximum fast registration work request page list length.

lock
    Protects free_list.

free_list
    List of free descriptors.

desc
    Fast registration descriptor pool.

.. _`srp_fr_pool.description`:

Description
-----------

An entry is available for allocation if and only if it occurs in \ ``free_list``\ .

.. _`srp_map_state`:

struct srp_map_state
====================

.. c:type:: struct srp_map_state

    per-request DMA memory mapping state

.. _`srp_map_state.definition`:

Definition
----------

.. code-block:: c

    struct srp_map_state {
        union {
            struct {
                struct ib_pool_fmr **next;
                struct ib_pool_fmr **end;
            } fmr;
            struct {
                struct srp_fr_desc **next;
                struct srp_fr_desc **end;
            } fr;
            struct {
                void **next;
                void **end;
            } gen;
        } ;
        struct srp_direct_buf *desc;
        union {
            u64 *pages;
            struct scatterlist *sg;
        } ;
        dma_addr_t base_dma_addr;
        u32 dma_len;
        u32 total_len;
        unsigned int npages;
        unsigned int nmdesc;
        unsigned int ndesc;
    }

.. _`srp_map_state.members`:

Members
-------

{unnamed_union}
    anonymous

fmr
    *undescribed*

fr
    *undescribed*

gen
    *undescribed*

desc
    Pointer to the element of the SRP buffer descriptor array
    that is being filled in.

{unnamed_union}
    anonymous

pages
    Array with DMA addresses of pages being considered for
    memory registration.

sg
    *undescribed*

base_dma_addr
    DMA address of the first page that has not yet been mapped.

dma_len
    Number of bytes that will be registered with the next
    FMR or FR memory registration call.

total_len
    Total number of bytes in the sg-list being mapped.

npages
    Number of page addresses in the pages[] array.

nmdesc
    Number of FMR or FR memory descriptors used for mapping.

ndesc
    Number of SRP buffer descriptors that have been filled in.

.. This file was automatic generated / don't edit.

