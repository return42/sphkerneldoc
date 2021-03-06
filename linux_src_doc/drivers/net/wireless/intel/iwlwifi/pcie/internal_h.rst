.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/pcie/internal.h

.. _`iwl_rx_mem_buffer`:

struct iwl_rx_mem_buffer
========================

.. c:type:: struct iwl_rx_mem_buffer


.. _`iwl_rx_mem_buffer.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_mem_buffer {
        dma_addr_t page_dma;
        struct page *page;
        u16 vid;
        bool invalid;
        struct list_head list;
        u32 size;
    }

.. _`iwl_rx_mem_buffer.members`:

Members
-------

page_dma
    bus address of rxb page

page
    driver's pointer to the rxb page

vid
    index of this rxb in the global table

invalid
    rxb is in driver ownership - not owned by HW

list
    *undescribed*

size
    size used from the buffer

.. _`isr_statistics`:

struct isr_statistics
=====================

.. c:type:: struct isr_statistics

    interrupt statistics

.. _`isr_statistics.definition`:

Definition
----------

.. code-block:: c

    struct isr_statistics {
        u32 hw;
        u32 sw;
        u32 err_code;
        u32 sch;
        u32 alive;
        u32 rfkill;
        u32 ctkill;
        u32 wakeup;
        u32 rx;
        u32 tx;
        u32 unhandled;
    }

.. _`isr_statistics.members`:

Members
-------

hw
    *undescribed*

sw
    *undescribed*

err_code
    *undescribed*

sch
    *undescribed*

alive
    *undescribed*

rfkill
    *undescribed*

ctkill
    *undescribed*

wakeup
    *undescribed*

rx
    *undescribed*

tx
    *undescribed*

unhandled
    *undescribed*

.. _`iwl_rx_transfer_desc`:

struct iwl_rx_transfer_desc
===========================

.. c:type:: struct iwl_rx_transfer_desc

    transfer descriptor

.. _`iwl_rx_transfer_desc.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_transfer_desc {
        __le32 type_n_size;
        __le64 addr;
        __le16 rbid;
        __le16 reserved;
    }

.. _`iwl_rx_transfer_desc.members`:

Members
-------

type_n_size
    buffer type (bit 0: external buff valid,

addr
    ptr to free buffer start address

rbid
    unique tag of the buffer

reserved
    reserved

.. _`iwl_rx_transfer_desc.bit-1`:

bit 1
-----

optional footer valid, bit 2-7: reserved)
and buffer size

.. _`iwl_rx_completion_desc`:

struct iwl_rx_completion_desc
=============================

.. c:type:: struct iwl_rx_completion_desc

    completion descriptor

.. _`iwl_rx_completion_desc.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_completion_desc {
        u8 type;
        u8 status;
        __le16 reserved1;
        __le16 rbid;
        __le32 size;
        u8 reserved2[22];
    }

.. _`iwl_rx_completion_desc.members`:

Members
-------

type
    buffer type (bit 0: external buff valid,

status
    status of the completion

reserved1
    reserved

rbid
    unique tag of the received buffer

size
    buffer size, masked by IWL_RX_CD_SIZE

reserved2
    reserved

.. _`iwl_rx_completion_desc.bit-1`:

bit 1
-----

optional footer valid, bit 2-7: reserved)

.. _`iwl_rxq`:

struct iwl_rxq
==============

.. c:type:: struct iwl_rxq

    Rx queue

.. _`iwl_rxq.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rxq {
        int id;
        void *bd;
        dma_addr_t bd_dma;
        union {
            void *used_bd;
            __le32 *bd_32;
            struct iwl_rx_completion_desc *cd;
        } ;
        dma_addr_t used_bd_dma;
        __le16 *tr_tail;
        dma_addr_t tr_tail_dma;
        __le16 *cr_tail;
        dma_addr_t cr_tail_dma;
        u32 read;
        u32 write;
        u32 free_count;
        u32 used_count;
        u32 write_actual;
        u32 queue_size;
        struct list_head rx_free;
        struct list_head rx_used;
        bool need_update;
        void *rb_stts;
        dma_addr_t rb_stts_dma;
        spinlock_t lock;
        struct napi_struct napi;
        struct iwl_rx_mem_buffer *queue[RX_QUEUE_SIZE];
    }

