.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/net_driver.h

.. _`efx_buffer`:

struct efx_buffer
=================

.. c:type:: struct efx_buffer

    A general-purpose DMA buffer

.. _`efx_buffer.definition`:

Definition
----------

.. code-block:: c

    struct efx_buffer {
        void *addr;
        dma_addr_t dma_addr;
        unsigned int len;
    }

.. _`efx_buffer.members`:

Members
-------

addr
    host base address of the buffer

dma_addr
    DMA base address of the buffer

len
    Buffer length, in bytes

.. _`efx_buffer.description`:

Description
-----------

The NIC uses these buffers for its interrupt status registers and
MAC stats dumps.

.. _`efx_special_buffer`:

struct efx_special_buffer
=========================

.. c:type:: struct efx_special_buffer

    DMA buffer entered into buffer table

.. _`efx_special_buffer.definition`:

Definition
----------

.. code-block:: c

    struct efx_special_buffer {
        struct efx_buffer buf;
        unsigned int index;
        unsigned int entries;
    }

.. _`efx_special_buffer.members`:

Members
-------

buf
    Standard \ :c:type:`struct efx_buffer <efx_buffer>`\ 

index
    Buffer index within controller;s buffer table

entries
    Number of buffer table entries

.. _`efx_special_buffer.description`:

Description
-----------

The NIC has a buffer table that maps buffers of size \ ``EFX_BUF_SIZE``\ .
Event and descriptor rings are addressed via one or more buffer
table entries (and so can be physically non-contiguous, although we
currently do not take advantage of that).  On Falcon and Siena we
have to take care of allocating and initialising the entries
ourselves.  On later hardware this is managed by the firmware and
\ ``index``\  and \ ``entries``\  are left as 0.

.. _`efx_tx_buffer`:

struct efx_tx_buffer
====================

.. c:type:: struct efx_tx_buffer

    buffer state for a TX descriptor

.. _`efx_tx_buffer.definition`:

Definition
----------

.. code-block:: c

    struct efx_tx_buffer {
        const struct sk_buff *skb;
        union {
            efx_qword_t option;
            dma_addr_t dma_addr;
        } ;
        unsigned short flags;
        unsigned short len;
        unsigned short unmap_len;
        unsigned short dma_offset;
    }

.. _`efx_tx_buffer.members`:

Members
-------

skb
    When \ ``flags``\  & \ ``EFX_TX_BUF_SKB``\ , the associated socket buffer to be
    freed when descriptor completes

{unnamed_union}
    anonymous

flags
    Flags for allocation and DMA mapping type

len
    Length of this fragment.
    This field is zero when the queue slot is empty.

unmap_len
    Length of this fragment to unmap

dma_offset
    Offset of \ ``dma_addr``\  from the address of the backing DMA mapping.
    Only valid if \ ``unmap_len``\  != 0.

.. _`efx_tx_queue`:

struct efx_tx_queue
===================

.. c:type:: struct efx_tx_queue

    An Efx TX queue

.. _`efx_tx_queue.definition`:

Definition
----------

.. code-block:: c

    struct efx_tx_queue {
        struct efx_nic *efx ____cacheline_aligned_in_smp;
        unsigned queue;
        unsigned int tso_version;
        struct efx_channel *channel;
        struct netdev_queue *core_txq;
        struct efx_tx_buffer *buffer;
        struct efx_buffer *cb_page;
        struct efx_special_buffer txd;
        unsigned int ptr_mask;
        void __iomem *piobuf;
        unsigned int piobuf_offset;
        bool initialised;
        int (*handle_tso)(struct efx_tx_queue*, struct sk_buff*, bool *);
        unsigned int read_count ____cacheline_aligned_in_smp;
        unsigned int old_write_count;
        unsigned int merge_events;
        unsigned int bytes_compl;
        unsigned int pkts_compl;
        unsigned int insert_count ____cacheline_aligned_in_smp;
        unsigned int write_count;
        unsigned int packet_write_count;
        unsigned int old_read_count;
        unsigned int tso_bursts;
        unsigned int tso_long_headers;
        unsigned int tso_packets;
        unsigned int tso_fallbacks;
        unsigned int pushes;
        unsigned int pio_packets;
        bool xmit_more_available;
        unsigned int cb_packets;
        unsigned long tx_packets;
        unsigned int empty_read_count ____cacheline_aligned_in_smp;
    #define EFX_EMPTY_COUNT_VALID 0x80000000
        atomic_t flush_outstanding;
    }

.. _`efx_tx_queue.members`:

Members
-------

____cacheline_aligned_in_smp
    *undescribed*

queue
    DMA queue number

tso_version
    Version of TSO in use for this queue.

channel
    The associated channel

core_txq
    The networking core TX queue structure

buffer
    The software buffer ring

cb_page
    Array of pages of copy buffers.  Carved up according to
    \ ``EFX_TX_CB_ORDER``\  into \ ``EFX_TX_CB_SIZE-sized``\  chunks.

txd
    The hardware descriptor ring

ptr_mask
    The size of the ring minus 1.

piobuf
    PIO buffer region for this TX queue (shared with its partner).
    Size of the region is efx_piobuf_size.

piobuf_offset
    Buffer offset to be specified in PIO descriptors

initialised
    Has hardware queue been initialised?

handle_tso
    TSO xmit preparation handler.  Sets up the TSO metadata and
    may also map tx data, depending on the nature of the TSO implementation.

____cacheline_aligned_in_smp
    *undescribed*

old_write_count
    The value of \ ``write_count``\  when last checked.
    This is here for performance reasons.  The xmit path will
    only get the up-to-date value of \ ``write_count``\  if this
    variable indicates that the queue is empty.  This is to
    avoid cache-line ping-pong between the xmit path and the
    completion path.

merge_events
    Number of TX merged completion events

bytes_compl
    *undescribed*

pkts_compl
    *undescribed*

____cacheline_aligned_in_smp
    *undescribed*

write_count
    Current write pointer
    This is the number of buffers that have been added to the
    hardware ring.

packet_write_count
    Completable write pointer
    This is the write pointer of the last packet written.
    Normally this will equal \ ``write_count``\ , but as option descriptors
    don't produce completion events, they won't update this.
    Filled in iff \ ``efx``\ ->type->option_descriptors; only used for PIO.
    Thus, this is written and used on EF10, and neither on farch.

old_read_count
    The value of read_count when last checked.
    This is here for performance reasons.  The xmit path will
    only get the up-to-date value of read_count if this
    variable indicates that the queue is full.  This is to
    avoid cache-line ping-pong between the xmit path and the
    completion path.

tso_bursts
    Number of times TSO xmit invoked by kernel

tso_long_headers
    Number of packets with headers too long for standard
    blocks

tso_packets
    Number of packets via the TSO xmit path

tso_fallbacks
    Number of times TSO fallback used

pushes
    Number of times the TX push feature has been used

pio_packets
    Number of times the TX PIO feature has been used

xmit_more_available
    Are any packets waiting to be pushed to the NIC

cb_packets
    Number of times the TX copybreak feature has been used

