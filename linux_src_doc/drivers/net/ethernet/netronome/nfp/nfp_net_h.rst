.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net.h

.. _`nfp_net_tx_buf`:

struct nfp_net_tx_buf
=====================

.. c:type:: struct nfp_net_tx_buf

    software TX buffer descriptor

.. _`nfp_net_tx_buf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_tx_buf {
        union {unnamed_union};
        dma_addr_t dma_addr;
        short int fidx;
        u16 pkt_cnt;
        u32 real_len;
    }

.. _`nfp_net_tx_buf.members`:

Members
-------

{unnamed_union}
    anonymous


dma_addr
    DMA mapping address of the buffer

fidx
    Fragment index (-1 for the head and [0..nr_frags-1] for frags)

pkt_cnt
    Number of packets to be produced out of the skb associated
    with this buffer (valid only on the head's buffer).
    Will be 1 for all non-TSO packets.

real_len
    Number of bytes which to be produced out of the skb (valid only
    on the head's buffer). Equal to skb->len for non-TSO packets.

.. _`nfp_net_tx_ring`:

struct nfp_net_tx_ring
======================

.. c:type:: struct nfp_net_tx_ring

    TX ring structure

.. _`nfp_net_tx_ring.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_tx_ring {
        struct nfp_net_r_vector *r_vec;
        u32 idx;
        int qcidx;
        u8 __iomem *qcp_q;
        u32 cnt;
        u32 wr_p;
        u32 rd_p;
        u32 qcp_rd_p;
        u32 wr_ptr_add;
        struct nfp_net_tx_buf *txbufs;
        struct nfp_net_tx_desc *txds;
        dma_addr_t dma;
        unsigned int size;
    }

.. _`nfp_net_tx_ring.members`:

Members
-------

r_vec
    Back pointer to ring vector structure

idx
    Ring index from Linux's perspective

qcidx
    Queue Controller Peripheral (QCP) queue index for the TX queue

qcp_q
    Pointer to base of the QCP TX queue

cnt
    Size of the queue in number of descriptors

wr_p
    TX ring write pointer (free running)

rd_p
    TX ring read pointer (free running)

qcp_rd_p
    Local copy of QCP TX queue read pointer

wr_ptr_add
    Accumulated number of buffers to add to QCP write pointer
    (used for .xmit_more delayed kick)

txbufs
    Array of transmitted TX buffers, to free on transmit

txds
    Virtual address of TX ring in host memory

dma
    DMA address of the TX ring

size
    Size, in bytes, of the TX ring (needed to free)

.. _`nfp_net_rx_buf`:

struct nfp_net_rx_buf
=====================

.. c:type:: struct nfp_net_rx_buf

    software RX buffer descriptor

.. _`nfp_net_rx_buf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_rx_buf {
        void *frag;
        dma_addr_t dma_addr;
    }

.. _`nfp_net_rx_buf.members`:

Members
-------

frag
    page fragment buffer

dma_addr
    DMA mapping address of the buffer

.. _`nfp_net_rx_ring`:

struct nfp_net_rx_ring
======================

.. c:type:: struct nfp_net_rx_ring

    RX ring structure

.. _`nfp_net_rx_ring.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_rx_ring {
        struct nfp_net_r_vector *r_vec;
        u32 cnt;
        u32 wr_p;
        u32 rd_p;
        u16 idx;
        u16 wr_ptr_add;
        int fl_qcidx;
        int rx_qcidx;
        u8 __iomem *qcp_fl;
        u8 __iomem *qcp_rx;
        struct nfp_net_rx_buf *rxbufs;
        struct nfp_net_rx_desc *rxds;
        dma_addr_t dma;
        unsigned int size;
        unsigned int bufsz;
    }

.. _`nfp_net_rx_ring.members`:

Members
-------

r_vec
    Back pointer to ring vector structure

cnt
    Size of the queue in number of descriptors

wr_p
    FL/RX ring write pointer (free running)

rd_p
    FL/RX ring read pointer (free running)

idx
    Ring index from Linux's perspective

wr_ptr_add
    Accumulated number of buffers to add to QCP write pointer
    (used for free list batching)

fl_qcidx
    Queue Controller Peripheral (QCP) queue index for the freelist

