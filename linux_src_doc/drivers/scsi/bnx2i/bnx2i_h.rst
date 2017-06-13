.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2i/bnx2i.h

.. _`generic_pdu_resc`:

struct generic_pdu_resc
=======================

.. c:type:: struct generic_pdu_resc

    login pdu resource structure

.. _`generic_pdu_resc.definition`:

Definition
----------

.. code-block:: c

    struct generic_pdu_resc {
        char *req_buf;
        dma_addr_t req_dma_addr;
        u32 req_buf_size;
        char *req_wr_ptr;
        struct iscsi_hdr resp_hdr;
        char *resp_buf;
        dma_addr_t resp_dma_addr;
        u32 resp_buf_size;
        char *resp_wr_ptr;
        char *req_bd_tbl;
        dma_addr_t req_bd_dma;
        char *resp_bd_tbl;
        dma_addr_t resp_bd_dma;
    }

.. _`generic_pdu_resc.members`:

Members
-------

req_buf
    driver buffer used to stage payload associated with
    the login request

req_dma_addr
    dma address for iscsi login request payload buffer

req_buf_size
    actual login request payload length

req_wr_ptr
    pointer into login request buffer when next data is
    to be written

resp_hdr
    iscsi header where iscsi login response header is to
    be recreated

resp_buf
    buffer to stage login response payload

resp_dma_addr
    login response payload buffer dma address

resp_buf_size
    login response paylod length

resp_wr_ptr
    pointer into login response buffer when next data is
    to be written

req_bd_tbl
    iscsi login request payload BD table

req_bd_dma
    login request BD table dma address

resp_bd_tbl
    iscsi login response payload BD table

resp_bd_dma
    login request BD table dma address

.. _`generic_pdu_resc.description`:

Description
-----------

following structure defines buffer info for generic pdus such as iSCSI Login,
Logout and NOP

.. _`bd_resc_page`:

struct bd_resc_page
===================

.. c:type:: struct bd_resc_page

    tracks DMA'able memory allocated for BD tables

.. _`bd_resc_page.definition`:

Definition
----------

.. code-block:: c

    struct bd_resc_page {
        struct list_head link;
        u32 max_ptrs;
        u32 num_valid;
        void  *page;
    }

.. _`bd_resc_page.members`:

Members
-------

link
    list head to link elements

max_ptrs
    maximun pointers that can be stored in this page

num_valid
    number of pointer valid in this page

page
    base addess for page pointer array

.. _`bd_resc_page.description`:

Description
-----------

structure to track DMA'able memory allocated for command BD tables

.. _`io_bdt`:

struct io_bdt
=============

.. c:type:: struct io_bdt

    I/O buffer destricptor table

.. _`io_bdt.definition`:

Definition
----------

.. code-block:: c

    struct io_bdt {
        struct iscsi_bd *bd_tbl;
        dma_addr_t bd_tbl_dma;
        u16 bd_valid;
    }

.. _`io_bdt.members`:

Members
-------

bd_tbl
    BD table's virtual address

bd_tbl_dma
    BD table's dma address

bd_valid
    num valid BD entries

.. _`io_bdt.description`:

Description
-----------

IO BD table

.. _`bnx2i_conn`:

struct bnx2i_conn
=================

.. c:type:: struct bnx2i_conn

    iscsi connection structure

.. _`bnx2i_conn.definition`:

Definition
----------

.. code-block:: c

    struct bnx2i_conn {
        struct iscsi_cls_conn *cls_conn;
        struct bnx2i_hba *hba;
        struct completion cmd_cleanup_cmpl;
        u32 iscsi_conn_cid;
    #define BNX2I_CID_RESERVED 0x5AFF
        u32 fw_cid;
        struct timer_list poll_timer;
        struct bnx2i_endpoint *ep;
        struct generic_pdu_resc gen_pdu;
        u64 violation_notified;
        atomic_t work_cnt;
    }

.. _`bnx2i_conn.members`:

Members
-------

cls_conn
    pointer to iscsi cls conn

hba
    adapter structure pointer

cmd_cleanup_cmpl
    *undescribed*

iscsi_conn_cid
    iscsi conn id

fw_cid
    firmware iscsi context id

poll_timer
    *undescribed*

ep
    endpoint structure pointer

gen_pdu
    login/nopout/logout pdu resources

violation_notified
    bit mask used to track iscsi error/warning messages
    already printed out

work_cnt
    keeps track of the number of outstanding work

.. _`bnx2i_conn.description`:

Description
-----------

iSCSI connection structure

.. _`iscsi_cid_queue`:

struct iscsi_cid_queue
======================

.. c:type:: struct iscsi_cid_queue

    Per adapter iscsi cid queue

.. _`iscsi_cid_queue.definition`:

Definition
----------

.. code-block:: c

    struct iscsi_cid_queue {
        void *cid_que_base;
        u32 *cid_que;
        u32 cid_q_prod_idx;
        u32 cid_q_cons_idx;
        u32 cid_q_max_idx;
        u32 cid_free_cnt;
        struct bnx2i_conn **conn_cid_tbl;
    }

.. _`iscsi_cid_queue.members`:

Members
-------

cid_que_base
    queue base memory

cid_que
    queue memory pointer

cid_q_prod_idx
    produce index

cid_q_cons_idx
    consumer index

cid_q_max_idx
    max index. used to detect wrap around condition

cid_free_cnt
    queue size

conn_cid_tbl
    iscsi cid to conn structure mapping table

.. _`iscsi_cid_queue.description`:

Description
-----------

Per adapter iSCSI CID Queue

.. _`bnx2i_hba`:

struct bnx2i_hba
================

.. c:type:: struct bnx2i_hba

    bnx2i adapter structure

.. _`bnx2i_hba.definition`:

Definition
----------

.. code-block:: c

    struct bnx2i_hba {
        struct list_head link;
        struct cnic_dev *cnic;
        struct pci_dev *pcidev;
        struct net_device *netdev;
        void __iomem *regview;
        resource_size_t reg_base;
        u32 age;
        unsigned long cnic_dev_type;
    #define BNX2I_NX2_DEV_5706 0x0
    #define BNX2I_NX2_DEV_5708 0x1
    #define BNX2I_NX2_DEV_5709 0x2
    #define BNX2I_NX2_DEV_57710 0x3
        u32 mail_queue_access;
    #define BNX2I_MQ_KERNEL_MODE 0x0
    #define BNX2I_MQ_KERNEL_BYPASS_MODE 0x1
    #define BNX2I_MQ_BIN_MODE 0x2
        unsigned long reg_with_cnic;
    #define BNX2I_CNIC_REGISTERED 1
        unsigned long adapter_state;
    #define ADAPTER_STATE_UP 0
    #define ADAPTER_STATE_GOING_DOWN 1
    #define ADAPTER_STATE_LINK_DOWN 2
    #define ADAPTER_STATE_INIT_FAILED 31
        unsigned int mtu_supported;
    #define BNX2I_MAX_MTU_SUPPORTED 9000
        struct Scsi_Host *shost;
        u32 max_sqes;
        u32 max_rqes;
        u32 max_cqes;
        u32 num_ccell;
        int ofld_conns_active;
        wait_queue_head_t eh_wait;
        int max_active_conns;
        struct iscsi_cid_queue cid_que;
        rwlock_t ep_rdwr_lock;
        struct list_head ep_ofld_list;
        struct list_head ep_active_list;
        struct list_head ep_destroy_list;
        char *mp_bd_tbl;
        dma_addr_t mp_bd_dma;
        char *dummy_buffer;
        dma_addr_t dummy_buf_dma;
        spinlock_t lock;
        struct mutex net_dev_lock;
        int hba_shutdown_tmo;
        int conn_teardown_tmo;
        int conn_ctx_destroy_tmo;
        u16 pci_did;
        u16 pci_vid;
        u16 pci_sdid;
        u16 pci_svid;
        u16 pci_func;
        u16 pci_devno;
        u32 num_wqe_sent;
        u32 num_cqe_rcvd;
        u32 num_intr_claimed;
        u32 link_changed_count;
        u32 ipaddr_changed_count;
        u32 num_sess_opened;
        u32 num_conn_opened;
        unsigned int ctx_ccell_tasks;
    #ifdef CONFIG_32BIT
        spinlock_t stat_lock;
    #endif
        struct bnx2i_stats_info bnx2i_stats;
        struct iscsi_stats_info stats;
    }

.. _`bnx2i_hba.members`:

Members
-------

link
    list head to link elements

cnic
    pointer to cnic device

pcidev
    pointer to pci dev

netdev
    pointer to netdev structure

regview
    mapped PCI register space

reg_base
    *undescribed*

age
    age, incremented by every recovery

cnic_dev_type
    cnic device type, 5706/5708/5709/57710

mail_queue_access
    mailbox queue access mode, applicable to 5709 only