.. _`iwl_rxq.members`:

Members
-------

id
    queue index

bd
    driver's pointer to buffer of receive buffer descriptors (rbd).
    Address size is 32 bit in pre-9000 devices and 64 bit in 9000 devices.
    In 22560 devices it is a pointer to a list of iwl_rx_transfer_desc's

bd_dma
    bus address of buffer of receive buffer descriptors (rbd)

{unnamed_union}
    anonymous

used_bd
    *undescribed*

bd_32
    *undescribed*

cd
    *undescribed*

used_bd_dma
    *undescribed*

tr_tail
    driver's pointer to the transmission ring tail buffer

tr_tail_dma
    physical address of the buffer for the transmission ring tail

cr_tail
    driver's pointer to the completion ring tail buffer

cr_tail_dma
    physical address of the buffer for the completion ring tail

read
    Shared index to newest available Rx buffer

write
    Shared index to oldest written Rx packet

free_count
    Number of pre-allocated buffers in rx_free

used_count
    Number of RBDs handled to allocator to use for allocation

write_actual
    *undescribed*

queue_size
    *undescribed*

rx_free
    list of RBDs with allocated RB ready for use

rx_used
    list of RBDs with no RB attached

need_update
    flag to indicate we need to update read/write index

rb_stts
    driver's pointer to receive buffer status

rb_stts_dma
    bus address of receive buffer status

lock
    *undescribed*

napi
    *undescribed*

queue
    actual rx queue. Not used for multi-rx queue.

.. _`iwl_rxq.note`:

NOTE
----

rx_free and rx_used are used as a FIFO for iwl_rx_mem_buffers

.. _`iwl_rb_allocator`:

struct iwl_rb_allocator
=======================

.. c:type:: struct iwl_rb_allocator

    Rx allocator