rx_qcidx
    Queue Controller Peripheral (QCP) queue index for the RX queue

qcp_fl
    Pointer to base of the QCP freelist queue

qcp_rx
    Pointer to base of the QCP RX queue

rxbufs
    Array of transmitted FL/RX buffers

rxds
    Virtual address of FL/RX ring in host memory

dma
    DMA address of the FL/RX ring

size
    Size, in bytes, of the FL/RX ring (needed to free)

bufsz
    Buffer allocation size for convenience of management routines
    (NOTE: this is in second cache line, do not use on fast path!)

.. _`nfp_net_r_vector`:

struct nfp_net_r_vector
=======================

.. c:type:: struct nfp_net_r_vector

    Per ring interrupt vector configuration

.. _`nfp_net_r_vector.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_r_vector {
        struct nfp_net *nfp_net;
        struct napi_struct napi;
        struct nfp_net_tx_ring *tx_ring;
        struct nfp_net_rx_ring *rx_ring;
        int irq_idx;
        struct u64_stats_sync rx_sync;
        u64 rx_pkts;
        u64 rx_bytes;
        u64 rx_drops;
        u64 hw_csum_rx_ok;
        u64 hw_csum_rx_inner_ok;
        u64 hw_csum_rx_error;
        struct nfp_net_tx_ring *xdp_ring;
        struct u64_stats_sync tx_sync;
        u64 tx_pkts;
        u64 tx_bytes;
        u64 hw_csum_tx;
        u64 hw_csum_tx_inner;
        u64 tx_gather;
        u64 tx_lso;
        u64 tx_errors;
        u64 tx_busy;
        irq_handler_t handler;
        char name[IFNAMSIZ + 8];
        cpumask_t affinity_mask;
    }

.. _`nfp_net_r_vector.members`:

Members
-------

nfp_net
    Backpointer to nfp_net structure

napi
    NAPI structure for this ring vec

tx_ring
    Pointer to TX ring

rx_ring
    Pointer to RX ring

irq_idx
    Index into MSI-X table

rx_sync
    Seqlock for atomic updates of RX stats

rx_pkts
    Number of received packets

rx_bytes
    Number of received bytes

rx_drops
    Number of packets dropped on RX due to lack of resources

hw_csum_rx_ok
    Counter of packets where the HW checksum was OK

hw_csum_rx_inner_ok
    Counter of packets where the inner HW checksum was OK

hw_csum_rx_error
    Counter of packets with bad checksums

xdp_ring
    Pointer to an extra TX ring for XDP

tx_sync
    Seqlock for atomic updates of TX stats

tx_pkts
    Number of Transmitted packets

tx_bytes
    Number of Transmitted bytes

hw_csum_tx
    Counter of packets with TX checksum offload requested

hw_csum_tx_inner
    Counter of inner TX checksum offload requests

tx_gather
    Counter of packets with Gather DMA

tx_lso
    Counter of LSO packets sent

tx_errors
    How many TX errors were encountered

tx_busy
    How often was TX busy (no space)?

handler
    Interrupt handler for this ring vector

name
    Name of the interrupt vector

affinity_mask
    SMP affinity mask for this vector

.. _`nfp_net_r_vector.description`:

Description
-----------

This structure ties RX and TX rings to interrupt vectors and a NAPI
context. This currently only supports one RX and TX ring per
interrupt vector but might be extended in the future to allow
association of multiple rings per vector.

.. _`nfp_net`:

struct nfp_net
==============

.. c:type:: struct nfp_net

    NFP network device structure

.. _`nfp_net.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net {
        struct pci_dev *pdev;
        struct net_device *netdev;
        unsigned nfp_fallback:1;
        unsigned is_vf:1;
        unsigned fw_loaded:1;
        unsigned bpf_offload_skip_sw:1;
        unsigned bpf_offload_xdp:1;
        u32 ctrl;
        u32 fl_bufsz;
        u32 rx_offset;
        struct bpf_prog *xdp_prog;
        struct nfp_net_tx_ring *tx_rings;
        struct nfp_net_rx_ring *rx_rings;
    #ifdef CONFIG_PCI_IOV
        unsigned int num_vfs;
        struct vf_data_storage *vfinfo;
        int vf_rate_link_speed;
    #endif
        struct nfp_cpp *cpp;
        struct platform_device *nfp_dev_cpp;
        struct nfp_cpp_area *ctrl_area;
        struct nfp_cpp_area *tx_area;
        struct nfp_cpp_area *rx_area;
        struct nfp_net_fw_version fw_ver;
        u32 cap;
        u32 max_mtu;
        u32 rss_cfg;
        u8 rss_key[NFP_NET_CFG_RSS_KEY_SZ];
        u8 rss_itbl[NFP_NET_CFG_RSS_ITBL_SZ];
        struct nfp_stat_pair rx_filter;
        struct nfp_stat_pair rx_filter_prev;
        unsigned long rx_filter_change;
        struct timer_list rx_filter_stats_timer;
        spinlock_t rx_filter_lock;
        unsigned int max_tx_rings;
        unsigned int max_rx_rings;
        unsigned int num_tx_rings;
        unsigned int num_stack_tx_rings;
        unsigned int num_rx_rings;
        int stride_tx;
        int stride_rx;
        int txd_cnt;
        int rxd_cnt;
        unsigned int max_r_vecs;
        unsigned int num_r_vecs;
        struct nfp_net_r_vector r_vecs[NFP_NET_MAX_R_VECS];
        struct msix_entry irq_entries[NFP_NET_MAX_IRQS];
        irq_handler_t lsc_handler;
        char lsc_name[IFNAMSIZ + 8];
        irq_handler_t exn_handler;
        char exn_name[IFNAMSIZ + 8];
        irq_handler_t shared_handler;
        char shared_name[IFNAMSIZ + 8];
        u32 me_freq_mhz;
        bool link_up;
        spinlock_t link_status_lock;
        spinlock_t reconfig_lock;
        u32 reconfig_posted;
        bool reconfig_timer_active;
        bool reconfig_sync_present;
        struct timer_list reconfig_timer;
        u32 rx_coalesce_usecs;
        u32 rx_coalesce_max_frames;
        u32 tx_coalesce_usecs;
        u32 tx_coalesce_max_frames;
        __be16 vxlan_ports[NFP_NET_N_VXLAN_PORTS];
        u8 vxlan_usecnt[NFP_NET_N_VXLAN_PORTS];
        u8 __iomem *qcp_cfg;
        u8 __iomem *ctrl_bar;
        u8 __iomem *q_bar;
        u8 __iomem *tx_bar;
        u8 __iomem *rx_bar;
        struct dentry *debugfs_dir;
    }

