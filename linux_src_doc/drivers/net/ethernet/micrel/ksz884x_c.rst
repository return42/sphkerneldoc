.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/micrel/ksz884x.c

.. _`pr_fmt`:

pr_fmt
======

.. c:function::  pr_fmt( fmt)

    Micrel KSZ8841/2 PCI Ethernet driver

    :param  fmt:
        *undescribed*

.. _`pr_fmt.description`:

Description
-----------

Copyright (c) 2009-2010 Micrel, Inc.
Tristram Ha <Tristram.Ha@micrel.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

.. _`ksz_hw_desc`:

struct ksz_hw_desc
==================

.. c:type:: struct ksz_hw_desc

    Hardware descriptor data structure

.. _`ksz_hw_desc.definition`:

Definition
----------

.. code-block:: c

    struct ksz_hw_desc {
        union desc_stat ctrl;
        union desc_buf buf;
        u32 addr;
        u32 next;
    }

.. _`ksz_hw_desc.members`:

Members
-------

ctrl
    Descriptor control value.

buf
    Descriptor buffer value.

addr
    Physical address of memory buffer.

next
    Pointer to next hardware descriptor.

.. _`ksz_sw_desc`:

struct ksz_sw_desc
==================

.. c:type:: struct ksz_sw_desc

    Software descriptor data structure

.. _`ksz_sw_desc.definition`:

Definition
----------

.. code-block:: c

    struct ksz_sw_desc {
        union desc_stat ctrl;
        union desc_buf buf;
        u32 buf_size;
    }

.. _`ksz_sw_desc.members`:

Members
-------

ctrl
    Descriptor control value.

buf
    Descriptor buffer value.

buf_size
    Current buffers size value in hardware descriptor.

.. _`ksz_dma_buf`:

struct ksz_dma_buf
==================

.. c:type:: struct ksz_dma_buf

    OS dependent DMA buffer data structure

.. _`ksz_dma_buf.definition`:

Definition
----------

.. code-block:: c

    struct ksz_dma_buf {
        struct sk_buff *skb;
        dma_addr_t dma;
        int len;
    }

.. _`ksz_dma_buf.members`:

Members
-------

skb
    Associated socket buffer.

dma
    Associated physical DMA address.

len
    *undescribed*

.. _`ksz_dma_buf.len`:

len
---

Actual len used.

.. _`ksz_desc`:

struct ksz_desc
===============

.. c:type:: struct ksz_desc

    Descriptor structure

.. _`ksz_desc.definition`:

Definition
----------

.. code-block:: c

    struct ksz_desc {
        struct ksz_hw_desc *phw;
        struct ksz_sw_desc sw;
        struct ksz_dma_buf dma_buf;
    }

.. _`ksz_desc.members`:

Members
-------

phw
    Hardware descriptor pointer to uncached physical memory.

sw
    Cached memory to hold hardware descriptor values for
    manipulation.

dma_buf
    Operating system dependent data structure to hold physical
    memory buffer allocation information.

.. _`ksz_desc_info`:

struct ksz_desc_info
====================

.. c:type:: struct ksz_desc_info

    Descriptor information data structure

.. _`ksz_desc_info.definition`:

Definition
----------

.. code-block:: c

    struct ksz_desc_info {
        struct ksz_desc *ring;
        struct ksz_desc *cur;
        struct ksz_hw_desc *ring_virt;
        u32 ring_phys;
        int size;
        int alloc;
        int avail;
        int last;
        int next;
        int mask;
    }

.. _`ksz_desc_info.members`:

Members
-------

ring
    First descriptor in the ring.

cur
    Current descriptor being manipulated.

ring_virt
    First hardware descriptor in the ring.

ring_phys
    The physical address of the first descriptor of the ring.

size
    Size of hardware descriptor.

alloc
    Number of descriptors allocated.

avail
    Number of descriptors available for use.

last
    Index for last descriptor released to hardware.

next
    Index for next descriptor available for use.

mask
    Mask for index wrapping.

.. _`ksz_mac_table`:

struct ksz_mac_table
====================

.. c:type:: struct ksz_mac_table

    Static MAC table data structure

.. _`ksz_mac_table.definition`:

Definition
----------

.. code-block:: c

    struct ksz_mac_table {
        u8 mac_addr[ETH_ALEN];
        u16 vid;
        u8 fid;
        u8 ports;
        u8 override:1;
        u8 use_fid:1;
        u8 valid:1;
    }

.. _`ksz_mac_table.members`:

Members
-------

mac_addr
    MAC address to filter.

vid
    VID value.

fid
    FID value.

ports
    Port membership.

override
    Override setting.

use_fid
    FID use setting.

valid
    Valid setting indicating the entry is being used.

.. _`ksz_vlan_table`:

struct ksz_vlan_table
=====================

.. c:type:: struct ksz_vlan_table

    VLAN table data structure

.. _`ksz_vlan_table.definition`:

Definition
----------

.. code-block:: c

    struct ksz_vlan_table {
        u16 vid;
        u8 fid;
        u8 member;
    }

.. _`ksz_vlan_table.members`:

Members
-------

vid
    VID value.

fid
    FID value.

member
    Port membership.

.. _`ksz_port_mib`:

struct ksz_port_mib
===================

.. c:type:: struct ksz_port_mib

    Port MIB data structure

.. _`ksz_port_mib.definition`:

Definition
----------

.. code-block:: c

    struct ksz_port_mib {
        u8 cnt_ptr;
        u8 link_down;
        u8 state;
        u8 mib_start;
        u64 counter[TOTAL_PORT_COUNTER_NUM];
        u32 dropped[2];
    }

.. _`ksz_port_mib.members`:

Members
-------

cnt_ptr
    Current pointer to MIB counter index.

link_down
    Indication the link has just gone down.

state
    Connection status of the port.

mib_start
    The starting counter index.  Some ports do not start at 0.

counter
    64-bit MIB counter value.

dropped
    Temporary buffer to remember last read packet dropped values.

.. _`ksz_port_mib.description`:

Description
-----------

MIB counters needs to be read periodically so that counters do not get
overflowed and give incorrect values.  A right balance is needed to
satisfy this condition and not waste too much CPU time.

It is pointless to read MIB counters when the port is disconnected.  The
\ ``state``\  provides the connection status so that MIB counters are read only
when the port is connected.  The \ ``link_down``\  indicates the port is just
disconnected so that all MIB counters are read one last time to update the
information.

.. _`ksz_port_cfg`:

struct ksz_port_cfg
===================

.. c:type:: struct ksz_port_cfg

    Port configuration data structure

.. _`ksz_port_cfg.definition`:

Definition
----------

.. code-block:: c

    struct ksz_port_cfg {
        u16 vid;
        u8 member;
        u8 port_prio;
        u32 rx_rate[PRIO_QUEUES];
        u32 tx_rate[PRIO_QUEUES];
        int stp_state;
    }

.. _`ksz_port_cfg.members`:

Members
-------

vid
    VID value.

member
    Port membership.

port_prio
    Port priority.

rx_rate
    Receive priority rate.

tx_rate
    Transmit priority rate.

stp_state
    Current Spanning Tree Protocol state.

.. _`ksz_switch`:

struct ksz_switch
=================

.. c:type:: struct ksz_switch

    KSZ8842 switch data structure

.. _`ksz_switch.definition`:

Definition
----------

.. code-block:: c

    struct ksz_switch {
        struct ksz_mac_table mac_table[STATIC_MAC_TABLE_ENTRIES];
        struct ksz_vlan_table vlan_table[VLAN_TABLE_ENTRIES];
        struct ksz_port_cfg port_cfg[TOTAL_PORT_NUM];
        u8 diffserv[DIFFSERV_ENTRIES];
        u8 p_802_1p[PRIO_802_1P_ENTRIES];
        u8 br_addr[ETH_ALEN];
        u8 other_addr[ETH_ALEN];
        u8 broad_per;
        u8 member;
    }

.. _`ksz_switch.members`:

Members
-------

mac_table
    MAC table entries information.

vlan_table
    VLAN table entries information.

port_cfg
    Port configuration information.

diffserv
    DiffServ priority settings.  Possible values from 6-bit of ToS
    (bit7 ~ bit2) field.

p_802_1p
    802.1P priority settings.  Possible values from 3-bit of 802.1p
    Tag priority field.

br_addr
    Bridge address.  Used for STP.