tx_packets
    *undescribed*

____cacheline_aligned_in_smp
    *undescribed*

flush_outstanding
    *undescribed*

.. _`efx_tx_queue.description`:

Description
-----------

This is a ring buffer of TX fragments.
Since the TX completion path always executes on the same
CPU and the xmit path can operate on different CPUs,
performance is increased by ensuring that the completion
path and the xmit path operate on different cache lines.
This is particularly important if the xmit path is always
executing on one CPU which is different from the completion
path.  There is also a cache line for members which are
read but not written on the fast path.

.. _`efx_rx_buffer`:

struct efx_rx_buffer
====================

.. c:type:: struct efx_rx_buffer

    An Efx RX data buffer

.. _`efx_rx_buffer.definition`:

Definition
----------

.. code-block:: c

    struct efx_rx_buffer {
        dma_addr_t dma_addr;
        struct page *page;
        u16 page_offset;
        u16 len;
        u16 flags;
    }

.. _`efx_rx_buffer.members`:

Members
-------

dma_addr
    DMA base address of the buffer

page
    The associated page buffer.
    Will be \ ``NULL``\  if the buffer slot is currently free.

page_offset
    If pending: offset in \ ``page``\  of DMA base address.

len
    If pending: length for DMA descriptor.

flags
    Flags for buffer and packet state.  These are only set on the
    first buffer of a scattered packet.

.. _`efx_rx_buffer.if-completed`:

If completed
------------

offset in \ ``page``\  of Ethernet header.

received length, excluding hash prefix.

.. _`efx_rx_page_state`:

struct efx_rx_page_state
========================

.. c:type:: struct efx_rx_page_state

    Page-based rx buffer state

.. _`efx_rx_page_state.definition`:

Definition
----------

.. code-block:: c

    struct efx_rx_page_state {
        dma_addr_t dma_addr;
        unsigned int __pad[0] ____cacheline_aligned;
    }

.. _`efx_rx_page_state.members`:

Members
-------

dma_addr
    The dma address of this page.

__pad
    *undescribed*

.. _`efx_rx_page_state.description`:

Description
-----------

Inserted at the start of every page allocated for receive buffers.
Used to facilitate sharing dma mappings between recycled rx buffers
and those passed up to the kernel.

.. _`efx_rx_queue`:

struct efx_rx_queue
===================

.. c:type:: struct efx_rx_queue

    An Efx RX queue

.. _`efx_rx_queue.definition`:

Definition
----------

.. code-block:: c

    struct efx_rx_queue {
        struct efx_nic *efx;
        int core_index;
        struct efx_rx_buffer *buffer;
        struct efx_special_buffer rxd;
        unsigned int ptr_mask;
        bool refill_enabled;
        bool flush_pending;
        unsigned int added_count;
        unsigned int notified_count;
        unsigned int removed_count;
        unsigned int scatter_n;
        unsigned int scatter_len;
        struct page **page_ring;
        unsigned int page_add;
        unsigned int page_remove;
        unsigned int page_recycle_count;
        unsigned int page_recycle_failed;
        unsigned int page_recycle_full;
        unsigned int page_ptr_mask;
        unsigned int max_fill;
        unsigned int fast_fill_trigger;
        unsigned int min_fill;
        unsigned int min_overfill;
        unsigned int recycle_count;
        struct timer_list slow_fill;
        unsigned int slow_fill_count;
        unsigned long rx_packets;
    }

.. _`efx_rx_queue.members`:

Members
-------

efx
    The associated Efx NIC

core_index
    Index of network core RX queue.  Will be >= 0 iff this
    is associated with a real RX queue.

buffer
    The software buffer ring

rxd
    The hardware descriptor ring

ptr_mask
    The size of the ring minus 1.

refill_enabled
    Enable refill whenever fill level is low

flush_pending
    Set when a RX flush is pending. Has the same lifetime as
    \ ``rxq_flush_pending``\ .

added_count
    Number of buffers added to the receive queue.

notified_count
    Number of buffers given to NIC (<= \ ``added_count``\ ).

removed_count
    Number of buffers removed from the receive queue.

scatter_n
    Used by NIC specific receive code.

scatter_len
    Used by NIC specific receive code.

page_ring
    The ring to store DMA mapped pages for reuse.

page_add
    Counter to calculate the write pointer for the recycle ring.

page_remove
    Counter to calculate the read pointer for the recycle ring.

page_recycle_count
    The number of pages that have been recycled.

page_recycle_failed
    The number of pages that couldn't be recycled because
    the kernel still held a reference to them.

page_recycle_full
    The number of pages that were released because the
    recycle ring was full.

page_ptr_mask
    The number of pages in the RX recycle ring minus 1.

max_fill
    RX descriptor maximum fill level (<= ring size)

fast_fill_trigger
    RX descriptor fill level that will trigger a fast fill
    (<= \ ``max_fill``\ )

min_fill
    RX descriptor minimum non-zero fill level.
    This records the minimum fill level observed when a ring
    refill was triggered.

min_overfill
    *undescribed*

recycle_count
    RX buffer recycle counter.

slow_fill
    Timer used to defer \ :c:func:`efx_nic_generate_fill_event`\ .

slow_fill_count
    *undescribed*

rx_packets
    *undescribed*

.. _`efx_channel`:

struct efx_channel
==================

.. c:type:: struct efx_channel

    An Efx channel

.. _`efx_channel.definition`:

Definition
----------

.. code-block:: c

    struct efx_channel {
        struct efx_nic *efx;
        int channel;
        const struct efx_channel_type *type;
        bool eventq_init;
        bool enabled;
        int irq;
        unsigned int irq_moderation_us;
        struct net_device *napi_dev;
        struct napi_struct napi_str;
    #ifdef CONFIG_NET_RX_BUSY_POLL
        unsigned long busy_poll_state;
    #endif
        struct efx_special_buffer eventq;
        unsigned int eventq_mask;
        unsigned int eventq_read_ptr;
        int event_test_cpu;
        unsigned int irq_count;
        unsigned int irq_mod_score;
    #ifdef CONFIG_RFS_ACCEL
        unsigned int rfs_filters_added;
    #define RPS_FLOW_ID_INVALID 0xFFFFFFFF
        u32 *rps_flow_id;
    #endif
        unsigned int n_rx_tobe_disc;
        unsigned int n_rx_ip_hdr_chksum_err;
        unsigned int n_rx_tcp_udp_chksum_err;
        unsigned int n_rx_outer_ip_hdr_chksum_err;
        unsigned int n_rx_outer_tcp_udp_chksum_err;
        unsigned int n_rx_inner_ip_hdr_chksum_err;
        unsigned int n_rx_inner_tcp_udp_chksum_err;
        unsigned int n_rx_eth_crc_err;
        unsigned int n_rx_mcast_mismatch;
        unsigned int n_rx_frm_trunc;
        unsigned int n_rx_overlength;
        unsigned int n_skbuff_leaks;
        unsigned int n_rx_nodesc_trunc;
        unsigned int n_rx_merge_events;
        unsigned int n_rx_merge_packets;
        unsigned int rx_pkt_n_frags;
        unsigned int rx_pkt_index;
        struct efx_rx_queue rx_queue;
        struct efx_tx_queue tx_queue[EFX_TXQ_TYPES];
        enum efx_sync_events_state sync_events_state;
        u32 sync_timestamp_major;
        u32 sync_timestamp_minor;
    }