.. _`nfp_net.members`:

Members
-------

pdev
    Backpointer to PCI device

netdev
    Backpointer to net_device structure

nfp_fallback
    Is the driver used in fallback mode?

is_vf
    Is the driver attached to a VF?

fw_loaded
    Is the firmware loaded?

bpf_offload_skip_sw
    Offloaded BPF program will not be rerun by cls_bpf

bpf_offload_xdp
    Offloaded BPF program is XDP

ctrl
    Local copy of the control register/word.

fl_bufsz
    Currently configured size of the freelist buffers

rx_offset
    Offset in the RX buffers where packet data starts

xdp_prog
    Installed XDP program

tx_rings
    Array of pre-allocated TX ring structures

rx_rings
    Array of pre-allocated RX ring structures

num_vfs
    *undescribed*

vfinfo
    *undescribed*

vf_rate_link_speed
    *undescribed*

cpp
    Pointer to the CPP handle

nfp_dev_cpp
    Pointer to the NFP Device handle

ctrl_area
    Pointer to the CPP area for the control BAR

tx_area
    Pointer to the CPP area for the TX queues

rx_area
    Pointer to the CPP area for the FL/RX queues

fw_ver
    Firmware version

cap
    Capabilities advertised by the Firmware

max_mtu
    Maximum support MTU advertised by the Firmware

rss_cfg
    RSS configuration

rss_key
    RSS secret key

rss_itbl
    RSS indirection table

rx_filter
    Filter offload statistics - dropped packets/bytes

rx_filter_prev
    Filter offload statistics - values from previous update

rx_filter_change
    Jiffies when statistics last changed

rx_filter_stats_timer
    Timer for polling filter offload statistics

rx_filter_lock
    Lock protecting timer state changes (teardown)