other_addr
    Other MAC address.  Used for multiple network device mode.

broad_per
    Broadcast storm percentage.

member
    Current port membership.  Used for STP.

.. _`ksz_port_info`:

struct ksz_port_info
====================

.. c:type:: struct ksz_port_info

    Port information data structure

.. _`ksz_port_info.definition`:

Definition
----------

.. code-block:: c

    struct ksz_port_info {
        uint state;
        uint tx_rate;
        u8 duplex;
        u8 advertised;
        u8 partner;
        u8 port_id;
        void *pdev;
    }

.. _`ksz_port_info.members`:

Members
-------

state
    Connection status of the port.

tx_rate
    Transmit rate divided by 10000 to get Mbit.

duplex
    Duplex mode.

advertised
    Advertised auto-negotiation setting.  Used to determine link.

partner
    Auto-negotiation partner setting.  Used to determine link.

port_id
    Port index to access actual hardware register.

pdev
    Pointer to OS dependent network device.

.. _`ksz_hw`:

struct ksz_hw
=============

.. c:type:: struct ksz_hw

    KSZ884X hardware data structure

.. _`ksz_hw.definition`:

Definition
----------

.. code-block:: c

    struct ksz_hw {
        void __iomem *io;
        struct ksz_switch *ksz_switch;
        struct ksz_port_info port_info[SWITCH_PORT_NUM];
        struct ksz_port_mib port_mib[TOTAL_PORT_NUM];
        int dev_count;
        int dst_ports;
        int id;
        int mib_cnt;
        int mib_port_cnt;
        u32 tx_cfg;
        u32 rx_cfg;
        u32 intr_mask;
        u32 intr_set;
        uint intr_blocked;
        struct ksz_desc_info rx_desc_info;
        struct ksz_desc_info tx_desc_info;
        int tx_int_cnt;
        int tx_int_mask;
        int tx_size;
        u8 perm_addr[ETH_ALEN];
        u8 override_addr[ETH_ALEN];
        u8 address[ADDITIONAL_ENTRIES][ETH_ALEN];
        u8 addr_list_size;
        u8 mac_override;
        u8 promiscuous;
        u8 all_multi;
        u8 multi_list[MAX_MULTICAST_LIST][ETH_ALEN];
        u8 multi_bits[HW_MULTICAST_SIZE];
        u8 multi_list_size;
        u8 enabled;
        u8 rx_stop;
        u8 reserved2[1];
        uint features;
        uint overrides;
        void *parent;
    }

.. _`ksz_hw.members`:

Members
-------

io
    Virtual address assigned.

ksz_switch
    Pointer to KSZ8842 switch.

port_info
    Port information.

port_mib
    Port MIB information.

dev_count
    Number of network devices this hardware supports.

dst_ports
    Destination ports in switch for transmission.

id
    Hardware ID.  Used for display only.

mib_cnt
    Number of MIB counters this hardware has.

mib_port_cnt
    Number of ports with MIB counters.

tx_cfg
    Cached transmit control settings.

rx_cfg
    Cached receive control settings.

intr_mask
    Current interrupt mask.

intr_set
    Current interrup set.

intr_blocked
    Interrupt blocked.

rx_desc_info
    Receive descriptor information.

tx_desc_info
    Transmit descriptor information.

tx_int_cnt
    Transmit interrupt count.  Used for TX optimization.

tx_int_mask
    Transmit interrupt mask.  Used for TX optimization.

tx_size
    Transmit data size.  Used for TX optimization.
    The maximum is defined by MAX_TX_HELD_SIZE.

perm_addr
    Permanent MAC address.

override_addr
    Overridden MAC address.

address
    Additional MAC address entries.

addr_list_size
    Additional MAC address list size.

mac_override
    Indication of MAC address overridden.

promiscuous
    Counter to keep track of promiscuous mode set.

all_multi
    Counter to keep track of all multicast mode set.

multi_list
    Multicast address entries.

multi_bits
    Cached multicast hash table settings.

multi_list_size
    Multicast address list size.

enabled
    Indication of hardware enabled.

rx_stop
    Indication of receive process stop.

features
    Hardware features to enable.

overrides
    Hardware features to override.

parent
    Pointer to parent, network device private structure.

.. _`ksz_port`:

struct ksz_port
===============

.. c:type:: struct ksz_port

    Virtual port data structure

.. _`ksz_port.definition`:

Definition
----------

.. code-block:: c

    struct ksz_port {
        u8 duplex;
        u8 speed;
        u8 force_link;
        u8 flow_ctrl;
        int first_port;
        int mib_port_cnt;
        int port_cnt;
        u64 counter[OID_COUNTER_LAST];
        struct ksz_hw *hw;
        struct ksz_port_info *linked;
    }

.. _`ksz_port.members`:

Members
-------

duplex
    Duplex mode setting.  1 for half duplex, 2 for full
    duplex, and 0 for auto, which normally results in full
    duplex.

speed
    Speed setting.  10 for 10 Mbit, 100 for 100 Mbit, and
    0 for auto, which normally results in 100 Mbit.

force_link
    Force link setting.  0 for auto-negotiation, and 1 for
    force.

flow_ctrl
    Flow control setting.  PHY_NO_FLOW_CTRL for no flow
    control, and PHY_FLOW_CTRL for flow control.
    PHY_TX_ONLY and PHY_RX_ONLY are not supported for 100
    Mbit PHY.

first_port
    Index of first port this port supports.

mib_port_cnt
    Number of ports with MIB counters.

port_cnt
    Number of ports this port supports.

counter
    Port statistics counter.

hw
    Pointer to hardware structure.

linked
    Pointer to port information linked to this port.

.. _`ksz_timer_info`:

struct ksz_timer_info
=====================

.. c:type:: struct ksz_timer_info

    Timer information data structure

.. _`ksz_timer_info.definition`:

Definition
----------

.. code-block:: c

    struct ksz_timer_info {
        struct timer_list timer;
        int cnt;
        int max;
        int period;
    }

.. _`ksz_timer_info.members`:

Members
-------

timer
    Kernel timer.

cnt
    Running timer counter.

max
    Number of times to run timer; -1 for infinity.

period
    Timer period in jiffies.

.. _`ksz_shared_mem`:

struct ksz_shared_mem
=====================

.. c:type:: struct ksz_shared_mem

    OS dependent shared memory data structure

.. _`ksz_shared_mem.definition`:

Definition
----------

.. code-block:: c

    struct ksz_shared_mem {
        dma_addr_t dma_addr;
        uint alloc_size;
        uint phys;
        u8 *alloc_virt;
        u8 *virt;
    }

.. _`ksz_shared_mem.members`:

Members
-------

dma_addr
    Physical DMA address allocated.

alloc_size
    Allocation size.

phys
    Actual physical address used.

alloc_virt
    Virtual address allocated.

virt
    Actual virtual address used.

.. _`ksz_counter_info`:

struct ksz_counter_info
=======================

.. c:type:: struct ksz_counter_info

    OS dependent counter information data structure

.. _`ksz_counter_info.definition`:

Definition
----------

.. code-block:: c

    struct ksz_counter_info {
        wait_queue_head_t counter;
        unsigned long time;
        int read;
    }

.. _`ksz_counter_info.members`:

Members
-------

counter
    Wait queue to wakeup after counters are read.

time
    Next time in jiffies to read counter.

read
    Indication of counters read in full or not.

.. _`dev_info`:

struct dev_info
===============

.. c:type:: struct dev_info

    Network device information data structure

.. _`dev_info.definition`:

Definition
----------

.. code-block:: c

    struct dev_info {
        struct net_device *dev;
        struct pci_dev *pdev;
        struct ksz_hw hw;
        struct ksz_shared_mem desc_pool;
        spinlock_t hwlock;
        struct mutex lock;
        int (*dev_rcv)(struct dev_info *);
        struct sk_buff *last_skb;
        int skb_index;
        int skb_len;
        struct work_struct mib_read;
        struct ksz_timer_info mib_timer_info;
        struct ksz_counter_info counter[TOTAL_PORT_NUM];
        int mtu;
        int opened;
        struct tasklet_struct rx_tasklet;
        struct tasklet_struct tx_tasklet;
        int wol_enable;
        int wol_support;
        unsigned long pme_wait;
    }

.. _`dev_info.members`:

Members
-------

dev
    Pointer to network device.

pdev
    Pointer to PCI device.

hw
    Hardware structure.