.. _`iwl_rb_allocator.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rb_allocator {
        atomic_t req_pending;
        atomic_t req_ready;
        struct list_head rbd_allocated;
        struct list_head rbd_empty;
        spinlock_t lock;
        struct workqueue_struct *alloc_wq;
        struct work_struct rx_alloc;
    }

.. _`iwl_rb_allocator.members`:

Members
-------

req_pending
    number of requests the allcator had not processed yet

req_ready
    number of requests honored and ready for claiming

rbd_allocated
    RBDs with pages allocated and ready to be handled to
    the queue. This is a list of \ :c:type:`struct iwl_rx_mem_buffer <iwl_rx_mem_buffer>`\ 

rbd_empty
    RBDs with no page attached for allocator use. This is a list
    of \ :c:type:`struct iwl_rx_mem_buffer <iwl_rx_mem_buffer>`\ 

lock
    protects the rbd_allocated and rbd_empty lists

alloc_wq
    work queue for background calls

rx_alloc
    work struct for background calls

.. _`iwl_queue_inc_wrap`:

iwl_queue_inc_wrap
==================

.. c:function:: int iwl_queue_inc_wrap(struct iwl_trans *trans, int index)

    increment queue index, wrap back to beginning \ ``index``\  -- current index

    :param trans:
        *undescribed*
    :type trans: struct iwl_trans \*

    :param index:
        *undescribed*
    :type index: int

.. _`iwl_get_closed_rb_stts`:

iwl_get_closed_rb_stts
======================

.. c:function:: __le16 iwl_get_closed_rb_stts(struct iwl_trans *trans, struct iwl_rxq *rxq)

    get closed rb stts from different structs \ ``rxq``\  - the rxq to get the rb stts from

    :param trans:
        *undescribed*
    :type trans: struct iwl_trans \*

    :param rxq:
        *undescribed*
    :type rxq: struct iwl_rxq \*

.. _`iwl_queue_dec_wrap`:

iwl_queue_dec_wrap
==================

.. c:function:: int iwl_queue_dec_wrap(struct iwl_trans *trans, int index)

    decrement queue index, wrap back to end \ ``index``\  -- current index

    :param trans:
        *undescribed*
    :type trans: struct iwl_trans \*

    :param index:
        *undescribed*
    :type index: int

.. _`iwl_txq`:

struct iwl_txq
==============

.. c:type:: struct iwl_txq

    Tx Queue for DMA

.. _`iwl_txq.definition`:

Definition
----------

.. code-block:: c

    struct iwl_txq {
        void *tfds;
        struct iwl_pcie_first_tb_buf *first_tb_bufs;
        dma_addr_t first_tb_dma;
        struct iwl_pcie_txq_entry *entries;
        spinlock_t lock;
        unsigned long frozen_expiry_remainder;
        struct timer_list stuck_timer;
        struct iwl_trans_pcie *trans_pcie;
        bool need_update;
        bool frozen;
        bool ampdu;
        int block;
        unsigned long wd_timeout;
        struct sk_buff_head overflow_q;
        struct iwl_dma_ptr bc_tbl;
        int write_ptr;
        int read_ptr;
        dma_addr_t dma_addr;
        int n_window;
        u32 id;
        int low_mark;
        int high_mark;
    }

.. _`iwl_txq.members`:

Members
-------

tfds
    transmit frame descriptors (DMA memory)

first_tb_bufs
    start of command headers, including scratch buffers, for
    the writeback -- this is DMA memory and an array holding one buffer
    for each command on the queue

first_tb_dma
    DMA address for the first_tb_bufs start

entries
    transmit entries (driver state)

lock
    queue lock

frozen_expiry_remainder
    remember how long until the timer fires

stuck_timer
    timer that fires if queue gets stuck

trans_pcie
    pointer back to transport (for timer)

need_update
    indicates need to update read/write index

frozen
    tx stuck queue timer is frozen

ampdu
    true if this queue is an ampdu queue for an specific RA/TID

block
    *undescribed*

wd_timeout
    queue watchdog timeout (jiffies) - per queue

overflow_q
    *undescribed*

bc_tbl
    byte count table of the queue (relevant only for gen2 transport)

write_ptr
    1-st empty entry (index) host_w

read_ptr
    last used entry (index) host_r

dma_addr
    physical addr for BD's

n_window
    safe queue window

id
    queue id

low_mark
    low watermark, resume queue if free space more than this

high_mark
    high watermark, stop queue if free space less than this

.. _`iwl_txq.description`:

Description
-----------

A Tx queue consists of circular buffer of BDs (a.k.a. TFDs, transmit frame
descriptors) and required locking structures.

.. _`iwl_txq.note-the-difference-between-tfd_queue_size_max-and-n_window`:

Note the difference between TFD_QUEUE_SIZE_MAX and n_window
-----------------------------------------------------------

the hardware
always assumes 256 descriptors, so TFD_QUEUE_SIZE_MAX is always 256 (unless
there might be HW changes in the future). For the normal TX
queues, n_window, which is the size of the software queue data
is also 256; however, for the command queue, n_window is only
32 since we don't need so many commands pending. Since the HW
still uses 256 BDs for DMA though, TFD_QUEUE_SIZE_MAX stays 256.

.. _`iwl_txq.hw-entries`:

HW entries
----------

\| 0 \| ... \| N \* 32 \| ... \| N \* 32 + 31 \| ... \| 255 \|

.. _`iwl_txq.sw-entries`:

SW entries
----------

\| 0      \| ... \| 31          \|
where N is a number between 0 and 7. This means that the SW
data is a window overlayed over the HW queue.

.. _`iwl_shared_irq_flags`:

enum iwl_shared_irq_flags
=========================

.. c:type:: enum iwl_shared_irq_flags

    level of sharing for irq

.. _`iwl_shared_irq_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_shared_irq_flags {
        IWL_SHARED_IRQ_NON_RX,
        IWL_SHARED_IRQ_FIRST_RSS
    };

.. _`iwl_shared_irq_flags.constants`:

Constants
---------

IWL_SHARED_IRQ_NON_RX
    interrupt vector serves non rx causes.

IWL_SHARED_IRQ_FIRST_RSS
    interrupt vector serves first RSS queue.

.. _`iwl_image_response_code`:

enum iwl_image_response_code
============================

.. c:type:: enum iwl_image_response_code

    image response values