max_tx_rings
    Maximum number of TX rings supported by the Firmware

max_rx_rings
    Maximum number of RX rings supported by the Firmware

num_tx_rings
    Currently configured number of TX rings

num_stack_tx_rings
    Number of TX rings used by the stack (not XDP)

num_rx_rings
    Currently configured number of RX rings

stride_tx
    *undescribed*

stride_rx
    *undescribed*

txd_cnt
    Size of the TX ring in number of descriptors

rxd_cnt
    Size of the RX ring in number of descriptors

max_r_vecs
    Number of allocated interrupt vectors for RX/TX

num_r_vecs
    Number of used ring vectors

r_vecs
    Pre-allocated array of ring vectors

irq_entries
    Pre-allocated array of MSI-X entries

lsc_handler
    Handler for Link State Change interrupt

lsc_name
    Name for Link State Change interrupt

exn_handler
    Handler for Exception interrupt

exn_name
    Name for Exception interrupt

shared_handler
    Handler for shared interrupts

shared_name
    Name for shared interrupt

me_freq_mhz
    ME clock_freq (MHz)

link_up
    Is the link up?

link_status_lock
    Protects \ ``link_up``\  and ensures atomicity with BAR reading

reconfig_lock
    Protects HW reconfiguration request regs/machinery

reconfig_posted
    Pending reconfig bits coming from async sources

reconfig_timer_active
    Timer for reading reconfiguration results is pending

reconfig_sync_present
    Some thread is performing synchronous reconfig

reconfig_timer
    Timer for async reading of reconfig results

rx_coalesce_usecs
    RX interrupt moderation usecs delay parameter

rx_coalesce_max_frames
    RX interrupt moderation frame count parameter

tx_coalesce_usecs
    TX interrupt moderation usecs delay parameter

tx_coalesce_max_frames
    TX interrupt moderation frame count parameter

vxlan_ports
    VXLAN ports for RX inner csum offload communicated to HW

vxlan_usecnt
    IPv4/IPv6 VXLAN port use counts

qcp_cfg
    Pointer to QCP queue used for configuration notification

ctrl_bar
    Pointer to mapped control BAR

q_bar
    *undescribed*

tx_bar
    Pointer to mapped TX queues

rx_bar
    Pointer to mapped FL/RX queues

debugfs_dir
    Device directory in debugfs

.. _`nfp_qcp_rd_ptr_add`:

nfp_qcp_rd_ptr_add
==================

.. c:function:: void nfp_qcp_rd_ptr_add(u8 __iomem *q, u32 val)

    Add the value to the read pointer of a queue

    :param u8 __iomem \*q:
        Base address for queue structure

    :param u32 val:
        Value to add to the queue pointer

.. _`nfp_qcp_rd_ptr_add.description`:

Description
-----------

If \ ``val``\  is greater than \ ``NFP_QCP_MAX_ADD``\  multiple writes are performed.

.. _`nfp_qcp_wr_ptr_add`:

nfp_qcp_wr_ptr_add
==================

.. c:function:: void nfp_qcp_wr_ptr_add(u8 __iomem *q, u32 val)

    Add the value to the write pointer of a queue

    :param u8 __iomem \*q:
        Base address for queue structure

    :param u32 val:
        Value to add to the queue pointer

.. _`nfp_qcp_wr_ptr_add.description`:

Description
-----------

If \ ``val``\  is greater than \ ``NFP_QCP_MAX_ADD``\  multiple writes are performed.

.. _`nfp_qcp_rd_ptr_read`:

nfp_qcp_rd_ptr_read
===================

.. c:function:: u32 nfp_qcp_rd_ptr_read(u8 __iomem *q)

    Read the current read pointer value for a queue

    :param u8 __iomem \*q:
        Base address for queue structure

.. _`nfp_qcp_rd_ptr_read.return`:

Return
------

Value read.

.. _`nfp_qcp_wr_ptr_read`:

nfp_qcp_wr_ptr_read
===================

.. c:function:: u32 nfp_qcp_wr_ptr_read(u8 __iomem *q)

    Read the current write pointer value for a queue

    :param u8 __iomem \*q:
        Base address for queue structure

.. _`nfp_qcp_wr_ptr_read.return`:

Return
------

Value read.

.. This file was automatic generated / don't edit.