desc_pool
    Physical memory used for descriptor pool.

hwlock
    Spinlock to prevent hardware from accessing.

lock
    Mutex lock to prevent device from accessing.

dev_rcv
    Receive process function used.

last_skb
    Socket buffer allocated for descriptor rx fragments.

skb_index
    Buffer index for receiving fragments.

skb_len
    Buffer length for receiving fragments.

mib_read
    Workqueue to read MIB counters.

mib_timer_info
    Timer to read MIB counters.

counter
    Used for MIB reading.

mtu
    Current MTU used.  The default is REGULAR_RX_BUF_SIZE;
    the maximum is MAX_RX_BUF_SIZE.

opened
    Counter to keep track of device open.

rx_tasklet
    Receive processing tasklet.

tx_tasklet
    Transmit processing tasklet.

wol_enable
    Wake-on-LAN enable set by ethtool.

wol_support
    Wake-on-LAN support used by ethtool.

pme_wait
    Used for KSZ8841 power management.

.. _`dev_priv`:

struct dev_priv
===============

.. c:type:: struct dev_priv

    Network device private data structure

.. _`dev_priv.definition`:

Definition
----------

.. code-block:: c

    struct dev_priv {
        struct dev_info *adapter;
        struct ksz_port port;
        struct ksz_timer_info monitor_timer_info;
        struct semaphore proc_sem;
        int id;
        struct mii_if_info mii_if;
        u32 advertising;
        u32 msg_enable;
        int media_state;
        int multicast;
        int promiscuous;
    }

.. _`dev_priv.members`:

Members
-------

adapter
    Adapter device information.

port
    Port information.

monitor_timer_info
    *undescribed*

proc_sem
    Semaphore for proc accessing.

id
    Device ID.

mii_if
    MII interface information.

advertising
    Temporary variable to store advertised settings.

msg_enable
    The message flags controlling driver output.

media_state
    The connection status of the device.

multicast
    The all multicast state of the device.

promiscuous
    The promiscuous state of the device.

.. _`hw_turn_on_intr`:

hw_turn_on_intr
===============

.. c:function:: void hw_turn_on_intr(struct ksz_hw *hw, u32 bit)

    turn on specified interrupts

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u32 bit:
        The interrupt bits to be on.

.. _`hw_turn_on_intr.description`:

Description
-----------

This routine turns on the specified interrupts in the interrupt mask so that
those interrupts will be enabled.

.. _`hw_block_intr`:

hw_block_intr
=============

.. c:function:: uint hw_block_intr(struct ksz_hw *hw)

    block hardware interrupts

    :param struct ksz_hw \*hw:
        *undescribed*

.. _`hw_block_intr.description`:

Description
-----------

This function blocks all interrupts of the hardware and returns the current
interrupt enable mask so that interrupts can be restored later.

Return the current interrupt enable mask.

.. _`sw_r_table`:

sw_r_table
==========

.. c:function:: void sw_r_table(struct ksz_hw *hw, int table, u16 addr, u32 *data)

    read 4 bytes of data from switch table

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int table:
        The table selector.

    :param u16 addr:
        The address of the table entry.

    :param u32 \*data:
        Buffer to store the read data.

.. _`sw_r_table.description`:

Description
-----------

This routine reads 4 bytes of data from the table of the switch.
Hardware interrupts are disabled to minimize corruption of read data.

.. _`sw_w_table_64`:

sw_w_table_64
=============

.. c:function:: void sw_w_table_64(struct ksz_hw *hw, int table, u16 addr, u32 data_hi, u32 data_lo)

    write 8 bytes of data to the switch table

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int table:
        The table selector.

    :param u16 addr:
        The address of the table entry.

    :param u32 data_hi:
        The high part of data to be written (bit63 ~ bit32).

    :param u32 data_lo:
        The low part of data to be written (bit31 ~ bit0).

.. _`sw_w_table_64.description`:

Description
-----------

This routine writes 8 bytes of data to the table of the switch.
Hardware interrupts are disabled to minimize corruption of written data.

.. _`sw_w_sta_mac_table`:

sw_w_sta_mac_table
==================

.. c:function:: void sw_w_sta_mac_table(struct ksz_hw *hw, u16 addr, u8 *mac_addr, u8 ports, int override, int valid, int use_fid, u8 fid)

    write to the static MAC table

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u16 addr:
        The address of the table entry.

    :param u8 \*mac_addr:
        The MAC address.

    :param u8 ports:
        The port members.

    :param int override:
        The flag to override the port receive/transmit settings.

    :param int valid:
        The flag to indicate entry is valid.

    :param int use_fid:
        The flag to indicate the FID is valid.

    :param u8 fid:
        The FID value.

.. _`sw_w_sta_mac_table.description`:

Description
-----------

This routine writes an entry of the static MAC table of the switch.  It
calls \ :c:func:`sw_w_table_64`\  to write the data.

.. _`sw_r_vlan_table`:

sw_r_vlan_table
===============

.. c:function:: int sw_r_vlan_table(struct ksz_hw *hw, u16 addr, u16 *vid, u8 *fid, u8 *member)

    read from the VLAN table

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u16 addr:
        The address of the table entry.

    :param u16 \*vid:
        Buffer to store the VID.

    :param u8 \*fid:
        Buffer to store the VID.

    :param u8 \*member:
        Buffer to store the port membership.

.. _`sw_r_vlan_table.description`:

Description
-----------

This function reads an entry of the VLAN table of the switch.  It calls
\ :c:func:`sw_r_table`\  to get the data.

Return 0 if the entry is valid; otherwise -1.

.. _`port_r_mib_cnt`:

port_r_mib_cnt
==============

.. c:function:: void port_r_mib_cnt(struct ksz_hw *hw, int port, u16 addr, u64 *cnt)

    read MIB counter

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u16 addr:
        The address of the counter.

    :param u64 \*cnt:
        Buffer to store the counter.

.. _`port_r_mib_cnt.description`:

Description
-----------

This routine reads a MIB counter of the port.
Hardware interrupts are disabled to minimize corruption of read data.

.. _`port_r_mib_pkt`:

port_r_mib_pkt
==============

.. c:function:: void port_r_mib_pkt(struct ksz_hw *hw, int port, u32 *last, u64 *cnt)

    read dropped packet counts

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u32 \*last:
        *undescribed*

    :param u64 \*cnt:
        Buffer to store the receive and transmit dropped packet counts.

.. _`port_r_mib_pkt.description`:

Description
-----------

This routine reads the dropped packet counts of the port.
Hardware interrupts are disabled to minimize corruption of read data.

.. _`port_r_cnt`:

port_r_cnt
==========

.. c:function:: int port_r_cnt(struct ksz_hw *hw, int port)

    read MIB counters periodically

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`port_r_cnt.description`:

Description
-----------

This routine is used to read the counters of the port periodically to avoid
counter overflow.  The hardware should be acquired first before calling this
routine.

Return non-zero when not all counters not read.

.. _`port_init_cnt`:

port_init_cnt
=============

.. c:function:: void port_init_cnt(struct ksz_hw *hw, int port)

    initialize MIB counter values

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`port_init_cnt.description`:

Description
-----------

This routine is used to initialize all counters to zero if the hardware
cannot do it after reset.

.. _`port_chk`:

port_chk
========

.. c:function:: int port_chk(struct ksz_hw *hw, int port, int offset, u16 bits)

    check port register bits

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int offset:
        The offset of the port register.

    :param u16 bits:
        The data bits to check.

.. _`port_chk.description`:

Description
-----------

This function checks whether the specified bits of the port register are set
or not.

Return 0 if the bits are not set.

.. _`port_cfg`:

port_cfg
========

.. c:function:: void port_cfg(struct ksz_hw *hw, int port, int offset, u16 bits, int set)

    set port register bits

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int offset:
        The offset of the port register.

    :param u16 bits:
        The data bits to set.

    :param int set:
        The flag indicating whether the bits are to be set or not.

.. _`port_cfg.description`:

Description
-----------

This routine sets or resets the specified bits of the port register.

.. _`port_chk_shift`:

port_chk_shift
==============

.. c:function:: int port_chk_shift(struct ksz_hw *hw, int port, u32 addr, int shift)

    check port bit

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u32 addr:
        *undescribed*

    :param int shift:
        Number of bits to shift.

.. _`port_chk_shift.description`:

Description
-----------

This function checks whether the specified port is set in the register or
not.