.. _`efx_channel.members`:

Members
-------

efx
    Associated Efx NIC

channel
    Channel instance number

type
    Channel type definition

eventq_init
    Event queue initialised flag

enabled
    Channel enabled indicator

irq
    IRQ number (MSI and MSI-X only)

irq_moderation_us
    IRQ moderation value (in microseconds)

napi_dev
    Net device used with NAPI

napi_str
    NAPI control structure

busy_poll_state
    *undescribed*

eventq
    Event queue buffer

eventq_mask
    Event queue pointer mask

eventq_read_ptr
    Event queue read pointer

event_test_cpu
    Last CPU to handle interrupt or test event for this channel

irq_count
    Number of IRQs since last adaptive moderation decision

irq_mod_score
    IRQ moderation score

rfs_filters_added
    *undescribed*

rps_flow_id
    Flow IDs of filters allocated for accelerated RFS,
    indexed by filter ID

n_rx_tobe_disc
    Count of RX_TOBE_DISC errors

n_rx_ip_hdr_chksum_err
    Count of RX IP header checksum errors

n_rx_tcp_udp_chksum_err
    Count of RX TCP and UDP checksum errors

n_rx_outer_ip_hdr_chksum_err
    *undescribed*

n_rx_outer_tcp_udp_chksum_err
    *undescribed*

n_rx_inner_ip_hdr_chksum_err
    *undescribed*

n_rx_inner_tcp_udp_chksum_err
    *undescribed*

n_rx_eth_crc_err
    *undescribed*

n_rx_mcast_mismatch
    Count of unmatched multicast frames

n_rx_frm_trunc
    Count of RX_FRM_TRUNC errors

n_rx_overlength
    Count of RX_OVERLENGTH errors

n_skbuff_leaks
    Count of skbuffs leaked due to RX overrun

n_rx_nodesc_trunc
    Number of RX packets truncated and then dropped due to
    lack of descriptors

n_rx_merge_events
    Number of RX merged completion events

n_rx_merge_packets
    Number of RX packets completed by merged events

rx_pkt_n_frags
    Number of fragments in next packet to be delivered by
    \__efx_rx_packet(), or zero if there is none

rx_pkt_index
    Ring index of first buffer for next packet to be delivered
    by \__efx_rx_packet(), if \ ``rx_pkt_n_frags``\  != 0

rx_queue
    RX queue for this channel

tx_queue
    TX queues for this channel

sync_events_state
    Current state of sync events on this channel

sync_timestamp_major
    Major part of the last ptp sync event

sync_timestamp_minor
    Minor part of the last ptp sync event

.. _`efx_channel.description`:

Description
-----------

A channel comprises an event queue, at least one TX queue, at least
one RX queue, and an associated tasklet for processing the event
queue.

.. _`efx_msi_context`:

struct efx_msi_context
======================

.. c:type:: struct efx_msi_context

    Context for each MSI

.. _`efx_msi_context.definition`:

Definition
----------

.. code-block:: c

    struct efx_msi_context {
        struct efx_nic *efx;
        unsigned int index;
        char name[IFNAMSIZ + 6];
    }

.. _`efx_msi_context.members`:

Members
-------

efx
    The associated NIC

index
    Index of the channel/IRQ

name
    Name of the channel/IRQ

.. _`efx_msi_context.description`:

Description
-----------

Unlike \ :c:type:`struct efx_channel <efx_channel>`\ , this is never reallocated and is always
safe for the IRQ handler to access.

.. _`efx_channel_type`:

struct efx_channel_type
=======================

.. c:type:: struct efx_channel_type

    distinguishes traffic and extra channels

.. _`efx_channel_type.definition`:

Definition
----------

.. code-block:: c

    struct efx_channel_type {
        void (*handle_no_channel)(struct efx_nic *);
        int (*pre_probe)(struct efx_channel *);
        void (*post_remove)(struct efx_channel *);
        void (*get_name)(struct efx_channel *, char *buf, size_t len);
        struct efx_channel *(*copy)(const struct efx_channel *);
        bool (*receive_skb)(struct efx_channel *, struct sk_buff *);
        bool keep_eventq;
    }

.. _`efx_channel_type.members`:

Members
-------

handle_no_channel
    Handle failure to allocate an extra channel

pre_probe
    Set up extra state prior to initialisation

post_remove
    Tear down extra state after finalisation, if allocated.
    May be called on channels that have not been probed.

get_name
    Generate the channel's name (used for its IRQ handler)

copy
    Copy the channel state prior to reallocation.  May be \ ``NULL``\  if
    reallocation is not supported.

receive_skb
    Handle an skb ready to be passed to \ :c:func:`netif_receive_skb`\ 

keep_eventq
    Flag for whether event queue should be kept initialised
    while the device is stopped

.. _`efx_link_state`:

struct efx_link_state
=====================

.. c:type:: struct efx_link_state

    Current state of the link

.. _`efx_link_state.definition`:

Definition
----------

.. code-block:: c

    struct efx_link_state {
        bool up;
        bool fd;
        u8 fc;
        unsigned int speed;
    }

.. _`efx_link_state.members`:

Members
-------

up
    Link is up

fd
    Link is full-duplex

fc
    Actual flow control flags

speed
    Link speed (Mbps)

.. _`efx_phy_operations`:

struct efx_phy_operations
=========================

.. c:type:: struct efx_phy_operations

    Efx PHY operations table

.. _`efx_phy_operations.definition`:

Definition
----------

.. code-block:: c

    struct efx_phy_operations {
        int (*probe) (struct efx_nic *efx);
        int (*init) (struct efx_nic *efx);
        void (*fini) (struct efx_nic *efx);
        void (*remove) (struct efx_nic *efx);
        int (*reconfigure) (struct efx_nic *efx);
        bool (*poll) (struct efx_nic *efx);
        void (*get_link_ksettings)(struct efx_nic *efx, struct ethtool_link_ksettings *cmd);
        int (*set_link_ksettings)(struct efx_nic *efx, const struct ethtool_link_ksettings *cmd);
        void (*set_npage_adv) (struct efx_nic *efx, u32);
        int (*test_alive) (struct efx_nic *efx);
        const char *(*test_name) (struct efx_nic *efx, unsigned int index);
        int (*run_tests) (struct efx_nic *efx, int *results, unsigned flags);
        int (*get_module_eeprom) (struct efx_nic *efx,struct ethtool_eeprom *ee, u8 *data);
        int (*get_module_info) (struct efx_nic *efx, struct ethtool_modinfo *modinfo);
    }

.. _`efx_phy_operations.members`:

Members
-------

probe
    Probe PHY and initialise efx->mdio.mode_support, efx->mdio.mmds,
    efx->loopback_modes.

