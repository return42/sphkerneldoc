.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ste_dma40.c

.. _`d40_command`:

enum d40_command
================

.. c:type:: enum d40_command

    The different commands and/or statuses.

.. _`d40_command.definition`:

Definition
----------

.. code-block:: c

    enum d40_command {
        D40_DMA_STOP,
        D40_DMA_RUN,
        D40_DMA_SUSPEND_REQ,
        D40_DMA_SUSPENDED
    };

.. _`d40_command.constants`:

Constants
---------

D40_DMA_STOP
    DMA channel command STOP or status STOPPED,

D40_DMA_RUN
    The DMA channel is RUNNING of the command RUN.

D40_DMA_SUSPEND_REQ
    Request the DMA to SUSPEND as soon as possible.

D40_DMA_SUSPENDED
    The DMA channel is SUSPENDED.

.. _`d40_interrupt_lookup`:

struct d40_interrupt_lookup
===========================

.. c:type:: struct d40_interrupt_lookup

    lookup table for interrupt handler

.. _`d40_interrupt_lookup.definition`:

Definition
----------

.. code-block:: c

    struct d40_interrupt_lookup {
        u32 src;
        u32 clr;
        bool is_error;
        int offset;
    }

.. _`d40_interrupt_lookup.members`:

Members
-------

src
    Interrupt mask register.

clr
    Interrupt clear register.

is_error
    true if this is an error interrupt.

offset
    start delta in the lookup_log_chans in d40_base. If equals to
    D40_PHY_CHAN, the lookup_phy_chans shall be used instead.

.. _`d40_reg_val`:

struct d40_reg_val
==================

.. c:type:: struct d40_reg_val

    simple lookup struct

.. _`d40_reg_val.definition`:

Definition
----------

.. code-block:: c

    struct d40_reg_val {
        unsigned int reg;
        unsigned int val;
    }

.. _`d40_reg_val.members`:

Members
-------

reg
    The register.

val
    The value that belongs to the register in reg.

.. _`d40_lli_pool`:

struct d40_lli_pool
===================

.. c:type:: struct d40_lli_pool

    Structure for keeping LLIs in memory

.. _`d40_lli_pool.definition`:

Definition
----------

.. code-block:: c

    struct d40_lli_pool {
        void *base;
        int size;
        dma_addr_t dma_addr;
        u8 pre_alloc_lli;
    }

.. _`d40_lli_pool.members`:

Members
-------

base
    Pointer to memory area when the pre_alloc_lli's are not large
    enough, IE bigger than the most common case, 1 dst and 1 src. NULL if
    pre_alloc_lli is used.

size
    The size in bytes of the memory at base or the size of pre_alloc_lli.

dma_addr
    DMA address, if mapped

pre_alloc_lli
    Pre allocated area for the most common case of transfers,
    one buffer to one buffer.

.. _`d40_desc`:

struct d40_desc
===============

.. c:type:: struct d40_desc

    A descriptor is one DMA job.

.. _`d40_desc.definition`:

Definition
----------

.. code-block:: c

    struct d40_desc {
        struct d40_phy_lli_bidir lli_phy;
        struct d40_log_lli_bidir lli_log;
        struct d40_lli_pool lli_pool;
        int lli_len;
        int lli_current;
        int lcla_alloc;
        struct dma_async_tx_descriptor txd;
        struct list_head node;
        bool is_in_client_list;
        bool cyclic;
    }

.. _`d40_desc.members`:

Members
-------

lli_phy
    LLI settings for physical channel. Both src and dst=
    points into the lli_pool, to base if lli_len > 1 or to pre_alloc_lli if
    lli_len equals one.

lli_log
    Same as above but for logical channels.

lli_pool
    The pool with two entries pre-allocated.

lli_len
    Number of llis of current descriptor.

lli_current
    Number of transferred llis.

lcla_alloc
    Number of LCLA entries allocated.

txd
    DMA engine struct. Used for among other things for communication
    during a transfer.

node
    List entry.

is_in_client_list
    true if the client owns this descriptor.

cyclic
    true if this is a cyclic job

.. _`d40_desc.description`:

Description
-----------

This descriptor is used for both logical and physical transfers.

.. _`d40_lcla_pool`:

struct d40_lcla_pool
====================

.. c:type:: struct d40_lcla_pool

    LCLA pool settings and data.

.. _`d40_lcla_pool.definition`:

Definition
----------

