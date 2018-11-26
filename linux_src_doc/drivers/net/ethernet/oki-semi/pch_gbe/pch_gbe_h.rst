.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe.h

.. _`pch_gbe_mac_info`:

struct pch_gbe_mac_info
=======================

.. c:type:: struct pch_gbe_mac_info

    MAC information

.. _`pch_gbe_mac_info.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_mac_info {
        u8 addr[6];
        u8 fc;
        u8 fc_autoneg;
        u8 tx_fc_enable;
        u32 max_frame_size;
        u32 min_frame_size;
        u8 autoneg;
        u16 link_speed;
        u16 link_duplex;
    }

.. _`pch_gbe_mac_info.members`:

Members
-------

addr
    Store the MAC address

fc
    Mode of flow control

fc_autoneg
    Auto negotiation enable for flow control setting

tx_fc_enable
    Enable flag of Transmit flow control

max_frame_size
    Max transmit frame size

min_frame_size
    Min transmit frame size

autoneg
    Auto negotiation enable

link_speed
    Link speed

link_duplex
    Link duplex

.. _`pch_gbe_phy_info`:

struct pch_gbe_phy_info
=======================

.. c:type:: struct pch_gbe_phy_info

    PHY information

.. _`pch_gbe_phy_info.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_phy_info {
        u32 addr;
        u32 id;
        u32 revision;
        u32 reset_delay_us;
        u16 autoneg_advertised;
    }

.. _`pch_gbe_phy_info.members`:

Members
-------

addr
    PHY address

id
    PHY's identifier

revision
    PHY's revision

reset_delay_us
    HW reset delay time[us]

autoneg_advertised
    Autoneg advertised

.. _`pch_gbe_rx_desc`:

struct pch_gbe_rx_desc
======================

.. c:type:: struct pch_gbe_rx_desc

    Receive Descriptor

.. _`pch_gbe_rx_desc.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_rx_desc {
        u32 buffer_addr;
        u32 tcp_ip_status;
        u16 rx_words_eob;
        u16 gbec_status;
        u8 dma_status;
        u8 reserved1;
        u16 reserved2;
    }

.. _`pch_gbe_rx_desc.members`:

Members
-------

buffer_addr
    RX Frame Buffer Address

tcp_ip_status
    TCP/IP Accelerator Status

rx_words_eob
    RX word count and Byte position

gbec_status
    GMAC Status

dma_status
    DMA Status

reserved1
    Reserved

reserved2
    Reserved

.. _`pch_gbe_tx_desc`:

struct pch_gbe_tx_desc
======================

.. c:type:: struct pch_gbe_tx_desc

    Transmit Descriptor

.. _`pch_gbe_tx_desc.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_tx_desc {
        u32 buffer_addr;
        u16 length;
        u16 reserved1;
        u16 tx_words_eob;
        u16 tx_frame_ctrl;
        u8 dma_status;
        u8 reserved2;
        u16 gbec_status;
    }

.. _`pch_gbe_tx_desc.members`:

Members
-------

buffer_addr
    TX Frame Buffer Address

length
    Data buffer length

reserved1
    Reserved

tx_words_eob
    TX word count and Byte position

tx_frame_ctrl
    TX Frame Control

dma_status
    DMA Status

reserved2
    Reserved

gbec_status
    GMAC Status

.. _`pch_gbe_buffer`:

struct pch_gbe_buffer
=====================

.. c:type:: struct pch_gbe_buffer

    Buffer information

.. _`pch_gbe_buffer.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_buffer {
        struct sk_buff *skb;
        dma_addr_t dma;
        unsigned char *rx_buffer;
        unsigned long time_stamp;
        u16 length;
        bool mapped;
    }

.. _`pch_gbe_buffer.members`:

Members
-------

skb
    pointer to a socket buffer

dma
    DMA address

rx_buffer
    *undescribed*

time_stamp
    time stamp

length
    data size

mapped
    *undescribed*

.. _`pch_gbe_tx_ring`:

struct pch_gbe_tx_ring
======================

.. c:type:: struct pch_gbe_tx_ring

    tx ring information

.. _`pch_gbe_tx_ring.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_tx_ring {
        struct pch_gbe_tx_desc *desc;
        dma_addr_t dma;
        unsigned int size;
        unsigned int count;
        unsigned int next_to_use;
        unsigned int next_to_clean;
        struct pch_gbe_buffer *buffer_info;
    }

.. _`pch_gbe_tx_ring.members`:

Members
-------

desc
    pointer to the descriptor ring memory

dma
    physical address of the descriptor ring

size
    length of descriptor ring in bytes

count
    number of descriptors in the ring

next_to_use
    next descriptor to associate a buffer with

next_to_clean
    next descriptor to check for DD status bit

buffer_info
    array of buffer information structs

.. _`pch_gbe_rx_ring`:

struct pch_gbe_rx_ring
======================

.. c:type:: struct pch_gbe_rx_ring

    rx ring information