init
    Initialise PHY

fini
    Shut down PHY

remove
    *undescribed*

reconfigure
    Reconfigure PHY (e.g. for new link parameters)

poll
    Update \ ``link_state``\  and report whether it changed.
    Serialised by the mac_lock.

get_link_ksettings
    Get ethtool settings. Serialised by the mac_lock.

set_link_ksettings
    Set ethtool settings. Serialised by the mac_lock.

set_npage_adv
    Set abilities advertised in (Extended) Next Page
    (only needed where AN bit is set in mmds)

test_alive
    Test that PHY is 'alive' (online)

test_name
    Get the name of a PHY-specific test/result

run_tests
    Run tests and record results as appropriate (offline).
    Flags are the ethtool tests flags.

get_module_eeprom
    *undescribed*

get_module_info
    *undescribed*

.. _`efx_phy_mode`:

enum efx_phy_mode
=================

.. c:type:: enum efx_phy_mode

    PHY operating mode flags

.. _`efx_phy_mode.definition`:

Definition
----------

.. code-block:: c

    enum efx_phy_mode {
        PHY_MODE_NORMAL,
        PHY_MODE_TX_DISABLED,
        PHY_MODE_LOW_POWER,
        PHY_MODE_OFF,
        PHY_MODE_SPECIAL
    };

.. _`efx_phy_mode.constants`:

Constants
---------

PHY_MODE_NORMAL
    on and should pass traffic

PHY_MODE_TX_DISABLED
    on with TX disabled

PHY_MODE_LOW_POWER
    set to low power through MDIO

PHY_MODE_OFF
    switched off through external control

PHY_MODE_SPECIAL
    on but will not pass traffic

.. _`efx_hw_stat_desc`:

struct efx_hw_stat_desc
=======================

.. c:type:: struct efx_hw_stat_desc

    Description of a hardware statistic

.. _`efx_hw_stat_desc.definition`:

Definition
----------

.. code-block:: c

    struct efx_hw_stat_desc {
        const char *name;
        u16 dma_width;
        u16 offset;
    }

.. _`efx_hw_stat_desc.members`:

Members
-------

name
    Name of the statistic as visible through ethtool, or \ ``NULL``\  if
    it should not be exposed

dma_width
    Width in bits (0 for non-DMA statistics)

offset
    Offset within stats (ignored for non-DMA statistics)

.. _`efx_nic`:

struct efx_nic
==============

.. c:type:: struct efx_nic

    an Efx NIC

.. _`efx_nic.definition`:

Definition
----------

.. code-block:: c

    struct efx_nic {
        char name[IFNAMSIZ];
        struct list_head node;
        struct efx_nic *primary;
        struct list_head secondary_list;
        struct pci_dev *pci_dev;
        unsigned int port_num;
        const struct efx_nic_type *type;
        int legacy_irq;
        bool eeh_disabled_legacy_irq;
        struct workqueue_struct *workqueue;
        char workqueue_name[16];
        struct work_struct reset_work;
        resource_size_t membase_phys;
        void __iomem *membase;
        enum efx_int_mode interrupt_mode;
        unsigned int timer_quantum_ns;
        unsigned int timer_max_ns;
        bool irq_rx_adaptive;
        unsigned int irq_mod_step_us;
        unsigned int irq_rx_moderation_us;
        u32 msg_enable;
        enum nic_state state;
        unsigned long reset_pending;
        struct efx_channel *channel[EFX_MAX_CHANNELS];
        struct efx_msi_context msi_context[EFX_MAX_CHANNELS];
        const struct efx_channel_type * extra_channel_type[EFX_MAX_EXTRA_CHANNELS];
        unsigned rxq_entries;
        unsigned txq_entries;
        unsigned int txq_stop_thresh;
        unsigned int txq_wake_thresh;
        unsigned tx_dc_base;
        unsigned rx_dc_base;
        unsigned sram_lim_qw;
        unsigned next_buffer_table;
        unsigned int max_channels;
        unsigned int max_tx_channels;
        unsigned n_channels;
        unsigned n_rx_channels;
        unsigned rss_spread;
        unsigned tx_channel_offset;
        unsigned n_tx_channels;
        unsigned int rx_ip_align;
        unsigned int rx_dma_len;
        unsigned int rx_buffer_order;
        unsigned int rx_buffer_truesize;
        unsigned int rx_page_buf_step;
        unsigned int rx_bufs_per_page;
        unsigned int rx_pages_per_batch;
        unsigned int rx_prefix_size;
        int rx_packet_hash_offset;
        int rx_packet_len_offset;
        int rx_packet_ts_offset;
        u8 rx_hash_key[40];
        u32 rx_indir_table[128];
        bool rx_scatter;
        bool rss_active;
        bool rx_hash_udp_4tuple;
        unsigned int_error_count;
        unsigned long int_error_expire;
        bool irq_soft_enabled;
        struct efx_buffer irq_status;
        unsigned irq_zero_count;
        unsigned irq_level;
        struct delayed_work selftest_work;
    #ifdef CONFIG_SFC_MTD
        struct list_head mtd_list;
    #endif
        void *nic_data;
        struct efx_mcdi_data *mcdi;
        struct mutex mac_lock;
        struct work_struct mac_work;
        bool port_enabled;
        bool mc_bist_for_other_fn;
        bool port_initialized;
        struct net_device *net_dev;
        netdev_features_t fixed_features;
        struct efx_buffer stats_buffer;
        u64 rx_nodesc_drops_total;
        u64 rx_nodesc_drops_while_down;
        bool rx_nodesc_drops_prev_state;
        unsigned int phy_type;
        const struct efx_phy_operations *phy_op;
        void *phy_data;
        struct mdio_if_info mdio;
        unsigned int mdio_bus;
        enum efx_phy_mode phy_mode;
        u32 link_advertising;
        struct efx_link_state link_state;
        unsigned int n_link_state_changes;
        bool unicast_filter;
        union efx_multicast_hash multicast_hash;
        u8 wanted_fc;
        unsigned fc_disable;
        atomic_t rx_reset;
        enum efx_loopback_mode loopback_mode;
        u64 loopback_modes;
        void *loopback_selftest;
        struct rw_semaphore filter_sem;
        spinlock_t filter_lock;
        void *filter_state;
    #ifdef CONFIG_RFS_ACCEL
        unsigned int rps_expire_channel;
        unsigned int rps_expire_index;
    #endif
        atomic_t active_queues;
        atomic_t rxq_flush_pending;
        atomic_t rxq_flush_outstanding;
        wait_queue_head_t flush_wq;
    #ifdef CONFIG_SFC_SRIOV
        unsigned vf_count;
        unsigned vf_init_count;
        unsigned vi_scale;
    #endif
        struct efx_ptp_data *ptp_data;
        char *vpd_sn;
        struct delayed_work monitor_work ____cacheline_aligned_in_smp;
        spinlock_t biu_lock;
        int last_irq_cpu;
        spinlock_t stats_lock;
        atomic_t n_rx_noskb_drops;
    }

.. _`efx_nic.members`:

Members
-------