reg_with_cnic
    indicates whether the device is register with CNIC

adapter_state
    adapter state, UP, GOING_DOWN, LINK_DOWN

mtu_supported
    Ethernet MTU supported

shost
    scsi host pointer

max_sqes
    SQ size

max_rqes
    RQ size

max_cqes
    CQ size

num_ccell
    number of command cells per connection

ofld_conns_active
    active connection list

eh_wait
    wait queue for the endpoint to shutdown

max_active_conns
    max offload connections supported by this device

cid_que
    iscsi cid queue

ep_rdwr_lock
    read / write lock to synchronize various ep lists

ep_ofld_list
    connection list for pending offload completion

ep_active_list
    connection list for active offload endpoints

ep_destroy_list
    connection list for pending offload completion

mp_bd_tbl
    BD table to be used with middle path requests

mp_bd_dma
    DMA address of 'mp_bd_tbl' memory buffer

dummy_buffer
    Dummy buffer to be used with zero length scsicmd reqs

dummy_buf_dma
    DMA address of 'dummy_buffer' memory buffer

lock
    lock to synchonize access to hba structure

net_dev_lock
    *undescribed*

hba_shutdown_tmo
    Timeout value to shutdown each connection

conn_teardown_tmo
    Timeout value to tear down each connection

conn_ctx_destroy_tmo
    Timeout value to destroy context of each connection

pci_did
    PCI device ID

pci_vid
    PCI vendor ID

pci_sdid
    PCI subsystem device ID

pci_svid
    PCI subsystem vendor ID

pci_func
    PCI function number in system pci tree

pci_devno
    PCI device number in system pci tree

num_wqe_sent
    statistic counter, total wqe's sent

num_cqe_rcvd
    statistic counter, total cqe's received

num_intr_claimed
    statistic counter, total interrupts claimed

link_changed_count
    statistic counter, num of link change notifications
    received

ipaddr_changed_count
    statistic counter, num times IP address changed while
    at least one connection is offloaded

num_sess_opened
    statistic counter, total num sessions opened

num_conn_opened
    statistic counter, total num conns opened on this hba

ctx_ccell_tasks
    captures number of ccells and tasks supported by
    currently offloaded connection, used to decode
    context memory

stat_lock
    spin lock used by the statistic collector (32 bit)

bnx2i_stats
    *undescribed*

stats
    local iSCSI statistic collection place holder

.. _`bnx2i_hba.description`:

Description
-----------

Adapter Data Structure

.. _`qp_info`:

struct qp_info
==============

.. c:type:: struct qp_info

    QP (share queue region) atrributes structure

.. _`qp_info.definition`:

Definition
----------

.. code-block:: c

    struct qp_info {
        void __iomem *ctx_base;
    #define DPM_TRIGER_TYPE 0x40
    #define BNX2I_570x_QUE_DB_SIZE 0
    #define BNX2I_5771x_QUE_DB_SIZE 16
        struct sqe *sq_virt;
        dma_addr_t sq_phys;
        u32 sq_mem_size;
        struct sqe *sq_prod_qe;
        struct sqe *sq_cons_qe;
        struct sqe *sq_first_qe;
        struct sqe *sq_last_qe;
        u16 sq_prod_idx;
        u16 sq_cons_idx;
        u32 sqe_left;
        void *sq_pgtbl_virt;
        dma_addr_t sq_pgtbl_phys;
        u32 sq_pgtbl_size;
        struct cqe *cq_virt;
        dma_addr_t cq_phys;
        u32 cq_mem_size;
        struct cqe *cq_prod_qe;
        struct cqe *cq_cons_qe;
        struct cqe *cq_first_qe;
        struct cqe *cq_last_qe;
        u16 cq_prod_idx;
        u16 cq_cons_idx;
        u32 cqe_left;
        u32 cqe_size;
        u32 cqe_exp_seq_sn;
        void *cq_pgtbl_virt;
        dma_addr_t cq_pgtbl_phys;
        u32 cq_pgtbl_size;
        struct rqe *rq_virt;
        dma_addr_t rq_phys;
        u32 rq_mem_size;
        struct rqe *rq_prod_qe;
        struct rqe *rq_cons_qe;
        struct rqe *rq_first_qe;
        struct rqe *rq_last_qe;
        u16 rq_prod_idx;
        u16 rq_cons_idx;
        u32 rqe_left;
        void *rq_pgtbl_virt;
        dma_addr_t rq_pgtbl_phys;
        u32 rq_pgtbl_size;
    }