.. _`iwl_image_response_code.definition`:

Definition
----------

.. code-block:: c

    enum iwl_image_response_code {
        IWL_IMAGE_RESP_DEF,
        IWL_IMAGE_RESP_SUCCESS,
        IWL_IMAGE_RESP_FAIL
    };

.. _`iwl_image_response_code.constants`:

Constants
---------

IWL_IMAGE_RESP_DEF
    the default value of the register

IWL_IMAGE_RESP_SUCCESS
    iml was read successfully

IWL_IMAGE_RESP_FAIL
    iml reading failed

.. _`iwl_self_init_dram`:

struct iwl_self_init_dram
=========================

.. c:type:: struct iwl_self_init_dram

    dram data used by self init process

.. _`iwl_self_init_dram.definition`:

Definition
----------

.. code-block:: c

    struct iwl_self_init_dram {
        struct iwl_dram_data *fw;
        int fw_cnt;
        struct iwl_dram_data *paging;
        int paging_cnt;
    }

.. _`iwl_self_init_dram.members`:

Members
-------

fw
    lmac and umac dram data

fw_cnt
    total number of items in array

paging
    paging dram data

paging_cnt
    total number of items in array

.. _`iwl_trans_pcie`:

struct iwl_trans_pcie
=====================

.. c:type:: struct iwl_trans_pcie

    PCIe transport specific data

.. _`iwl_trans_pcie.definition`:

Definition
----------

.. code-block:: c

    struct iwl_trans_pcie {
        struct iwl_rxq *rxq;
        struct iwl_rx_mem_buffer rx_pool[RX_POOL_SIZE];
        struct iwl_rx_mem_buffer *global_table[RX_POOL_SIZE];
        struct iwl_rb_allocator rba;
        union {
            struct iwl_context_info *ctxt_info;
            struct iwl_context_info_gen3 *ctxt_info_gen3;
        } ;
        struct iwl_prph_info *prph_info;
        struct iwl_prph_scratch *prph_scratch;
        dma_addr_t ctxt_info_dma_addr;
        dma_addr_t prph_info_dma_addr;
        dma_addr_t prph_scratch_dma_addr;
        dma_addr_t iml_dma_addr;
        struct iwl_self_init_dram init_dram;
        struct iwl_trans *trans;
        struct net_device napi_dev;
        struct __percpu iwl_tso_hdr_page *tso_hdr_page;
        __le32 *ict_tbl;
        dma_addr_t ict_tbl_dma;
        int ict_index;
        bool use_ict;
        bool is_down, opmode_down;
        bool debug_rfkill;
        struct isr_statistics isr_stats;
        spinlock_t irq_lock;
        struct mutex mutex;
        u32 inta_mask;
        u32 scd_base_addr;
        struct iwl_dma_ptr scd_bc_tbls;
        struct iwl_dma_ptr kw;
        struct iwl_txq *txq_memory;
        struct iwl_txq *txq[IWL_MAX_TVQM_QUEUES];
        unsigned long queue_used[BITS_TO_LONGS(IWL_MAX_TVQM_QUEUES)];
        unsigned long queue_stopped[BITS_TO_LONGS(IWL_MAX_TVQM_QUEUES)];
        struct pci_dev *pci_dev;
        void __iomem *hw_base;
        bool ucode_write_complete;
        wait_queue_head_t ucode_write_waitq;
        wait_queue_head_t wait_command_queue;
        wait_queue_head_t d0i3_waitq;
        u8 page_offs, dev_cmd_offs;
        u8 cmd_queue;
        u8 def_rx_queue;
        u8 cmd_fifo;
        unsigned int cmd_q_wdg_timeout;
        u8 n_no_reclaim_cmds;
        u8 no_reclaim_cmds[MAX_NO_RECLAIM_CMDS];
        u8 max_tbs;
        u16 tfd_size;
        enum iwl_amsdu_size rx_buf_size;
        bool bc_table_dword;
        bool scd_set_active;
        bool sw_csum_tx;
        bool pcie_dbg_dumped_once;
        u32 rx_page_order;
        spinlock_t reg_lock;
        bool cmd_hold_nic_awake;
        bool ref_cmd_in_flight;
        struct msix_entry msix_entries[IWL_MAX_RX_HW_QUEUES];
        bool msix_enabled;
        u8 shared_vec_mask;
        u32 alloc_vecs;
        u32 def_irq;
        u32 fh_init_mask;
        u32 hw_init_mask;
        u32 fh_mask;
        u32 hw_mask;
        cpumask_t affinity_mask[IWL_MAX_RX_HW_QUEUES];
        u16 tx_cmd_queue_size;
        bool in_rescan;
    }