name
    Device name (net device name or bus id before net device registered)

node
    List node for maintaning primary/secondary function lists

primary
    &struct efx_nic instance for the primary function of this
    controller.  May be the same structure, and may be \ ``NULL``\  if no
    primary function is bound.  Serialised by rtnl_lock.

secondary_list
    List of \ :c:type:`struct efx_nic <efx_nic>`\  instances for the secondary PCI
    functions of the controller, if this is for the primary function.
    Serialised by rtnl_lock.

pci_dev
    The PCI device

port_num
    *undescribed*

type
    Controller type attributes

legacy_irq
    IRQ number

eeh_disabled_legacy_irq
    *undescribed*

workqueue
    Workqueue for port reconfigures and the HW monitor.
    Work items do not hold and must not acquire RTNL.

workqueue_name
    Name of workqueue

reset_work
    Scheduled reset workitem

membase_phys
    Memory BAR value as physical address

membase
    Memory BAR value

interrupt_mode
    Interrupt mode

timer_quantum_ns
    Interrupt timer quantum, in nanoseconds

timer_max_ns
    Interrupt timer maximum value, in nanoseconds

irq_rx_adaptive
    Adaptive IRQ moderation enabled for RX event queues

irq_mod_step_us
    *undescribed*

irq_rx_moderation_us
    IRQ moderation time for RX event queues

msg_enable
    Log message enable flags

state
    Device state number (%STATE\_\*). Serialised by the rtnl_lock.

reset_pending
    Bitmask for pending resets

channel
    Channels

msi_context
    Context for each MSI

extra_channel_type
    *undescribed*

rxq_entries
    Size of receive queues requested by user.

txq_entries
    Size of transmit queues requested by user.

txq_stop_thresh
    TX queue fill level at or above which we stop it.

txq_wake_thresh
    TX queue fill level at or below which we wake it.

tx_dc_base
    Base qword address in SRAM of TX queue descriptor caches

rx_dc_base
    Base qword address in SRAM of RX queue descriptor caches

sram_lim_qw
    Qword address limit of SRAM

next_buffer_table
    First available buffer table id

max_channels
    *undescribed*

max_tx_channels
    *undescribed*

n_channels
    Number of channels in use

n_rx_channels
    Number of channels used for RX (= number of RX queues)

rss_spread
    *undescribed*

tx_channel_offset
    *undescribed*

n_tx_channels
    Number of channels used for TX

rx_ip_align
    RX DMA address offset to have IP header aligned in
    in accordance with NET_IP_ALIGN

rx_dma_len
    Current maximum RX DMA length

rx_buffer_order
    Order (log2) of number of pages for each RX buffer

rx_buffer_truesize
    Amortised allocation size of an RX buffer,
    for use in sk_buff::truesize

rx_page_buf_step
    *undescribed*

rx_bufs_per_page
    *undescribed*

rx_pages_per_batch
    *undescribed*

rx_prefix_size
    Size of RX prefix before packet data

rx_packet_hash_offset
    Offset of RX flow hash from start of packet data
    (valid only if \ ``rx_prefix_size``\  != 0; always negative)

rx_packet_len_offset
    Offset of RX packet length from start of packet data
    (valid only for NICs that set \ ``EFX_RX_PKT_PREFIX_LEN``\ ; always negative)

rx_packet_ts_offset
    Offset of timestamp from start of packet data
    (valid only if channel->sync_timestamps_enabled; always negative)

rx_hash_key
    Toeplitz hash key for RSS

rx_indir_table
    Indirection table for RSS

rx_scatter
    Scatter mode enabled for receives

rss_active
    RSS enabled on hardware

rx_hash_udp_4tuple
    UDP 4-tuple hashing enabled

int_error_count
    Number of internal errors seen recently

int_error_expire
    Time at which error count will be expired

irq_soft_enabled
    Are IRQs soft-enabled? If not, IRQ handler will
    acknowledge but do nothing else.

irq_status
    Interrupt status buffer

irq_zero_count
    Number of legacy IRQs seen with queue flags == 0

irq_level
    IRQ level/index for IRQs not triggered by an event queue

selftest_work
    Work item for asynchronous self-test

mtd_list
    List of MTDs attached to the NIC

nic_data
    Hardware dependent state

mcdi
    Management-Controller-to-Driver Interface state

mac_lock
    MAC access lock. Protects \ ``port_enabled``\ , \ ``phy_mode``\ ,
    \ :c:func:`efx_monitor`\  and \ :c:func:`efx_reconfigure_port`\ 

mac_work
    Work item for changing MAC promiscuity and multicast hash

port_enabled
    Port enabled indicator.
    Serialises \ :c:func:`efx_stop_all`\ , \ :c:func:`efx_start_all`\ , \ :c:func:`efx_monitor`\  and
    \ :c:func:`efx_mac_work`\  with kernel interfaces. Safe to read under any
    one of the rtnl_lock, mac_lock, or netif_tx_lock, but all three must
    be held to modify it.

mc_bist_for_other_fn
    *undescribed*

port_initialized
    Port initialized?

net_dev
    Operating system network device. Consider holding the rtnl lock

fixed_features
    Features which cannot be turned off

stats_buffer
    DMA buffer for statistics

rx_nodesc_drops_total
    *undescribed*

rx_nodesc_drops_while_down
    *undescribed*

rx_nodesc_drops_prev_state
    *undescribed*

phy_type
    PHY type

phy_op
    PHY interface

phy_data
    PHY private data (including PHY-specific stats)

mdio
    PHY MDIO interface

mdio_bus
    PHY MDIO bus ID (only used by Siena)

phy_mode
    PHY operating mode. Serialised by \ ``mac_lock``\ .

link_advertising
    Autonegotiation advertising flags

link_state
    Current state of the link

n_link_state_changes
    Number of times the link has changed state

unicast_filter
    Flag for Falcon-arch simple unicast filter.
    Protected by \ ``mac_lock``\ .

multicast_hash
    Multicast hash table for Falcon-arch.
    Protected by \ ``mac_lock``\ .

wanted_fc
    Wanted flow control flags

fc_disable
    When non-zero flow control is disabled. Typically used to
    ensure that network back pressure doesn't delay dma queue flushes.
    Serialised by the rtnl lock.

rx_reset
    *undescribed*

loopback_mode
    Loopback status

loopback_modes
    Supported loopback mode bitmask

loopback_selftest
    Offline self-test private state

filter_sem
    Filter table rw_semaphore, for freeing the table

filter_lock
    Filter table lock, for mere content changes

filter_state
    Architecture-dependent filter table state

rps_expire_channel
    Next channel to check for expiry

rps_expire_index
    Next index to check for expiry in
    \ ``rps_expire_channel``\ 's \ ``rps_flow_id``\ 

active_queues
    Count of RX and TX queues that haven't been flushed and drained.

rxq_flush_pending
    Count of number of receive queues that need to be flushed.
    Decremented when the \ :c:func:`efx_flush_rx_queue`\  is called.

rxq_flush_outstanding
    Count of number of RX flushes started but not yet
    completed (either success or failure). Not used when MCDI is used to
    flush receive queues.