.. _`qp_info.members`:

Members
-------

ctx_base
    ioremapped pci register base to access doorbell register
    pertaining to this offloaded connection

sq_virt
    virtual address of send queue (SQ) region

sq_phys
    DMA address of SQ memory region

sq_mem_size
    SQ size

sq_prod_qe
    SQ producer entry pointer

sq_cons_qe
    SQ consumer entry pointer

sq_first_qe
    virtual address of first entry in SQ

sq_last_qe
    virtual address of last entry in SQ

sq_prod_idx
    SQ producer index

sq_cons_idx
    SQ consumer index

sqe_left
    number sq entry left

sq_pgtbl_virt
    page table describing buffer consituting SQ region

sq_pgtbl_phys
    dma address of 'sq_pgtbl_virt'

sq_pgtbl_size
    SQ page table size

cq_virt
    virtual address of completion queue (CQ) region

cq_phys
    DMA address of RQ memory region

cq_mem_size
    CQ size

cq_prod_qe
    CQ producer entry pointer

cq_cons_qe
    CQ consumer entry pointer

cq_first_qe
    virtual address of first entry in CQ

cq_last_qe
    virtual address of last entry in CQ

cq_prod_idx
    CQ producer index

cq_cons_idx
    CQ consumer index

cqe_left
    number cq entry left

cqe_size
    size of each CQ entry

cqe_exp_seq_sn
    next expected CQE sequence number

cq_pgtbl_virt
    page table describing buffer consituting CQ region

cq_pgtbl_phys
    dma address of 'cq_pgtbl_virt'

cq_pgtbl_size
    CQ page table size

rq_virt
    virtual address of receive queue (RQ) region

rq_phys
    DMA address of RQ memory region

rq_mem_size
    RQ size

rq_prod_qe
    RQ producer entry pointer

rq_cons_qe
    RQ consumer entry pointer

rq_first_qe
    virtual address of first entry in RQ

rq_last_qe
    virtual address of last entry in RQ

rq_prod_idx
    RQ producer index

rq_cons_idx
    RQ consumer index

rqe_left
    number rq entry left

rq_pgtbl_virt
    page table describing buffer consituting RQ region

rq_pgtbl_phys
    dma address of 'rq_pgtbl_virt'

rq_pgtbl_size
    RQ page table size

.. _`qp_info.description`:

Description
-----------

queue pair (QP) is a per connection shared data structure which is used
to send work requests (SQ), receive completion notifications (CQ)
and receive asynchoronous / scsi sense info (RQ). 'qp_info' structure
below holds queue memory, consumer/producer indexes and page table
information

.. _`bnx2i_endpoint`:

struct bnx2i_endpoint
=====================

.. c:type:: struct bnx2i_endpoint

    representation of tcp connection in NX2 world

.. _`bnx2i_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct bnx2i_endpoint {
        struct list_head link;
        struct bnx2i_hba *hba;
        struct bnx2i_conn *conn;
        struct iscsi_endpoint *cls_ep;
        struct cnic_sock *cm_sk;
        u32 hba_age;
        u32 state;
        unsigned long timestamp;
        atomic_t num_active_cmds;
        u32 ec_shift;
        struct qp_info qp;
        struct ep_handles ids;
    #define ep_iscsi_cid ids.drv_iscsi_cid
    #define ep_cid ids.fw_cid
    #define ep_pg_cid ids.pg_cid
        struct timer_list ofld_timer;
        wait_queue_head_t ofld_wait;
    }

.. _`bnx2i_endpoint.members`:

Members
-------

link
    list head to link elements

hba
    adapter to which this connection belongs

conn
    iscsi connection this EP is linked to

cls_ep
    associated iSCSI endpoint pointer

cm_sk
    cnic sock struct

hba_age
    age to detect if 'iscsid' issues \ :c:func:`ep_disconnect`\ 
    after HBA reset is completed by bnx2i/cnic/bnx2
    modules

state
    tracks offload connection state machine

timestamp
    tracks the start time when the ep begins to connect

num_active_cmds
    tracks the number of outstanding commands for this ep

ec_shift
    the amount of shift as part of the event coal calc

qp
    QP information

ids
    contains chip allocated \*context id\* & driver assigned
    \*iscsi cid\*

ofld_timer
    offload timer to detect timeout

ofld_wait
    wait queue

.. _`bnx2i_endpoint.description`:

Description
-----------

Endpoint Structure - equivalent of tcp socket structure

.. This file was automatic generated / don't edit.