.. code-block:: c

    struct d40_lcla_pool {
        void *base;
        dma_addr_t dma_addr;
        void *base_unaligned;
        int pages;
        spinlock_t lock;
        struct d40_desc **alloc_map;
    }

.. _`d40_lcla_pool.members`:

Members
-------

base
    The virtual address of LCLA. 18 bit aligned.

dma_addr
    *undescribed*

base_unaligned
    The orignal kmalloc pointer, if kmalloc is used.
    This pointer is only there for clean-up on error.

pages
    The number of pages needed for all physical channels.
    Only used later for clean-up on error

lock
    Lock to protect the content in this struct.

alloc_map
    big map over which LCLA entry is own by which job.

.. _`d40_phy_res`:

struct d40_phy_res
==================

.. c:type:: struct d40_phy_res

    struct for handling eventlines mapped to physical channels.

.. _`d40_phy_res.definition`:

Definition
----------

.. code-block:: c

    struct d40_phy_res {
        spinlock_t lock;
        bool reserved;
        int num;
        u32 allocated_src;
        u32 allocated_dst;
        bool use_soft_lli;
    }

.. _`d40_phy_res.members`:

Members
-------

lock
    A lock protection this entity.

reserved
    True if used by secure world or otherwise.

num
    The physical channel number of this entity.

allocated_src
    Bit mapped to show which src event line's are mapped to
    this physical channel. Can also be free or physically allocated.

allocated_dst
    Same as for src but is dst.
    allocated_dst and allocated_src uses the D40_ALLOC\* defines as well as
    event line number.

use_soft_lli
    To mark if the linked lists of channel are managed by SW.

.. _`d40_chan`:

struct d40_chan
===============

.. c:type:: struct d40_chan

    Struct that describes a channel.

.. _`d40_chan.definition`:

Definition
----------

.. code-block:: c

    struct d40_chan {
        spinlock_t lock;
        int log_num;
        int pending_tx;
        bool busy;
        struct d40_phy_res *phy_chan;
        struct dma_chan chan;
        struct tasklet_struct tasklet;
        struct list_head client;
        struct list_head pending_queue;
        struct list_head active;
        struct list_head done;
        struct list_head queue;
        struct list_head prepare_queue;
        struct stedma40_chan_cfg dma_cfg;
        bool configured;
        struct d40_base *base;
        u32 src_def_cfg;
        u32 dst_def_cfg;
        struct d40_def_lcsp log_def;
        struct d40_log_lli_full *lcpa;
        dma_addr_t runtime_addr;
        enum dma_transfer_direction runtime_direction;
    }

.. _`d40_chan.members`:

Members
-------

lock
    A spinlock to protect this struct.

log_num
    The logical number, if any of this channel.

pending_tx
    The number of pending transfers. Used between interrupt handler
    and tasklet.

busy
    Set to true when transfer is ongoing on this channel.

phy_chan
    Pointer to physical channel which this instance runs on. If this
    point is NULL, then the channel is not allocated.

chan
    DMA engine handle.

tasklet
    Tasklet that gets scheduled from interrupt context to complete a
    transfer and call client callback.

client
    Cliented owned descriptor list.

pending_queue
    Submitted jobs, to be issued by \ :c:func:`issue_pending`\ 

active
    Active descriptor.

done
    Completed jobs

queue
    Queued jobs.

prepare_queue
    Prepared jobs.

dma_cfg
    The client configuration of this dma channel.

configured
    whether the dma_cfg configuration is valid

base
    Pointer to the device instance struct.

src_def_cfg
    Default cfg register setting for src.

dst_def_cfg
    Default cfg register setting for dst.

log_def
    Default logical channel settings.

lcpa
    Pointer to dst and src lcpa settings.

runtime_addr
    runtime configured address.

runtime_direction
    runtime configured direction.

.. _`d40_chan.description`:

Description
-----------

This struct can either "be" a logical or a physical channel.

.. _`d40_gen_dmac`:

struct d40_gen_dmac
===================

.. c:type:: struct d40_gen_dmac

    generic values to represent u8500/u8540 DMA controller

.. _`d40_gen_dmac.definition`:

Definition
----------

.. code-block:: c

    struct d40_gen_dmac {
        u32 *backup;
        u32 backup_size;
        u32 realtime_en;
        u32 realtime_clear;
        u32 high_prio_en;
        u32 high_prio_clear;
        u32 interrupt_en;
        u32 interrupt_clear;
        struct d40_interrupt_lookup *il;
        u32 il_size;
        struct d40_reg_val *init_reg;
        u32 init_reg_size;
    }