Return 0 if the port is not set.

.. _`port_cfg_shift`:

port_cfg_shift
==============

.. c:function:: void port_cfg_shift(struct ksz_hw *hw, int port, u32 addr, int shift, int set)

    set port bit

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u32 addr:
        *undescribed*

    :param int shift:
        Number of bits to shift.

    :param int set:
        The flag indicating whether the port is to be set or not.

.. _`port_cfg_shift.description`:

Description
-----------

This routine sets or resets the specified port in the register.

.. _`port_r8`:

port_r8
=======

.. c:function:: void port_r8(struct ksz_hw *hw, int port, int offset, u8 *data)

    read byte from port register

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int offset:
        The offset of the port register.

    :param u8 \*data:
        Buffer to store the data.

.. _`port_r8.description`:

Description
-----------

This routine reads a byte from the port register.

.. _`port_r16`:

port_r16
========

.. c:function:: void port_r16(struct ksz_hw *hw, int port, int offset, u16 *data)

    read word from port register.

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int offset:
        The offset of the port register.

    :param u16 \*data:
        Buffer to store the data.

.. _`port_r16.description`:

Description
-----------

This routine reads a word from the port register.

.. _`port_w16`:

port_w16
========

.. c:function:: void port_w16(struct ksz_hw *hw, int port, int offset, u16 data)

    write word to port register.

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int offset:
        The offset of the port register.

    :param u16 data:
        Data to write.

.. _`port_w16.description`:

Description
-----------

This routine writes a word to the port register.

.. _`sw_chk`:

sw_chk
======

.. c:function:: int sw_chk(struct ksz_hw *hw, u32 addr, u16 bits)

    check switch register bits

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u32 addr:
        The address of the switch register.

    :param u16 bits:
        The data bits to check.

.. _`sw_chk.description`:

Description
-----------

This function checks whether the specified bits of the switch register are
set or not.

Return 0 if the bits are not set.

.. _`sw_cfg`:

sw_cfg
======

.. c:function:: void sw_cfg(struct ksz_hw *hw, u32 addr, u16 bits, int set)

    set switch register bits

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u32 addr:
        The address of the switch register.

    :param u16 bits:
        The data bits to set.

    :param int set:
        The flag indicating whether the bits are to be set or not.

.. _`sw_cfg.description`:

Description
-----------

This function sets or resets the specified bits of the switch register.

.. _`sw_cfg_broad_storm`:

sw_cfg_broad_storm
==================

.. c:function:: void sw_cfg_broad_storm(struct ksz_hw *hw, u8 percent)

    configure broadcast storm threshold

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 percent:
        Broadcast storm threshold in percent of transmit rate.

.. _`sw_cfg_broad_storm.description`:

Description
-----------

This routine configures the broadcast storm threshold of the switch.

.. _`sw_get_broad_storm`:

sw_get_broad_storm
==================

.. c:function:: void sw_get_broad_storm(struct ksz_hw *hw, u8 *percent)

    get broadcast storm threshold

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 \*percent:
        Buffer to store the broadcast storm threshold percentage.

.. _`sw_get_broad_storm.description`:

Description
-----------

This routine retrieves the broadcast storm threshold of the switch.

.. _`sw_dis_broad_storm`:

sw_dis_broad_storm
==================

.. c:function:: void sw_dis_broad_storm(struct ksz_hw *hw, int port)

    disable broadstorm

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`sw_dis_broad_storm.description`:

Description
-----------

This routine disables the broadcast storm limit function of the switch.

.. _`sw_ena_broad_storm`:

sw_ena_broad_storm
==================

.. c:function:: void sw_ena_broad_storm(struct ksz_hw *hw, int port)

    enable broadcast storm

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`sw_ena_broad_storm.description`:

Description
-----------

This routine enables the broadcast storm limit function of the switch.

.. _`sw_init_broad_storm`:

sw_init_broad_storm
===================

.. c:function:: void sw_init_broad_storm(struct ksz_hw *hw)

    initialize broadcast storm

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_init_broad_storm.description`:

Description
-----------

This routine initializes the broadcast storm limit function of the switch.

.. _`hw_cfg_broad_storm`:

hw_cfg_broad_storm
==================

.. c:function:: void hw_cfg_broad_storm(struct ksz_hw *hw, u8 percent)

    configure broadcast storm

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 percent:
        Broadcast storm threshold in percent of transmit rate.

.. _`hw_cfg_broad_storm.description`:

Description
-----------

This routine configures the broadcast storm threshold of the switch.
It is called by user functions.  The hardware should be acquired first.

.. _`sw_dis_prio_rate`:

sw_dis_prio_rate
================

.. c:function:: void sw_dis_prio_rate(struct ksz_hw *hw, int port)

    disable switch priority rate

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`sw_dis_prio_rate.description`:

Description
-----------

This routine disables the priority rate function of the switch.

.. _`sw_init_prio_rate`:

sw_init_prio_rate
=================

.. c:function:: void sw_init_prio_rate(struct ksz_hw *hw)

    initialize switch prioirty rate

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_init_prio_rate.description`:

Description
-----------

This routine initializes the priority rate function of the switch.

.. _`sw_dis_diffserv`:

sw_dis_diffserv
===============

.. c:function:: void sw_dis_diffserv(struct ksz_hw *hw, int port)

    disable switch DiffServ priority

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`sw_dis_diffserv.description`:

Description
-----------

This routine disables the DiffServ priority function of the switch.

.. _`sw_dis_802_1p`:

sw_dis_802_1p
=============

.. c:function:: void sw_dis_802_1p(struct ksz_hw *hw, int port)

    disable switch 802.1p priority

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`sw_dis_802_1p.description`:

Description
-----------

This routine disables the 802.1p priority function of the switch.

.. _`sw_cfg_replace_null_vid`:

sw_cfg_replace_null_vid
=======================

.. c:function:: void sw_cfg_replace_null_vid(struct ksz_hw *hw, int set)

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int set:
        The flag to disable or enable.

.. _`sw_cfg_replace_vid`:

sw_cfg_replace_vid
==================

.. c:function:: void sw_cfg_replace_vid(struct ksz_hw *hw, int port, int set)

    enable switch 802.10 priority re-mapping

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int set:
        The flag to disable or enable.

.. _`sw_cfg_replace_vid.description`:

Description
-----------

This routine enables the 802.1p priority re-mapping function of the switch.
That allows 802.1p priority field to be replaced with the port's default
tag's priority value if the ingress packet's 802.1p priority has a higher
priority than port's default tag's priority.

.. _`sw_cfg_port_based`:

sw_cfg_port_based
=================

.. c:function:: void sw_cfg_port_based(struct ksz_hw *hw, int port, u8 prio)

    configure switch port based priority

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u8 prio:
        The priority to set.

.. _`sw_cfg_port_based.description`:

Description
-----------

This routine configures the port based priority of the switch.

.. _`sw_dis_multi_queue`:

sw_dis_multi_queue
==================

.. c:function:: void sw_dis_multi_queue(struct ksz_hw *hw, int port)

    disable transmit multiple queues

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

.. _`sw_dis_multi_queue.description`:

Description
-----------

This routine disables the transmit multiple queues selection of the switch
port.  Only single transmit queue on the port.

.. _`sw_init_prio`:

sw_init_prio
============

.. c:function:: void sw_init_prio(struct ksz_hw *hw)

    initialize switch priority

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_init_prio.description`:

Description
-----------

This routine initializes the switch QoS priority functions.

.. _`port_get_def_vid`:

port_get_def_vid
================

.. c:function:: void port_get_def_vid(struct ksz_hw *hw, int port, u16 *vid)

    get port default VID.

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u16 \*vid:
        Buffer to store the VID.

.. _`port_get_def_vid.description`:

Description
-----------

This routine retrieves the default VID of the port.

.. _`sw_init_vlan`:

sw_init_vlan
============

.. c:function:: void sw_init_vlan(struct ksz_hw *hw)

    initialize switch VLAN

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_init_vlan.description`:

Description
-----------

This routine initializes the VLAN function of the switch.

.. _`sw_cfg_port_base_vlan`:

sw_cfg_port_base_vlan
=====================

.. c:function:: void sw_cfg_port_base_vlan(struct ksz_hw *hw, int port, u8 member)

    configure port-based VLAN membership

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param u8 member:
        The port-based VLAN membership.

.. _`sw_cfg_port_base_vlan.description`:

Description
-----------

This routine configures the port-based VLAN membership of the port.

.. _`sw_get_addr`:

sw_get_addr
===========

.. c:function:: void sw_get_addr(struct ksz_hw *hw, u8 *mac_addr)

    get the switch MAC address.

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 \*mac_addr:
        Buffer to store the MAC address.

.. _`sw_get_addr.description`:

Description
-----------

This function retrieves the MAC address of the switch.

.. _`sw_set_addr`:

sw_set_addr
===========

.. c:function:: void sw_set_addr(struct ksz_hw *hw, u8 *mac_addr)

    configure switch MAC address

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 \*mac_addr:
        The MAC address.

.. _`sw_set_addr.description`:

Description
-----------

This function configures the MAC address of the switch.

.. _`sw_set_global_ctrl`:

sw_set_global_ctrl
==================

.. c:function:: void sw_set_global_ctrl(struct ksz_hw *hw)

    set switch global control

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_set_global_ctrl.description`:

Description
-----------

This routine sets the global control of the switch function.

.. _`port_set_stp_state`:

port_set_stp_state
==================

.. c:function:: void port_set_stp_state(struct ksz_hw *hw, int port, int state)

    configure port spanning tree state

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        The port index.

    :param int state:
        The spanning tree state.

.. _`port_set_stp_state.description`:

Description
-----------

This routine configures the spanning tree state of the port.

.. _`sw_clr_sta_mac_table`:

sw_clr_sta_mac_table
====================

.. c:function:: void sw_clr_sta_mac_table(struct ksz_hw *hw)

    clear static MAC table

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_clr_sta_mac_table.description`:

Description
-----------

This routine clears the static MAC table.

.. _`sw_init_stp`:

sw_init_stp
===========

.. c:function:: void sw_init_stp(struct ksz_hw *hw)

    initialize switch spanning tree support

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_init_stp.description`:

Description
-----------

This routine initializes the spanning tree support of the switch.

.. _`sw_block_addr`:

sw_block_addr
=============

.. c:function:: void sw_block_addr(struct ksz_hw *hw)

    block certain packets from the host port

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_block_addr.description`:

Description
-----------

This routine blocks certain packets from reaching to the host port.

.. _`hw_r_phy`:

hw_r_phy
========

.. c:function:: void hw_r_phy(struct ksz_hw *hw, int port, u16 reg, u16 *val)

    read data from PHY register

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        Port to read.

    :param u16 reg:
        PHY register to read.

    :param u16 \*val:
        Buffer to store the read data.

.. _`hw_r_phy.description`:

Description
-----------

This routine reads data from the PHY register.

.. _`hw_w_phy`:

hw_w_phy
========

.. c:function:: void hw_w_phy(struct ksz_hw *hw, int port, u16 reg, u16 val)

    write data to PHY register

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int port:
        Port to write.

    :param u16 reg:
        PHY register to write.

    :param u16 val:
        Word data to write.

.. _`hw_w_phy.description`:

Description
-----------

This routine writes data to the PHY register.

.. _`eeprom_read`:

eeprom_read
===========

.. c:function:: u16 eeprom_read(struct ksz_hw *hw, u8 reg)

    read from AT93C46 EEPROM

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 reg:
        The register offset.

.. _`eeprom_read.description`:

Description
-----------

This function reads a word from the AT93C46 EEPROM.

Return the data value.

.. _`eeprom_write`:

eeprom_write
============

.. c:function:: void eeprom_write(struct ksz_hw *hw, u8 reg, u16 data)

    write to AT93C46 EEPROM

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 reg:
        The register offset.

    :param u16 data:
        The data value.

.. _`eeprom_write.description`:

Description
-----------

This procedure writes a word to the AT93C46 EEPROM.

.. _`port_get_link_speed`:

port_get_link_speed
===================

.. c:function:: void port_get_link_speed(struct ksz_port *port)

    get current link status

    :param struct ksz_port \*port:
        The port instance.

.. _`port_get_link_speed.description`:

Description
-----------

This routine reads PHY registers to determine the current link status of the
switch ports.

.. _`port_set_link_speed`:

port_set_link_speed
===================

.. c:function:: void port_set_link_speed(struct ksz_port *port)

    set port speed

    :param struct ksz_port \*port:
        The port instance.

.. _`port_set_link_speed.description`:

Description
-----------

This routine sets the link speed of the switch ports.

.. _`port_force_link_speed`:

port_force_link_speed
=====================

.. c:function:: void port_force_link_speed(struct ksz_port *port)

    force port speed

    :param struct ksz_port \*port:
        The port instance.

.. _`port_force_link_speed.description`:

Description
-----------

This routine forces the link speed of the switch ports.

.. _`hw_chk_wol_pme_status`:

hw_chk_wol_pme_status
=====================

.. c:function:: int hw_chk_wol_pme_status(struct ksz_hw *hw)

    check PMEN pin

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_chk_wol_pme_status.description`:

Description
-----------

This function is used to check PMEN pin is asserted.

Return 1 if PMEN pin is asserted; otherwise, 0.

.. _`hw_clr_wol_pme_status`:

hw_clr_wol_pme_status
=====================

.. c:function:: void hw_clr_wol_pme_status(struct ksz_hw *hw)

    clear PMEN pin

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_clr_wol_pme_status.description`:

Description
-----------

This routine is used to clear PME_Status to deassert PMEN pin.

.. _`hw_cfg_wol_pme`:

hw_cfg_wol_pme
==============

.. c:function:: void hw_cfg_wol_pme(struct ksz_hw *hw, int set)

    enable or disable Wake-on-LAN

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int set:
        The flag indicating whether to enable or disable.

.. _`hw_cfg_wol_pme.description`:

Description
-----------

This routine is used to enable or disable Wake-on-LAN.

.. _`hw_cfg_wol`:

hw_cfg_wol
==========

.. c:function:: void hw_cfg_wol(struct ksz_hw *hw, u16 frame, int set)

    configure Wake-on-LAN features

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u16 frame:
        The pattern frame bit.

    :param int set:
        The flag indicating whether to enable or disable.

.. _`hw_cfg_wol.description`:

Description
-----------

This routine is used to enable or disable certain Wake-on-LAN features.

.. _`hw_set_wol_frame`:

hw_set_wol_frame
================

.. c:function:: void hw_set_wol_frame(struct ksz_hw *hw, int i, uint mask_size, const u8 *mask, uint frame_size, const u8 *pattern)

    program Wake-on-LAN pattern

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int i:
        The frame index.

    :param uint mask_size:
        The size of the mask.

    :param const u8 \*mask:
        Mask to ignore certain bytes in the pattern.

    :param uint frame_size:
        The size of the frame.

    :param const u8 \*pattern:
        The frame data.

.. _`hw_set_wol_frame.description`:

Description
-----------

This routine is used to program Wake-on-LAN pattern.

.. _`hw_add_wol_arp`:

hw_add_wol_arp
==============

.. c:function:: void hw_add_wol_arp(struct ksz_hw *hw, const u8 *ip_addr)

    add ARP pattern

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param const u8 \*ip_addr:
        The IPv4 address assigned to the device.

.. _`hw_add_wol_arp.description`:

Description
-----------

This routine is used to add ARP pattern for waking up the host.

.. _`hw_add_wol_bcast`:

hw_add_wol_bcast
================

.. c:function:: void hw_add_wol_bcast(struct ksz_hw *hw)

    add broadcast pattern

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_add_wol_bcast.description`:

Description
-----------

This routine is used to add broadcast pattern for waking up the host.

.. _`hw_add_wol_mcast`:

hw_add_wol_mcast
================

.. c:function:: void hw_add_wol_mcast(struct ksz_hw *hw)

    add multicast pattern

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_add_wol_mcast.description`:

Description
-----------

This routine is used to add multicast pattern for waking up the host.

It is assumed the multicast packet is the ICMPv6 neighbor solicitation used
by IPv6 ping command.  Note that multicast packets are filtred through the
multicast hash table, so not all multicast packets can wake up the host.

.. _`hw_add_wol_ucast`:

hw_add_wol_ucast
================