flush_wq
    wait queue used by \ :c:func:`efx_nic_flush_queues`\  to wait for flush completions.

vf_count
    Number of VFs intended to be enabled.

vf_init_count
    Number of VFs that have been fully initialised.

vi_scale
    log2 number of vnics per VF.

ptp_data
    PTP state data

vpd_sn
    Serial number read from VPD

____cacheline_aligned_in_smp
    *undescribed*

biu_lock
    BIU (bus interface unit) lock

last_irq_cpu
    Last CPU to handle a possible test interrupt.  This
    field is used by \ :c:func:`efx_test_interrupts`\  to verify that an
    interrupt has occurred.

stats_lock
    Statistics update lock. Must be held when calling
    efx_nic_type::{update,start,stop}_stats.

n_rx_noskb_drops
    Count of RX packets dropped due to failure to allocate an skb

.. _`efx_nic.description`:

Description
-----------

This is stored in the private area of the \ :c:type:`struct net_device <net_device>`\ .

.. _`efx_nic_type`:

struct efx_nic_type
===================

.. c:type:: struct efx_nic_type

    Efx device type definition

.. _`efx_nic_type.definition`:

Definition
----------

.. code-block:: c

    struct efx_nic_type {
        bool is_vf;
        unsigned int mem_bar;
        unsigned int (*mem_map_size)(struct efx_nic *efx);
        int (*probe)(struct efx_nic *efx);
        void (*remove)(struct efx_nic *efx);
        int (*init)(struct efx_nic *efx);
        int (*dimension_resources)(struct efx_nic *efx);
        void (*fini)(struct efx_nic *efx);
        void (*monitor)(struct efx_nic *efx);
        enum reset_type (*map_reset_reason)(enum reset_type reason);
        int (*map_reset_flags)(u32 *flags);
        int (*reset)(struct efx_nic *efx, enum reset_type method);
        int (*probe_port)(struct efx_nic *efx);
        void (*remove_port)(struct efx_nic *efx);
        bool (*handle_global_event)(struct efx_channel *channel, efx_qword_t *);
        int (*fini_dmaq)(struct efx_nic *efx);
        void (*prepare_flush)(struct efx_nic *efx);
        void (*finish_flush)(struct efx_nic *efx);
        void (*prepare_flr)(struct efx_nic *efx);
        void (*finish_flr)(struct efx_nic *efx);
        size_t (*describe_stats)(struct efx_nic *efx, u8 *names);
        size_t (*update_stats)(struct efx_nic *efx, u64 *full_stats, struct rtnl_link_stats64 *core_stats);
        void (*start_stats)(struct efx_nic *efx);
        void (*pull_stats)(struct efx_nic *efx);
        void (*stop_stats)(struct efx_nic *efx);
        void (*set_id_led)(struct efx_nic *efx, enum efx_led_mode mode);
        void (*push_irq_moderation)(struct efx_channel *channel);
        int (*reconfigure_port)(struct efx_nic *efx);
        void (*prepare_enable_fc_tx)(struct efx_nic *efx);
        int (*reconfigure_mac)(struct efx_nic *efx);
        bool (*check_mac_fault)(struct efx_nic *efx);
        void (*get_wol)(struct efx_nic *efx, struct ethtool_wolinfo *wol);
        int (*set_wol)(struct efx_nic *efx, u32 type);
        void (*resume_wol)(struct efx_nic *efx);
        int (*test_chip)(struct efx_nic *efx, struct efx_self_tests *tests);
        int (*test_nvram)(struct efx_nic *efx);
        void (*mcdi_request)(struct efx_nic *efx,const efx_dword_t *hdr, size_t hdr_len, const efx_dword_t *sdu, size_t sdu_len);
        bool (*mcdi_poll_response)(struct efx_nic *efx);
        void (*mcdi_read_response)(struct efx_nic *efx, efx_dword_t *pdu, size_t pdu_offset, size_t pdu_len);
        int (*mcdi_poll_reboot)(struct efx_nic *efx);
        void (*mcdi_reboot_detected)(struct efx_nic *efx);
        void (*irq_enable_master)(struct efx_nic *efx);
        int (*irq_test_generate)(struct efx_nic *efx);
        void (*irq_disable_non_ev)(struct efx_nic *efx);
        irqreturn_t (*irq_handle_msi)(int irq, void *dev_id);
        irqreturn_t (*irq_handle_legacy)(int irq, void *dev_id);
        int (*tx_probe)(struct efx_tx_queue *tx_queue);
        void (*tx_init)(struct efx_tx_queue *tx_queue);
        void (*tx_remove)(struct efx_tx_queue *tx_queue);
        void (*tx_write)(struct efx_tx_queue *tx_queue);
        unsigned int (*tx_limit_len)(struct efx_tx_queue *tx_queue, dma_addr_t dma_addr, unsigned int len);
        int (*rx_push_rss_config)(struct efx_nic *efx, bool user, const u32 *rx_indir_table, const u8 *key);
        int (*rx_pull_rss_config)(struct efx_nic *efx);
        int (*rx_probe)(struct efx_rx_queue *rx_queue);
        void (*rx_init)(struct efx_rx_queue *rx_queue);
        void (*rx_remove)(struct efx_rx_queue *rx_queue);
        void (*rx_write)(struct efx_rx_queue *rx_queue);
        void (*rx_defer_refill)(struct efx_rx_queue *rx_queue);
        int (*ev_probe)(struct efx_channel *channel);
        int (*ev_init)(struct efx_channel *channel);
        void (*ev_fini)(struct efx_channel *channel);
        void (*ev_remove)(struct efx_channel *channel);
        int (*ev_process)(struct efx_channel *channel, int quota);
        void (*ev_read_ack)(struct efx_channel *channel);
        void (*ev_test_generate)(struct efx_channel *channel);
        int (*filter_table_probe)(struct efx_nic *efx);
        void (*filter_table_restore)(struct efx_nic *efx);
        void (*filter_table_remove)(struct efx_nic *efx);
        void (*filter_update_rx_scatter)(struct efx_nic *efx);
        s32 (*filter_insert)(struct efx_nic *efx, struct efx_filter_spec *spec, bool replace);
        int (*filter_remove_safe)(struct efx_nic *efx,enum efx_filter_priority priority, u32 filter_id);
        int (*filter_get_safe)(struct efx_nic *efx,enum efx_filter_priority priority, u32 filter_id, struct efx_filter_spec *);
        int (*filter_clear_rx)(struct efx_nic *efx, enum efx_filter_priority priority);
        u32 (*filter_count_rx_used)(struct efx_nic *efx, enum efx_filter_priority priority);
        u32 (*filter_get_rx_id_limit)(struct efx_nic *efx);
        s32 (*filter_get_rx_ids)(struct efx_nic *efx,enum efx_filter_priority priority, u32 *buf, u32 size);
    #ifdef CONFIG_RFS_ACCEL
        s32 (*filter_rfs_insert)(struct efx_nic *efx, struct efx_filter_spec *spec);
        bool (*filter_rfs_expire_one)(struct efx_nic *efx, u32 flow_id, unsigned int index);
    #endif
    #ifdef CONFIG_SFC_MTD
        int (*mtd_probe)(struct efx_nic *efx);
        void (*mtd_rename)(struct efx_mtd_partition *part);
        int (*mtd_read)(struct mtd_info *mtd, loff_t start, size_t len, size_t *retlen, u8 *buffer);
        int (*mtd_erase)(struct mtd_info *mtd, loff_t start, size_t len);
        int (*mtd_write)(struct mtd_info *mtd, loff_t start, size_t len, size_t *retlen, const u8 *buffer);
        int (*mtd_sync)(struct mtd_info *mtd);
    #endif
        void (*ptp_write_host_time)(struct efx_nic *efx, u32 host_time);
        int (*ptp_set_ts_sync_events)(struct efx_nic *efx, bool en, bool temp);
        int (*ptp_set_ts_config)(struct efx_nic *efx, struct hwtstamp_config *init);
        int (*sriov_configure)(struct efx_nic *efx, int num_vfs);
        int (*vlan_rx_add_vid)(struct efx_nic *efx, __be16 proto, u16 vid);
        int (*vlan_rx_kill_vid)(struct efx_nic *efx, __be16 proto, u16 vid);
        int (*get_phys_port_id)(struct efx_nic *efx, struct netdev_phys_item_id *ppid);
        int (*sriov_init)(struct efx_nic *efx);
        void (*sriov_fini)(struct efx_nic *efx);
        bool (*sriov_wanted)(struct efx_nic *efx);
        void (*sriov_reset)(struct efx_nic *efx);
        void (*sriov_flr)(struct efx_nic *efx, unsigned vf_i);
        int (*sriov_set_vf_mac)(struct efx_nic *efx, int vf_i, u8 *mac);
        int (*sriov_set_vf_vlan)(struct efx_nic *efx, int vf_i, u16 vlan, u8 qos);
        int (*sriov_set_vf_spoofchk)(struct efx_nic *efx, int vf_i, bool spoofchk);
        int (*sriov_get_vf_config)(struct efx_nic *efx, int vf_i, struct ifla_vf_info *ivi);
        int (*sriov_set_vf_link_state)(struct efx_nic *efx, int vf_i, int link_state);
        int (*vswitching_probe)(struct efx_nic *efx);
        int (*vswitching_restore)(struct efx_nic *efx);
        void (*vswitching_remove)(struct efx_nic *efx);
        int (*get_mac_address)(struct efx_nic *efx, unsigned char *perm_addr);
        int (*set_mac_address)(struct efx_nic *efx);
        u32 (*tso_versions)(struct efx_nic *efx);
        int (*udp_tnl_push_ports)(struct efx_nic *efx);
        int (*udp_tnl_add_port)(struct efx_nic *efx, struct efx_udp_tunnel tnl);
        bool (*udp_tnl_has_port)(struct efx_nic *efx, __be16 port);
        int (*udp_tnl_del_port)(struct efx_nic *efx, struct efx_udp_tunnel tnl);
        int revision;
        unsigned int txd_ptr_tbl_base;
        unsigned int rxd_ptr_tbl_base;
        unsigned int buf_tbl_base;
        unsigned int evq_ptr_tbl_base;
        unsigned int evq_rptr_tbl_base;
        u64 max_dma_mask;
        unsigned int rx_prefix_size;
        unsigned int rx_hash_offset;
        unsigned int rx_ts_offset;
        unsigned int rx_buffer_padding;
        bool can_rx_scatter;
        bool always_rx_scatter;
        bool option_descriptors;
        unsigned int min_interrupt_mode;
        unsigned int max_interrupt_mode;
        unsigned int timer_period_max;
        netdev_features_t offload_features;
        int mcdi_max_ver;
        unsigned int max_rx_ip_filters;
        u32 hwtstamp_filters;
        unsigned int rx_hash_key_size;
    }