.. _`iwl_trans_pcie.members`:

Members
-------

rxq
    all the RX queue data

rx_pool
    initial pool of iwl_rx_mem_buffer for all the queues

global_table
    table mapping received VID from hw to rxb

rba
    allocator for RX replenishing

{unnamed_union}
    anonymous

ctxt_info
    context information for FW self init

ctxt_info_gen3
    context information for gen3 devices

prph_info
    prph info for self init

prph_scratch
    prph scratch for self init

ctxt_info_dma_addr
    dma addr of context information

prph_info_dma_addr
    dma addr of prph info

prph_scratch_dma_addr
    dma addr of prph scratch

iml_dma_addr
    *undescribed*

init_dram
    DRAM data of firmware image (including paging).
    Context information addresses will be taken from here.
    This is driver's local copy for keeping track of size and
    count for allocating and freeing the memory.

trans
    pointer to the generic transport area

napi_dev
    *undescribed*

tso_hdr_page
    *undescribed*

ict_tbl
    *undescribed*

ict_tbl_dma
    *undescribed*

ict_index
    *undescribed*

use_ict
    *undescribed*

is_down
    *undescribed*

opmode_down
    *undescribed*

debug_rfkill
    *undescribed*

isr_stats
    *undescribed*

irq_lock
    *undescribed*

mutex
    to protect stop_device / start_fw / start_hw

inta_mask
    *undescribed*

scd_base_addr
    scheduler sram base address in SRAM

scd_bc_tbls
    pointer to the byte count table of the scheduler

kw
    keep warm address

txq_memory
    *undescribed*

txq
    *undescribed*

queue_used
    *undescribed*

queue_stopped
    *undescribed*

pci_dev
    basic pci-network driver stuff

hw_base
    pci hardware address support

ucode_write_complete
    indicates that the ucode has been copied.

ucode_write_waitq
    wait queue for uCode load
    \ ``cmd_queue``\  - command queue number
    \ ``def_rx_queue``\  - default rx queue number

wait_command_queue
    *undescribed*

d0i3_waitq
    *undescribed*

page_offs
    *undescribed*

dev_cmd_offs
    *undescribed*

cmd_queue
    *undescribed*

def_rx_queue
    *undescribed*

cmd_fifo
    *undescribed*

cmd_q_wdg_timeout
    *undescribed*

n_no_reclaim_cmds
    *undescribed*

no_reclaim_cmds
    *undescribed*

max_tbs
    *undescribed*

tfd_size
    *undescribed*

rx_buf_size
    Rx buffer size

bc_table_dword
    true if the BC table expects DWORD (as opposed to bytes)

scd_set_active
    should the transport configure the SCD for HCMD queue

sw_csum_tx
    if true, then the transport will compute the csum of the TXed
    frame.

pcie_dbg_dumped_once
    *undescribed*

rx_page_order
    page order for receive buffer size

reg_lock
    protect hw register access

cmd_hold_nic_awake
    *undescribed*

ref_cmd_in_flight
    *undescribed*

msix_entries
    array of MSI-X entries

msix_enabled
    true if managed to enable MSI-X

shared_vec_mask
    the type of causes the shared vector handles
    (see iwl_shared_irq_flags).

alloc_vecs
    the number of interrupt vectors allocated by the OS

def_irq
    default irq for non rx causes

fh_init_mask
    initial unmasked fh causes

hw_init_mask
    initial unmasked hw causes

fh_mask
    current unmasked fh causes

hw_mask
    current unmasked hw causes

affinity_mask
    *undescribed*

tx_cmd_queue_size
    *undescribed*

in_rescan
    true if we have triggered a device rescan

.. This file was automatic generated / don't edit.