.. c:function:: void hw_add_wol_ucast(struct ksz_hw *hw)

    add unicast pattern

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_add_wol_ucast.description`:

Description
-----------

This routine is used to add unicast pattern to wakeup the host.

It is assumed the unicast packet is directed to the device, as the hardware
can only receive them in normal case.

.. _`hw_enable_wol`:

hw_enable_wol
=============

.. c:function:: void hw_enable_wol(struct ksz_hw *hw, u32 wol_enable, const u8 *net_addr)

    enable Wake-on-LAN

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u32 wol_enable:
        The Wake-on-LAN settings.

    :param const u8 \*net_addr:
        The IPv4 address assigned to the device.

.. _`hw_enable_wol.description`:

Description
-----------

This routine is used to enable Wake-on-LAN depending on driver settings.

.. _`hw_init`:

hw_init
=======

.. c:function:: int hw_init(struct ksz_hw *hw)

    check driver is correct for the hardware

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_init.description`:

Description
-----------

This function checks the hardware is correct for this driver and sets the
hardware up for proper initialization.

Return number of ports or 0 if not right.

.. _`hw_reset`:

hw_reset
========

.. c:function:: void hw_reset(struct ksz_hw *hw)

    reset the hardware

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_reset.description`:

Description
-----------

This routine resets the hardware.

.. _`hw_setup`:

hw_setup
========

.. c:function:: void hw_setup(struct ksz_hw *hw)

    setup the hardware

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_setup.description`:

Description
-----------

This routine setup the hardware for proper operation.

.. _`hw_setup_intr`:

hw_setup_intr
=============

.. c:function:: void hw_setup_intr(struct ksz_hw *hw)

    setup interrupt mask

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_setup_intr.description`:

Description
-----------

This routine setup the interrupt mask for proper operation.

.. _`hw_set_desc_base`:

hw_set_desc_base
================

.. c:function:: void hw_set_desc_base(struct ksz_hw *hw, u32 tx_addr, u32 rx_addr)

    set descriptor base addresses

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u32 tx_addr:
        The transmit descriptor base.

    :param u32 rx_addr:
        The receive descriptor base.

.. _`hw_set_desc_base.description`:

Description
-----------

This routine programs the descriptor base addresses after reset.

.. _`hw_start_rx`:

hw_start_rx
===========

.. c:function:: void hw_start_rx(struct ksz_hw *hw)

    start receiving

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_start_rx.description`:

Description
-----------

This routine starts the receive function of the hardware.

.. _`hw_stop_rx`:

hw_stop_rx
==========

.. c:function:: void hw_stop_rx(struct ksz_hw *hw)

    stop receiving

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_stop_rx.description`:

Description
-----------

This routine stops the receive function of the hardware.

.. _`hw_start_tx`:

hw_start_tx
===========

.. c:function:: void hw_start_tx(struct ksz_hw *hw)

    start transmitting

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_start_tx.description`:

Description
-----------

This routine starts the transmit function of the hardware.

.. _`hw_stop_tx`:

hw_stop_tx
==========

.. c:function:: void hw_stop_tx(struct ksz_hw *hw)

    stop transmitting

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_stop_tx.description`:

Description
-----------

This routine stops the transmit function of the hardware.

.. _`hw_disable`:

hw_disable
==========

.. c:function:: void hw_disable(struct ksz_hw *hw)

    disable hardware

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_disable.description`:

Description
-----------

This routine disables the hardware.

.. _`hw_enable`:

hw_enable
=========

.. c:function:: void hw_enable(struct ksz_hw *hw)

    enable hardware

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_enable.description`:

Description
-----------

This routine enables the hardware.

.. _`hw_alloc_pkt`:

hw_alloc_pkt
============

.. c:function:: int hw_alloc_pkt(struct ksz_hw *hw, int length, int physical)

    allocate enough descriptors for transmission

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int length:
        The length of the packet.

    :param int physical:
        Number of descriptors required.

.. _`hw_alloc_pkt.description`:

Description
-----------

This function allocates descriptors for transmission.

Return 0 if not successful; 1 for buffer copy; or number of descriptors.

.. _`hw_send_pkt`:

hw_send_pkt
===========

.. c:function:: void hw_send_pkt(struct ksz_hw *hw)

    mark packet for transmission

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_send_pkt.description`:

Description
-----------

This routine marks the packet for transmission in PCI version.

.. _`hw_set_addr`:

hw_set_addr
===========

.. c:function:: void hw_set_addr(struct ksz_hw *hw)

    set MAC address

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_set_addr.description`:

Description
-----------

This routine programs the MAC address of the hardware when the address is
overridden.

.. _`hw_read_addr`:

hw_read_addr
============

.. c:function:: void hw_read_addr(struct ksz_hw *hw)

    read MAC address

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_read_addr.description`:

Description
-----------

This routine retrieves the MAC address of the hardware.

.. _`hw_clr_multicast`:

hw_clr_multicast
================