.. _`efx_nic_type.members`:

Members
-------

is_vf
    *undescribed*

mem_bar
    Get the memory BAR

mem_map_size
    Get memory BAR mapped size

probe
    Probe the controller

remove
    Free resources allocated by \ :c:func:`probe`\ 

init
    Initialise the controller

dimension_resources
    Dimension controller resources (buffer table,
    and VIs once the available interrupt resources are clear)

fini
    Shut down the controller

monitor
    Periodic function for polling link state and hardware monitor

map_reset_reason
    Map ethtool reset reason to a reset method

map_reset_flags
    Map ethtool reset flags to a reset method, if possible

reset
    Reset the controller hardware and possibly the PHY.  This will
    be called while the controller is uninitialised.

probe_port
    Probe the MAC and PHY

remove_port
    Free resources allocated by \ :c:func:`probe_port`\ 

handle_global_event
    Handle a "global" event (may be \ ``NULL``\ )

fini_dmaq
    Flush and finalise DMA queues (RX and TX queues)

prepare_flush
    Prepare the hardware for flushing the DMA queues
    (for Falcon architecture)

finish_flush
    Clean up after flushing the DMA queues (for Falcon
    architecture)

prepare_flr
    Prepare for an FLR

finish_flr
    Clean up after an FLR

describe_stats
    Describe statistics for ethtool

update_stats
    Update statistics not provided by event handling.
    Either argument may be \ ``NULL``\ .

start_stats
    Start the regular fetching of statistics

pull_stats
    Pull stats from the NIC and wait until they arrive.

stop_stats
    Stop the regular fetching of statistics

set_id_led
    Set state of identifying LED or revert to automatic function

push_irq_moderation
    Apply interrupt moderation value

reconfigure_port
    Push loopback/power/txdis changes to the MAC and PHY

prepare_enable_fc_tx
    Prepare MAC to enable pause frame TX (may be \ ``NULL``\ )

reconfigure_mac
    Push MAC address, MTU, flow control and filter settings
    to the hardware.  Serialised by the mac_lock.

check_mac_fault
    Check MAC fault state. True if fault present.

get_wol
    Get WoL configuration from driver state

set_wol
    Push WoL configuration to the NIC

resume_wol
    Synchronise WoL state between driver and MC (e.g. after resume)

test_chip
    Test registers.  May use \ :c:func:`efx_farch_test_registers`\ , and is
    expected to reset the NIC.

test_nvram
    Test validity of NVRAM contents

mcdi_request
    Send an MCDI request with the given header and SDU.
    The SDU length may be any value from 0 up to the protocol-
    defined maximum, but its buffer will be padded to a multiple
    of 4 bytes.

mcdi_poll_response
    Test whether an MCDI response is available.

mcdi_read_response
    Read the MCDI response PDU.  The offset will
    be a multiple of 4.  The length may not be, but the buffer
    will be padded so it is safe to round up.

mcdi_poll_reboot
    Test whether the MCDI has rebooted.  If so,
    return an appropriate error code for aborting any current
    request; otherwise return 0.

mcdi_reboot_detected
    *undescribed*

irq_enable_master
    Enable IRQs on the NIC.  Each event queue must
    be separately enabled after this.