.. _`pch_gbe_rx_ring.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_rx_ring {
        struct pch_gbe_rx_desc *desc;
        dma_addr_t dma;
        unsigned char *rx_buff_pool;
        dma_addr_t rx_buff_pool_logic;
        unsigned int rx_buff_pool_size;
        unsigned int size;
        unsigned int count;
        unsigned int next_to_use;
        unsigned int next_to_clean;
        struct pch_gbe_buffer *buffer_info;
    }

.. _`pch_gbe_rx_ring.members`:

Members
-------

desc
    pointer to the descriptor ring memory

dma
    physical address of the descriptor ring

rx_buff_pool
    *undescribed*

rx_buff_pool_logic
    *undescribed*

rx_buff_pool_size
    *undescribed*

size
    length of descriptor ring in bytes

count
    number of descriptors in the ring

next_to_use
    next descriptor to associate a buffer with

next_to_clean
    next descriptor to check for DD status bit

buffer_info
    array of buffer information structs

.. _`pch_gbe_hw_stats`:

struct pch_gbe_hw_stats
=======================

.. c:type:: struct pch_gbe_hw_stats

    Statistics counters collected by the MAC

.. _`pch_gbe_hw_stats.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_hw_stats {
        u32 rx_packets;
        u32 tx_packets;
        u32 rx_bytes;
        u32 tx_bytes;
        u32 rx_errors;
        u32 tx_errors;
        u32 rx_dropped;
        u32 tx_dropped;
        u32 multicast;
        u32 collisions;
        u32 rx_crc_errors;
        u32 rx_frame_errors;
        u32 rx_alloc_buff_failed;
        u32 tx_length_errors;
        u32 tx_aborted_errors;
        u32 tx_carrier_errors;
        u32 tx_timeout_count;
        u32 tx_restart_count;
        u32 intr_rx_dsc_empty_count;
        u32 intr_rx_frame_err_count;
        u32 intr_rx_fifo_err_count;
        u32 intr_rx_dma_err_count;
        u32 intr_tx_fifo_err_count;
        u32 intr_tx_dma_err_count;
        u32 intr_tcpip_err_count;
    }

.. _`pch_gbe_hw_stats.members`:

Members
-------

rx_packets
    total packets received

tx_packets
    total packets transmitted

rx_bytes
    total bytes received

tx_bytes
    total bytes transmitted

rx_errors
    bad packets received

tx_errors
    packet transmit problems

rx_dropped
    no space in Linux buffers

tx_dropped
    no space available in Linux

multicast
    multicast packets received

collisions
    collisions

rx_crc_errors
    received packet with crc error

rx_frame_errors
    received frame alignment error

rx_alloc_buff_failed
    allocate failure of a receive buffer

tx_length_errors
    transmit length error

tx_aborted_errors
    transmit aborted error

tx_carrier_errors
    transmit carrier error

tx_timeout_count
    Number of transmit timeout

tx_restart_count
    Number of transmit restert

intr_rx_dsc_empty_count
    Interrupt count of receive descriptor empty

intr_rx_frame_err_count
    Interrupt count of receive frame error

intr_rx_fifo_err_count
    Interrupt count of receive FIFO error

intr_rx_dma_err_count
    Interrupt count of receive DMA error

intr_tx_fifo_err_count
    Interrupt count of transmit FIFO error

intr_tx_dma_err_count
    Interrupt count of transmit DMA error

intr_tcpip_err_count
    Interrupt count of TCP/IP Accelerator

.. _`pch_gbe_privdata`:

struct pch_gbe_privdata
=======================

.. c:type:: struct pch_gbe_privdata

    PCI Device ID driver data

.. _`pch_gbe_privdata.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_privdata {
        bool phy_tx_clk_delay;
        bool phy_disable_hibernate;
        int (*platform_init)(struct pci_dev *pdev);
    }

.. _`pch_gbe_privdata.members`:

Members
-------

phy_tx_clk_delay
    Bool, configure the PHY TX delay in software

phy_disable_hibernate
    Bool, disable PHY hibernation

platform_init
    Platform initialization callback, called from
    probe, prior to PHY initialization.

.. _`pch_gbe_adapter`:

struct pch_gbe_adapter
======================

.. c:type:: struct pch_gbe_adapter

    board specific private data structure

.. _`pch_gbe_adapter.definition`:

Definition
----------

.. code-block:: c

    struct pch_gbe_adapter {
        spinlock_t stats_lock;
        spinlock_t ethtool_lock;
        atomic_t irq_sem;
        struct net_device *netdev;
        struct pci_dev *pdev;
        int irq;
        struct net_device *polling_netdev;
        struct napi_struct napi;
        struct pch_gbe_hw hw;
        struct pch_gbe_hw_stats stats;
        struct work_struct reset_task;
        struct mii_if_info mii;
        struct timer_list watchdog_timer;
        u32 wake_up_evt;
        u32 *config_space;
        unsigned long led_status;
        struct pch_gbe_tx_ring *tx_ring;
        struct pch_gbe_rx_ring *rx_ring;
        unsigned long rx_buffer_len;
        unsigned long tx_queue_len;
        bool rx_stop_flag;
        int hwts_tx_en;
        int hwts_rx_en;
        struct pci_dev *ptp_pdev;
        struct pch_gbe_privdata *pdata;
    }

.. _`pch_gbe_adapter.members`:

Members
-------

stats_lock
    Spinlock structure for status

ethtool_lock
    Spinlock structure for ethtool

irq_sem
    Semaphore for interrupt

netdev
    Pointer of network device structure

pdev
    Pointer of pci device structure

irq
    *undescribed*

polling_netdev
    Pointer of polling network device structure

napi
    NAPI structure

hw
    Pointer of hardware structure

stats
    Hardware status

reset_task
    Reset task

mii
    MII information structure

watchdog_timer
    Watchdog timer list

wake_up_evt
    Wake up event

config_space
    Configuration space

led_status
    LED status

tx_ring
    Pointer of Tx descriptor ring structure

rx_ring
    Pointer of Rx descriptor ring structure

rx_buffer_len
    Receive buffer length

tx_queue_len
    Transmit queue length

rx_stop_flag
    *undescribed*

hwts_tx_en
    *undescribed*

hwts_rx_en
    *undescribed*

ptp_pdev
    *undescribed*

pdata
    *undescribed*

.. This file was automatic generated / don't edit.