.. c:function:: void hw_clr_multicast(struct ksz_hw *hw)

    clear multicast addresses

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_clr_multicast.description`:

Description
-----------

This routine removes all multicast addresses set in the hardware.

.. _`hw_set_grp_addr`:

hw_set_grp_addr
===============

.. c:function:: void hw_set_grp_addr(struct ksz_hw *hw)

    set multicast addresses

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`hw_set_grp_addr.description`:

Description
-----------

This routine programs multicast addresses for the hardware to accept those
addresses.

.. _`hw_set_multicast`:

hw_set_multicast
================

.. c:function:: void hw_set_multicast(struct ksz_hw *hw, u8 multicast)

    enable or disable all multicast receiving

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 multicast:
        To turn on or off the all multicast feature.

.. _`hw_set_multicast.description`:

Description
-----------

This routine enables/disables the hardware to accept all multicast packets.

.. _`hw_set_promiscuous`:

hw_set_promiscuous
==================

.. c:function:: void hw_set_promiscuous(struct ksz_hw *hw, u8 prom)

    enable or disable promiscuous receiving

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param u8 prom:
        To turn on or off the promiscuous feature.

.. _`hw_set_promiscuous.description`:

Description
-----------

This routine enables/disables the hardware to accept all packets.

.. _`sw_enable`:

sw_enable
=========

.. c:function:: void sw_enable(struct ksz_hw *hw, int enable)

    enable the switch

    :param struct ksz_hw \*hw:
        The hardware instance.

    :param int enable:
        The flag to enable or disable the switch

.. _`sw_enable.description`:

Description
-----------

This routine is used to enable/disable the switch in KSZ8842.

.. _`sw_setup`:

sw_setup
========

.. c:function:: void sw_setup(struct ksz_hw *hw)

    setup the switch

    :param struct ksz_hw \*hw:
        The hardware instance.

.. _`sw_setup.description`:

Description
-----------

This routine setup the hardware switch engine for default operation.

.. _`ksz_start_timer`:

ksz_start_timer
===============

.. c:function:: void ksz_start_timer(struct ksz_timer_info *info, int time)

    start kernel timer

    :param struct ksz_timer_info \*info:
        Kernel timer information.

    :param int time:
        The time tick.

.. _`ksz_start_timer.description`:

Description
-----------

This routine starts the kernel timer after the specified time tick.

.. _`ksz_stop_timer`:

ksz_stop_timer
==============

.. c:function:: void ksz_stop_timer(struct ksz_timer_info *info)

    stop kernel timer

    :param struct ksz_timer_info \*info:
        Kernel timer information.

.. _`ksz_stop_timer.description`:

Description
-----------

This routine stops the kernel timer.

.. _`ksz_alloc_soft_desc`:

ksz_alloc_soft_desc
===================

.. c:function:: int ksz_alloc_soft_desc(struct ksz_desc_info *desc_info, int transmit)

    allocate software descriptors

    :param struct ksz_desc_info \*desc_info:
        Descriptor information structure.

    :param int transmit:
        Indication that descriptors are for transmit.

.. _`ksz_alloc_soft_desc.description`:

Description
-----------

This local function allocates software descriptors for manipulation in
memory.

Return 0 if successful.

.. _`ksz_alloc_desc`:

ksz_alloc_desc
==============

.. c:function:: int ksz_alloc_desc(struct dev_info *adapter)

    allocate hardware descriptors

    :param struct dev_info \*adapter:
        Adapter information structure.

.. _`ksz_alloc_desc.description`:

Description
-----------

This local function allocates hardware descriptors for receiving and
transmitting.

Return 0 if successful.

.. _`free_dma_buf`:

free_dma_buf
============

.. c:function:: void free_dma_buf(struct dev_info *adapter, struct ksz_dma_buf *dma_buf, int direction)

    release DMA buffer resources

    :param struct dev_info \*adapter:
        Adapter information structure.

    :param struct ksz_dma_buf \*dma_buf:
        *undescribed*

    :param int direction:
        *undescribed*

.. _`free_dma_buf.description`:

Description
-----------

This routine is just a helper function to release the DMA buffer resources.

.. _`ksz_init_rx_buffers`:

ksz_init_rx_buffers
===================

.. c:function:: void ksz_init_rx_buffers(struct dev_info *adapter)

    initialize receive descriptors

    :param struct dev_info \*adapter:
        Adapter information structure.

.. _`ksz_init_rx_buffers.description`:

Description
-----------

This routine initializes DMA buffers for receiving.

.. _`ksz_alloc_mem`:

ksz_alloc_mem
=============

.. c:function:: int ksz_alloc_mem(struct dev_info *adapter)

    allocate memory for hardware descriptors

    :param struct dev_info \*adapter:
        Adapter information structure.

.. _`ksz_alloc_mem.description`:

Description
-----------

This function allocates memory for use by hardware descriptors for receiving
and transmitting.

Return 0 if successful.

.. _`ksz_free_desc`:

ksz_free_desc
=============

.. c:function:: void ksz_free_desc(struct dev_info *adapter)

    free software and hardware descriptors

    :param struct dev_info \*adapter:
        Adapter information structure.

.. _`ksz_free_desc.description`:

Description
-----------

This local routine frees the software and hardware descriptors allocated by
\ :c:func:`ksz_alloc_desc`\ .

.. _`ksz_free_buffers`:

ksz_free_buffers
================

.. c:function:: void ksz_free_buffers(struct dev_info *adapter, struct ksz_desc_info *desc_info, int direction)

    free buffers used in the descriptors

    :param struct dev_info \*adapter:
        Adapter information structure.

    :param struct ksz_desc_info \*desc_info:
        Descriptor information structure.

    :param int direction:
        *undescribed*

.. _`ksz_free_buffers.description`:

Description
-----------

This local routine frees buffers used in the DMA buffers.

.. _`ksz_free_mem`:

ksz_free_mem
============

.. c:function:: void ksz_free_mem(struct dev_info *adapter)

    free all resources used by descriptors

    :param struct dev_info \*adapter:
        Adapter information structure.

.. _`ksz_free_mem.description`:

Description
-----------

This local routine frees all the resources allocated by \ :c:func:`ksz_alloc_mem`\ .

.. _`send_packet`:

send_packet
===========

.. c:function:: void send_packet(struct sk_buff *skb, struct net_device *dev)

    send packet

    :param struct sk_buff \*skb:
        Socket buffer.

    :param struct net_device \*dev:
        Network device.

.. _`send_packet.description`:

Description
-----------

This routine is used to send a packet out to the network.

.. _`transmit_cleanup`:

transmit_cleanup
================

.. c:function:: void transmit_cleanup(struct dev_info *hw_priv, int normal)

    clean up transmit descriptors

    :param struct dev_info \*hw_priv:
        *undescribed*

    :param int normal:
        *undescribed*

.. _`transmit_cleanup.description`:

Description
-----------

This routine is called to clean up the transmitted buffers.

.. _`tx_done`:

tx_done
=======

.. c:function:: void tx_done(struct dev_info *hw_priv)

    transmit done processing

    :param struct dev_info \*hw_priv:
        *undescribed*

.. _`tx_done.description`:

Description
-----------

This routine is called when the transmit interrupt is triggered, indicating
either a packet is sent successfully or there are transmit errors.

.. _`netdev_tx`:

netdev_tx
=========

.. c:function:: netdev_tx_t netdev_tx(struct sk_buff *skb, struct net_device *dev)

    send out packet

    :param struct sk_buff \*skb:
        Socket buffer.

    :param struct net_device \*dev:
        Network device.

.. _`netdev_tx.description`:

Description
-----------

This function is used by the upper network layer to send out a packet.

Return 0 if successful; otherwise an error code indicating failure.

.. _`netdev_tx_timeout`:

netdev_tx_timeout
=================

.. c:function:: void netdev_tx_timeout(struct net_device *dev)

    transmit timeout processing

    :param struct net_device \*dev:
        Network device.

.. _`netdev_tx_timeout.description`:

Description
-----------

This routine is called when the transmit timer expires.  That indicates the
hardware is not running correctly because transmit interrupts are not
triggered to free up resources so that the transmit routine can continue
sending out packets.  The hardware is reset to correct the problem.

.. _`netdev_intr`:

netdev_intr
===========

.. c:function:: irqreturn_t netdev_intr(int irq, void *dev_id)

    interrupt handling

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        Network device.

.. _`netdev_intr.description`:

Description
-----------

This function is called by upper network layer to signal interrupt.

Return IRQ_HANDLED if interrupt is handled.

.. _`netdev_close`:

netdev_close
============

.. c:function:: int netdev_close(struct net_device *dev)

    close network device

    :param struct net_device \*dev:
        Network device.

.. _`netdev_close.description`:

Description
-----------

This function process the close operation of network device.  This is caused
by the user command "ifconfig ethX down."

Return 0 if successful; otherwise an error code indicating failure.

.. _`netdev_open`:

netdev_open
===========

.. c:function:: int netdev_open(struct net_device *dev)

    open network device

    :param struct net_device \*dev:
        Network device.

.. _`netdev_open.description`:

Description
-----------

This function process the open operation of network device.  This is caused
by the user command "ifconfig ethX up."

Return 0 if successful; otherwise an error code indicating failure.

.. _`netdev_query_statistics`:

netdev_query_statistics
=======================

.. c:function:: struct net_device_stats *netdev_query_statistics(struct net_device *dev)

    query network device statistics

    :param struct net_device \*dev:
        Network device.

.. _`netdev_query_statistics.description`:

Description
-----------

This function returns the statistics of the network device.  The device
needs not be opened.

Return network device statistics.

.. _`netdev_set_mac_address`:

netdev_set_mac_address
======================

.. c:function:: int netdev_set_mac_address(struct net_device *dev, void *addr)

    set network device MAC address

    :param struct net_device \*dev:
        Network device.

    :param void \*addr:
        Buffer of MAC address.

.. _`netdev_set_mac_address.description`:

Description
-----------

This function is used to set the MAC address of the network device.

Return 0 to indicate success.

.. _`netdev_set_rx_mode`:

netdev_set_rx_mode
==================

.. c:function:: void netdev_set_rx_mode(struct net_device *dev)

    :param struct net_device \*dev:
        Network device.

.. _`netdev_set_rx_mode.description`:

Description
-----------

This routine is used to set multicast addresses or put the network device
into promiscuous mode.

.. _`netdev_ioctl`:

netdev_ioctl
============

.. c:function:: int netdev_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd)

    I/O control processing

    :param struct net_device \*dev:
        Network device.

    :param struct ifreq \*ifr:
        Interface request structure.

    :param int cmd:
        I/O control code.

.. _`netdev_ioctl.description`:

Description
-----------

This function is used to process I/O control calls.

Return 0 to indicate success.

.. _`mdio_read`:

mdio_read
=========

.. c:function:: int mdio_read(struct net_device *dev, int phy_id, int reg_num)

    read PHY register

    :param struct net_device \*dev:
        Network device.

    :param int phy_id:
        The PHY id.

    :param int reg_num:
        The register number.

.. _`mdio_read.description`:

Description
-----------

This function returns the PHY register value.

Return the register value.

.. _`mdio_write`:

mdio_write
==========

.. c:function:: void mdio_write(struct net_device *dev, int phy_id, int reg_num, int val)

    set PHY register

    :param struct net_device \*dev:
        Network device.

    :param int phy_id:
        The PHY id.

    :param int reg_num:
        The register number.

    :param int val:
        The register value.

.. _`mdio_write.description`:

Description
-----------

This procedure sets the PHY register value.

.. _`netdev_get_link_ksettings`:

netdev_get_link_ksettings
=========================

.. c:function:: int netdev_get_link_ksettings(struct net_device *dev, struct ethtool_link_ksettings *cmd)

    get network device settings

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_link_ksettings \*cmd:
        Ethtool command.

.. _`netdev_get_link_ksettings.description`:

Description
-----------

This function queries the PHY and returns its state in the ethtool command.

Return 0 if successful; otherwise an error code.

.. _`netdev_set_link_ksettings`:

netdev_set_link_ksettings
=========================

.. c:function:: int netdev_set_link_ksettings(struct net_device *dev, const struct ethtool_link_ksettings *cmd)

    set network device settings

    :param struct net_device \*dev:
        Network device.

    :param const struct ethtool_link_ksettings \*cmd:
        Ethtool command.

.. _`netdev_set_link_ksettings.description`:

Description
-----------

This function sets the PHY according to the ethtool command.

Return 0 if successful; otherwise an error code.

.. _`netdev_nway_reset`:

netdev_nway_reset
=================

.. c:function:: int netdev_nway_reset(struct net_device *dev)

    restart auto-negotiation

    :param struct net_device \*dev:
        Network device.

.. _`netdev_nway_reset.description`:

Description
-----------

This function restarts the PHY for auto-negotiation.

Return 0 if successful; otherwise an error code.

.. _`netdev_get_link`:

netdev_get_link
===============

.. c:function:: u32 netdev_get_link(struct net_device *dev)

    get network device link status

    :param struct net_device \*dev:
        Network device.

.. _`netdev_get_link.description`:

Description
-----------

This function gets the link status from the PHY.

Return true if PHY is linked and false otherwise.

.. _`netdev_get_drvinfo`:

netdev_get_drvinfo
==================

.. c:function:: void netdev_get_drvinfo(struct net_device *dev, struct ethtool_drvinfo *info)

    get network driver information

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_drvinfo \*info:
        Ethtool driver info data structure.

.. _`netdev_get_drvinfo.description`:

Description
-----------

This procedure returns the driver information.

.. _`netdev_get_regs`:

netdev_get_regs
===============

.. c:function:: void netdev_get_regs(struct net_device *dev, struct ethtool_regs *regs, void *ptr)

    get register dump

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_regs \*regs:
        Ethtool registers data structure.

    :param void \*ptr:
        Buffer to store the register values.

.. _`netdev_get_regs.description`:

Description
-----------

This procedure dumps the register values in the provided buffer.

.. _`netdev_get_wol`:

netdev_get_wol
==============

.. c:function:: void netdev_get_wol(struct net_device *dev, struct ethtool_wolinfo *wol)

    get Wake-on-LAN support

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_wolinfo \*wol:
        Ethtool Wake-on-LAN data structure.

.. _`netdev_get_wol.description`:

Description
-----------

This procedure returns Wake-on-LAN support.

.. _`netdev_set_wol`:

netdev_set_wol
==============

.. c:function:: int netdev_set_wol(struct net_device *dev, struct ethtool_wolinfo *wol)

    set Wake-on-LAN support

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_wolinfo \*wol:
        Ethtool Wake-on-LAN data structure.

.. _`netdev_set_wol.description`:

Description
-----------

This function sets Wake-on-LAN support.

Return 0 if successful; otherwise an error code.

.. _`netdev_get_msglevel`:

netdev_get_msglevel
===================

.. c:function:: u32 netdev_get_msglevel(struct net_device *dev)

    get debug message level

    :param struct net_device \*dev:
        Network device.

.. _`netdev_get_msglevel.description`:

Description
-----------

This function returns current debug message level.

Return current debug message flags.

.. _`netdev_set_msglevel`:

netdev_set_msglevel
===================

.. c:function:: void netdev_set_msglevel(struct net_device *dev, u32 value)

    set debug message level

    :param struct net_device \*dev:
        Network device.

    :param u32 value:
        Debug message flags.

.. _`netdev_set_msglevel.description`:

Description
-----------

This procedure sets debug message level.

.. _`netdev_get_eeprom_len`:

netdev_get_eeprom_len
=====================

.. c:function:: int netdev_get_eeprom_len(struct net_device *dev)

    get EEPROM length

    :param struct net_device \*dev:
        Network device.

.. _`netdev_get_eeprom_len.description`:

Description
-----------

This function returns the length of the EEPROM.

Return length of the EEPROM.

.. _`eeprom_magic`:

EEPROM_MAGIC
============

.. c:function::  EEPROM_MAGIC()

    get EEPROM data

.. _`eeprom_magic.description`:

Description
-----------

This function dumps the EEPROM data in the provided buffer.

Return 0 if successful; otherwise an error code.

.. _`netdev_set_eeprom`:

netdev_set_eeprom
=================

.. c:function:: int netdev_set_eeprom(struct net_device *dev, struct ethtool_eeprom *eeprom, u8 *data)

    write EEPROM data

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_eeprom \*eeprom:
        Ethtool EEPROM data structure.

    :param u8 \*data:
        Data buffer.

.. _`netdev_set_eeprom.description`:

Description
-----------

This function modifies the EEPROM data one byte at a time.

Return 0 if successful; otherwise an error code.

.. _`netdev_get_pauseparam`:

netdev_get_pauseparam
=====================

.. c:function:: void netdev_get_pauseparam(struct net_device *dev, struct ethtool_pauseparam *pause)

    get flow control parameters

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_pauseparam \*pause:
        Ethtool PAUSE settings data structure.

.. _`netdev_get_pauseparam.description`:

Description
-----------

This procedure returns the PAUSE control flow settings.

.. _`netdev_set_pauseparam`:

netdev_set_pauseparam
=====================

.. c:function:: int netdev_set_pauseparam(struct net_device *dev, struct ethtool_pauseparam *pause)

    set flow control parameters

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_pauseparam \*pause:
        Ethtool PAUSE settings data structure.

.. _`netdev_set_pauseparam.description`:

Description
-----------

This function sets the PAUSE control flow settings.
Not implemented yet.

Return 0 if successful; otherwise an error code.

.. _`netdev_get_ringparam`:

netdev_get_ringparam
====================

.. c:function:: void netdev_get_ringparam(struct net_device *dev, struct ethtool_ringparam *ring)

    get tx/rx ring parameters

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_ringparam \*ring:
        *undescribed*

.. _`netdev_get_ringparam.description`:

Description
-----------

This procedure returns the TX/RX ring settings.

.. _`netdev_get_strings`:

netdev_get_strings
==================

.. c:function:: void netdev_get_strings(struct net_device *dev, u32 stringset, u8 *buf)

    get statistics identity strings

    :param struct net_device \*dev:
        Network device.

    :param u32 stringset:
        String set identifier.

    :param u8 \*buf:
        Buffer to store the strings.

.. _`netdev_get_strings.description`:

Description
-----------

This procedure returns the strings used to identify the statistics.

.. _`netdev_get_sset_count`:

netdev_get_sset_count
=====================

.. c:function:: int netdev_get_sset_count(struct net_device *dev, int sset)

    get statistics size

    :param struct net_device \*dev:
        Network device.

    :param int sset:
        The statistics set number.

.. _`netdev_get_sset_count.description`:

Description
-----------

This function returns the size of the statistics to be reported.

Return size of the statistics to be reported.

.. _`netdev_get_ethtool_stats`:

netdev_get_ethtool_stats
========================

.. c:function:: void netdev_get_ethtool_stats(struct net_device *dev, struct ethtool_stats *stats, u64 *data)

    get network device statistics

    :param struct net_device \*dev:
        Network device.

    :param struct ethtool_stats \*stats:
        Ethtool statistics data structure.

    :param u64 \*data:
        Buffer to store the statistics.

.. _`netdev_get_ethtool_stats.description`:

Description
-----------

This procedure returns the statistics.

.. _`netdev_set_features`:

netdev_set_features
===================

.. c:function:: int netdev_set_features(struct net_device *dev, netdev_features_t features)

    set receive checksum support

    :param struct net_device \*dev:
        Network device.

    :param netdev_features_t features:
        New device features (offloads).

.. _`netdev_set_features.description`:

Description
-----------

This function sets receive checksum support setting.

Return 0 if successful; otherwise an error code.

.. _`dev_monitor`:

dev_monitor
===========

.. c:function:: void dev_monitor(unsigned long ptr)

    periodic monitoring

    :param unsigned long ptr:
        Network device pointer.

.. _`dev_monitor.description`:

Description
-----------

This routine is run in a kernel timer to monitor the network device.

.. _`netdev_init`:

netdev_init
===========

.. c:function:: int netdev_init(struct net_device *dev)

    initialize network device.

    :param struct net_device \*dev:
        Network device.

.. _`netdev_init.description`:

Description
-----------

This function initializes the network device.

Return 0 if successful; otherwise an error code indicating failure.

.. This file was automatic generated / don't edit.