.. _`d40_gen_dmac.members`:

Members
-------

backup
    the pointer to the registers address array for backup

backup_size
    the size of the registers address array for backup

realtime_en
    the realtime enable register

realtime_clear
    the realtime clear register

high_prio_en
    the high priority enable register

high_prio_clear
    the high priority clear register

interrupt_en
    the interrupt enable register

interrupt_clear
    the interrupt clear register

il
    the pointer to struct d40_interrupt_lookup

il_size
    the size of d40_interrupt_lookup array

init_reg
    the pointer to the struct d40_reg_val

init_reg_size
    the size of d40_reg_val array

.. _`d40_base`:

struct d40_base
===============

.. c:type:: struct d40_base

    The big global struct, one for each probe'd instance.

.. _`d40_base.definition`:

Definition
----------

.. code-block:: c

    struct d40_base {
        spinlock_t interrupt_lock;
        spinlock_t execmd_lock;
        struct device *dev;
        void __iomem *virtbase;
        u8 rev:4;
        struct clk *clk;
        phys_addr_t phy_start;
        resource_size_t phy_size;
        int irq;
        int num_memcpy_chans;
        int num_phy_chans;
        int num_log_chans;
        struct device_dma_parameters dma_parms;
        struct dma_device dma_both;
        struct dma_device dma_slave;
        struct dma_device dma_memcpy;
        struct d40_chan *phy_chans;
        struct d40_chan *log_chans;
        struct d40_chan **lookup_log_chans;
        struct d40_chan **lookup_phy_chans;
        struct stedma40_platform_data *plat_data;
        struct regulator *lcpa_regulator;
        struct d40_phy_res *phy_res;
        struct d40_lcla_pool lcla_pool;
        void *lcpa_base;
        dma_addr_t phy_lcpa;
        resource_size_t lcpa_size;
        struct kmem_cache *desc_slab;
        u32 reg_val_backup;
        u32 reg_val_backup_v4;
        u32 *reg_val_backup_chan;
        u16 gcc_pwr_off_mask;
        struct d40_gen_dmac gen_dmac;
    }

.. _`d40_base.members`:

Members
-------

interrupt_lock
    Lock used to make sure one interrupt is handle a time.

execmd_lock
    Lock for execute command usage since several channels share
    the same physical register.

dev
    The device structure.

virtbase
    The virtual base address of the DMA's register.

rev
    silicon revision detected.

clk
    Pointer to the DMA clock structure.

phy_start
    Physical memory start of the DMA registers.

phy_size
    Size of the DMA register map.

irq
    The IRQ number.

num_memcpy_chans
    The number of channels used for memcpy (mem-to-mem
    transfers).

num_phy_chans
    The number of physical channels. Read from HW. This
    is the number of available channels for this driver, not counting "Secure
    mode" allocated physical channels.

num_log_chans
    The number of logical channels. Calculated from
    num_phy_chans.

dma_parms
    *undescribed*

dma_both
    dma_device channels that can do both memcpy and slave transfers.

dma_slave
    dma_device channels that can do only do slave transfers.

dma_memcpy
    dma_device channels that can do only do memcpy transfers.

phy_chans
    Room for all possible physical channels in system.

log_chans
    Room for all possible logical channels in system.

lookup_log_chans
    Used to map interrupt number to logical channel. Points
    to log_chans entries.

lookup_phy_chans
    Used to map interrupt number to physical channel. Points
    to phy_chans entries.

plat_data
    Pointer to provided platform_data which is the driver
    configuration.

lcpa_regulator
    Pointer to hold the regulator for the esram bank for lcla.

phy_res
    Vector containing all physical channels.

lcla_pool
    lcla pool settings and data.

lcpa_base
    The virtual mapped address of LCPA.

phy_lcpa
    The physical address of the LCPA.

lcpa_size
    The size of the LCPA area.

desc_slab
    cache for descriptors.

reg_val_backup
    Here the values of some hardware registers are stored
    before the DMA is powered off. They are restored when the power is back on.

reg_val_backup_v4
    Backup of registers that only exits on dma40 v3 and
    later

reg_val_backup_chan
    Backup data for standard channel parameter registers.

gcc_pwr_off_mask
    Mask to maintain the channels that can be turned off.

gen_dmac
    the struct for generic registers values to represent u8500/8540
    DMA controller

.. This file was automatic generated / don't edit.

