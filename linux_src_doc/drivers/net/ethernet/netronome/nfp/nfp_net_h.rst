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
        bool is_xdp;
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

is_xdp
    Is this a XDP TX ring?

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
        u32 idx;
        int fl_qcidx;
        u8 __iomem *qcp_fl;
        struct nfp_net_rx_buf *rxbufs;
        struct nfp_net_rx_desc *rxds;
        dma_addr_t dma;
        unsigned int size;
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

fl_qcidx
    Queue Controller Peripheral (QCP) queue index for the freelist

qcp_fl
    Pointer to base of the QCP freelist queue

rxbufs
    Array of transmitted FL/RX buffers

rxds
    Virtual address of FL/RX ring in host memory

dma
    DMA address of the FL/RX ring

size
    Size, in bytes, of the FL/RX ring (needed to free)

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
        union {unnamed_union};
        struct nfp_net_tx_ring *tx_ring;
        struct nfp_net_rx_ring *rx_ring;
        u16 irq_entry;
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
        u32 irq_vector;
        irq_handler_t handler;
        char name;
        cpumask_t affinity_mask;
    }

.. _`nfp_net_r_vector.members`:

Members
-------

nfp_net
    Backpointer to nfp_net structure

{unnamed_union}
    anonymous


tx_ring
    Pointer to TX ring

rx_ring
    Pointer to RX ring

irq_entry
    MSI-X table entry (use for talking to the device)

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

irq_vector
    Interrupt vector number (use for talking to the OS)

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

.. _`nfp_net_dp`:

struct nfp_net_dp
=================

.. c:type:: struct nfp_net_dp

    NFP network device datapath data structure

.. _`nfp_net_dp.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_dp {
        struct device *dev;
        struct net_device *netdev;
        u8 is_vf:1;
        u8 bpf_offload_skip_sw:1;
        u8 bpf_offload_xdp:1;
        u8 chained_metadata_format:1;
        u8 rx_dma_dir;
        u8 rx_offset;
        u32 rx_dma_off;
        u32 ctrl;
        u32 fl_bufsz;
        struct bpf_prog *xdp_prog;
        struct nfp_net_tx_ring *tx_rings;
        struct nfp_net_rx_ring *rx_rings;
        u8 __iomem *ctrl_bar;
        unsigned int txd_cnt;
        unsigned int rxd_cnt;
        unsigned int num_r_vecs;
        unsigned int num_tx_rings;
        unsigned int num_stack_tx_rings;
        unsigned int num_rx_rings;
        unsigned int mtu;
    }

.. _`nfp_net_dp.members`:

Members
-------

dev
    Backpointer to struct device

netdev
    Backpointer to net_device structure

is_vf
    Is the driver attached to a VF?

bpf_offload_skip_sw
    Offloaded BPF program will not be rerun by cls_bpf

bpf_offload_xdp
    Offloaded BPF program is XDP

chained_metadata_format
    Firemware will use new metadata format

rx_dma_dir
    Mapping direction for RX buffers

rx_offset
    Offset in the RX buffers where packet data starts

rx_dma_off
    Offset at which DMA packets (for XDP headroom)

ctrl
    Local copy of the control register/word.

fl_bufsz
    Currently configured size of the freelist buffers

xdp_prog
    Installed XDP program

tx_rings
    Array of pre-allocated TX ring structures

rx_rings
    Array of pre-allocated RX ring structures

ctrl_bar
    Pointer to mapped control BAR

txd_cnt
    Size of the TX ring in number of descriptors

rxd_cnt
    Size of the RX ring in number of descriptors

num_r_vecs
    Number of used ring vectors

num_tx_rings
    Currently configured number of TX rings

num_stack_tx_rings
    Number of TX rings used by the stack (not XDP)

num_rx_rings
    Currently configured number of RX rings

mtu
    Device MTU

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
        struct nfp_net_dp dp;
        struct nfp_net_fw_version fw_ver;
        u32 cap;
        u32 max_mtu;
        u8 rss_hfunc;
        u32 rss_cfg;
        u8 rss_key;
        u8 rss_itbl;
        u32 xdp_flags;
        struct bpf_prog *xdp_prog;
        unsigned int max_tx_rings;
        unsigned int max_rx_rings;
        int stride_tx;
        int stride_rx;
        unsigned int max_r_vecs;
        struct nfp_net_r_vector r_vecs;
        struct msix_entry irq_entries;
        irq_handler_t lsc_handler;
        char lsc_name;
        irq_handler_t exn_handler;
        char exn_name;
        irq_handler_t shared_handler;
        char shared_name;
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
        __be16 vxlan_ports;
        u8 vxlan_usecnt;
        u8 __iomem *qcp_cfg;
        u8 __iomem *tx_bar;
        u8 __iomem *rx_bar;
        struct dentry *debugfs_dir;
        struct list_head vnic_list;
        struct pci_dev *pdev;
        struct nfp_app *app;
        struct nfp_port *port;
        void *app_priv;
    }

.. _`nfp_net.members`:

Members
-------

dp
    Datapath structure

fw_ver
    Firmware version

cap
    Capabilities advertised by the Firmware

max_mtu
    Maximum support MTU advertised by the Firmware

rss_hfunc
    RSS selected hash function

rss_cfg
    RSS configuration

rss_key
    RSS secret key

rss_itbl
    RSS indirection table

xdp_flags
    Flags with which XDP prog was loaded

xdp_prog
    XDP prog (for ctrl path, both DRV and HW modes)

max_tx_rings
    Maximum number of TX rings supported by the Firmware

max_rx_rings
    Maximum number of RX rings supported by the Firmware

stride_tx
    *undescribed*

stride_rx
    *undescribed*

max_r_vecs
    Number of allocated interrupt vectors for RX/TX

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
    Protects \ ``link``\ \_\* and ensures atomicity with BAR reading

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

tx_bar
    Pointer to mapped TX queues

rx_bar
    Pointer to mapped FL/RX queues

debugfs_dir
    Device directory in debugfs

vnic_list
    Entry on device vNIC list

pdev
    Backpointer to PCI device

app
    APP handle if available

port
    Pointer to nfp_port structure if vNIC is a port

app_priv
    APP private data for this vNIC

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