irq_test_generate
    Generate a test IRQ

irq_disable_non_ev
    Disable non-event IRQs on the NIC.  Each event
    queue must be separately disabled before this.

irq_handle_msi
    Handle MSI for a channel.  The \ ``dev_id``\  argument is
    a pointer to the \ :c:type:`struct efx_msi_context <efx_msi_context>`\  for the channel.

irq_handle_legacy
    Handle legacy interrupt.  The \ ``dev_id``\  argument
    is a pointer to the \ :c:type:`struct efx_nic <efx_nic>`\ .

tx_probe
    Allocate resources for TX queue

tx_init
    Initialise TX queue on the NIC

tx_remove
    Free resources for TX queue

tx_write
    Write TX descriptors and doorbell

tx_limit_len
    *undescribed*

rx_push_rss_config
    Write RSS hash key and indirection table to the NIC

rx_pull_rss_config
    Read RSS hash key and indirection table back from the NIC

rx_probe
    Allocate resources for RX queue

rx_init
    Initialise RX queue on the NIC

rx_remove
    Free resources for RX queue

rx_write
    Write RX descriptors and doorbell

rx_defer_refill
    Generate a refill reminder event

ev_probe
    Allocate resources for event queue

ev_init
    Initialise event queue on the NIC

ev_fini
    Deinitialise event queue on the NIC

ev_remove
    Free resources for event queue

ev_process
    Process events for a queue, up to the given NAPI quota

ev_read_ack
    Acknowledge read events on a queue, rearming its IRQ

ev_test_generate
    Generate a test event

filter_table_probe
    Probe filter capabilities and set up filter software state

filter_table_restore
    Restore filters removed from hardware

filter_table_remove
    Remove filters from hardware and tear down software state

filter_update_rx_scatter
    Update filters after change to rx scatter setting

filter_insert
    add or replace a filter

filter_remove_safe
    remove a filter by ID, carefully

filter_get_safe
    retrieve a filter by ID, carefully

filter_clear_rx
    Remove all RX filters whose priority is less than or
    equal to the given priority and is not \ ``EFX_FILTER_PRI_AUTO``\ 

filter_count_rx_used
    Get the number of filters in use at a given priority

filter_get_rx_id_limit
    Get maximum value of a filter id, plus 1

filter_get_rx_ids
    Get list of RX filters at a given priority

filter_rfs_insert
    Add or replace a filter for RFS.  This must be
    atomic.  The hardware change may be asynchronous but should
    not be delayed for long.  It may fail if this can't be done
    atomically.

filter_rfs_expire_one
    Consider expiring a filter inserted for RFS.
    This must check whether the specified table entry is used by RFS
    and that \ :c:func:`rps_may_expire_flow`\  returns true for it.

mtd_probe
    Probe and add MTD partitions associated with this net device,
    using \ :c:func:`efx_mtd_add`\ 

mtd_rename
    Set an MTD partition name using the net device name

mtd_read
    Read from an MTD partition

mtd_erase
    Erase part of an MTD partition

mtd_write
    Write to an MTD partition

mtd_sync
    Wait for write-back to complete on MTD partition.  This
    also notifies the driver that a writer has finished using this
    partition.

ptp_write_host_time
    Send host time to MC as part of sync protocol

ptp_set_ts_sync_events
    Enable or disable sync events for inline RX
    timestamping, possibly only temporarily for the purposes of a reset.

ptp_set_ts_config
    Set hardware timestamp configuration.  The flags
    and tx_type will already have been validated but this operation
    must validate and update rx_filter.

sriov_configure
    *undescribed*

vlan_rx_add_vid
    *undescribed*

vlan_rx_kill_vid
    *undescribed*

get_phys_port_id
    Get the underlying physical port id.

sriov_init
    *undescribed*

sriov_fini
    *undescribed*

sriov_wanted
    *undescribed*

sriov_reset
    *undescribed*

sriov_flr
    *undescribed*

sriov_set_vf_mac
    *undescribed*

sriov_set_vf_vlan
    *undescribed*

sriov_set_vf_spoofchk
    *undescribed*

sriov_get_vf_config
    *undescribed*

sriov_set_vf_link_state
    *undescribed*

vswitching_probe
    *undescribed*

vswitching_restore
    *undescribed*

vswitching_remove
    *undescribed*

get_mac_address
    *undescribed*

set_mac_address
    Set the MAC address of the device

tso_versions
    Returns mask of firmware-assisted TSO versions supported.
    If \ ``NULL``\ , then device does not support any TSO version.

udp_tnl_push_ports
    Push the list of UDP tunnel ports to the NIC if required.

udp_tnl_add_port
    Add a UDP tunnel port

udp_tnl_has_port
    Check if a port has been added as UDP tunnel

udp_tnl_del_port
    Remove a UDP tunnel port

revision
    Hardware architecture revision

txd_ptr_tbl_base
    TX descriptor ring base address

rxd_ptr_tbl_base
    RX descriptor ring base address

buf_tbl_base
    Buffer table base address

evq_ptr_tbl_base
    Event queue pointer table base address

evq_rptr_tbl_base
    Event queue read-pointer table base address

max_dma_mask
    Maximum possible DMA mask

rx_prefix_size
    Size of RX prefix before packet data

rx_hash_offset
    Offset of RX flow hash within prefix

rx_ts_offset
    Offset of timestamp within prefix

rx_buffer_padding
    Size of padding at end of RX packet

can_rx_scatter
    NIC is able to scatter packets to multiple buffers

always_rx_scatter
    NIC will always scatter packets to multiple buffers

option_descriptors
    NIC supports TX option descriptors

min_interrupt_mode
    Lowest capability interrupt mode supported
    from \ :c:type:`enum efx_int_mode <efx_int_mode>`\ .

max_interrupt_mode
    Highest capability interrupt mode supported
    from \ :c:type:`enum efx_int_mode <efx_int_mode>`\ .

timer_period_max
    Maximum period of interrupt timer (in ticks)

offload_features
    net_device feature flags for protocol offload
    features implemented in hardware

mcdi_max_ver
    Maximum MCDI version supported

max_rx_ip_filters
    *undescribed*

hwtstamp_filters
    Mask of hardware timestamp filter types supported

rx_hash_key_size
    *undescribed*

.. _`efx_frame_pad`:

EFX_FRAME_PAD
=============

.. c:function::  EFX_FRAME_PAD()

    calculate maximum frame length

.. _`efx_frame_pad.description`:

Description
-----------

This calculates the maximum frame length that will be used for a
given MTU.  The frame length will be equal to the MTU plus a
constant amount of header space and padding.  This is the quantity
that the net driver will program into the MAC as the maximum frame
length.

The 10G MAC requires 8-byte alignment on the frame
length, so we round up to the nearest 8.

Re-clocking by the XGXS on RX can reduce an IPG to 32 bits (half an
XGMII cycle).  If the frame length reaches the maximum value in the
same cycle, the XMAC can miss the IPG altogether.  We work around
this by adding a further 16 bytes.

.. This file was automatic generated / don't edit.

