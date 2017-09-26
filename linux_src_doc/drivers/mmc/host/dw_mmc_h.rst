.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/dw_mmc.h

.. _`dw_mci`:

struct dw_mci
=============

.. c:type:: struct dw_mci

    MMC controller state shared between all slots

.. _`dw_mci.definition`:

Definition
----------

.. code-block:: c

    struct dw_mci {
        spinlock_t lock;
        spinlock_t irq_lock;
        void __iomem *regs;
        void __iomem *fifo_reg;
        u32 data_addr_override;
        bool wm_aligned;
        struct scatterlist *sg;
        struct sg_mapping_iter sg_miter;
        struct mmc_request *mrq;
        struct mmc_command *cmd;
        struct mmc_data *data;
        struct mmc_command stop_abort;
        unsigned int prev_blksz;
        unsigned char timing;
        int use_dma;
        int using_dma;
        int dma_64bit_address;
        dma_addr_t sg_dma;
        void *sg_cpu;
        const struct dw_mci_dma_ops *dma_ops;
        unsigned int ring_size;
        struct dw_mci_dma_slave *dms;
        resource_size_t phy_regs;
        u32 cmd_status;
        u32 data_status;
        u32 stop_cmdr;
        u32 dir_status;
        struct tasklet_struct tasklet;
        unsigned long pending_events;
        unsigned long completed_events;
        enum dw_mci_state state;
        struct list_head queue;
        u32 bus_hz;
        u32 current_speed;
        u32 fifoth_val;
        u16 verid;
        struct device *dev;
        struct dw_mci_board *pdata;
        const struct dw_mci_drv_data *drv_data;
        void *priv;
        struct clk *biu_clk;
        struct clk *ciu_clk;
        struct dw_mci_slot *slot;
        int fifo_depth;
        int data_shift;
        u8 part_buf_start;
        u8 part_buf_count;
        union {
            u16 part_buf16;
            u32 part_buf32;
            u64 part_buf;
        } ;
        void (*push_data)(struct dw_mci *host, void *buf, int cnt);
        void (*pull_data)(struct dw_mci *host, void *buf, int cnt);
        bool vqmmc_enabled;
        unsigned long irq_flags;
        int irq;
        int sdio_id0;
        struct timer_list cmd11_timer;
        struct timer_list cto_timer;
        struct timer_list dto_timer;
    }

.. _`dw_mci.members`:

Members
-------

lock
    Spinlock protecting the queue and associated data.

irq_lock
    Spinlock protecting the INTMASK setting.

regs
    Pointer to MMIO registers.

fifo_reg
    Pointer to MMIO registers for data FIFO

data_addr_override
    override fifo reg offset with this value.

wm_aligned
    force fifo watermark equal with data length in PIO mode.
    Set as true if alignment is needed.

sg
    Scatterlist entry currently being processed by PIO code, if any.

sg_miter
    PIO mapping scatterlist iterator.

mrq
    The request currently being processed on \ ``cur_slot``\ ,
    or NULL if the controller is idle.

cmd
    The command currently being sent to the card, or NULL.

data
    The data currently being transferred, or NULL if no data
    transfer is in progress.

stop_abort
    The command currently prepared for stoping transfer.

prev_blksz
    The former transfer blksz record.

timing
    Record of current ios timing.

use_dma
    Whether DMA channel is initialized or not.

using_dma
    Whether DMA is in use for the current transfer.

dma_64bit_address
    Whether DMA supports 64-bit address mode or not.

sg_dma
    Bus address of DMA buffer.

sg_cpu
    Virtual address of DMA buffer.

dma_ops
    Pointer to platform-specific DMA callbacks.

ring_size
    Buffer size for idma descriptors.
    command. Only valid when EVENT_CMD_COMPLETE is pending.

dms
    structure of slave-dma private data.

phy_regs
    physical address of controller's register map

cmd_status
    Snapshot of SR taken upon completion of the current

data_status
    Snapshot of SR taken upon completion of the current
    data transfer. Only valid when EVENT_DATA_COMPLETE or
    EVENT_DATA_ERROR is pending.

stop_cmdr
    Value to be loaded into CMDR when the stop command is
    to be sent.

dir_status
    Direction of current transfer.

tasklet
    Tasklet running the request state machine.

pending_events
    Bitmask of events flagged by the interrupt handler
    to be processed by the tasklet.

completed_events
    Bitmask of events which the state machine has
    processed.

state
    Tasklet state.

queue
    List of slots waiting for access to the controller.

bus_hz
    The rate of \ ``mck``\  in Hz. This forms the basis for MMC bus
    rate and timeout calculations.

current_speed
    Configured rate of the controller.

fifoth_val
    The value of FIFOTH register.

verid
    Denote Version ID.

dev
    Device associated with the MMC controller.

pdata
    Platform data associated with the MMC controller.

drv_data
    Driver specific data for identified variant of the controller

priv
    Implementation defined private data.

biu_clk
    Pointer to bus interface unit clock instance.

ciu_clk
    Pointer to card interface unit clock instance.

slot
    Slots sharing this MMC controller.

fifo_depth
    depth of FIFO.

data_shift
    log2 of FIFO item size.

part_buf_start
    Start index in part_buf.

part_buf_count
    Bytes of partial data in part_buf.

{unnamed_union}
    anonymous

part_buf16
    *undescribed*

part_buf32
    *undescribed*

part_buf
    Simple buffer for partial fifo reads/writes.

push_data
    Pointer to FIFO push function.

pull_data
    Pointer to FIFO pull function.

vqmmc_enabled
    Status of vqmmc, should be true or false.

irq_flags
    The flags to be passed to request_irq.

irq
    The irq value to be passed to request_irq.

sdio_id0
    Number of slot0 in the SDIO interrupt registers.

cmd11_timer
    Timer for SD3.0 voltage switch over scheme.

cto_timer
    Timer for broken command transfer over scheme.

dto_timer
    Timer for broken data transfer over scheme.

.. _`dw_mci.description`:

Description
-----------

Locking
=======

\ ``lock``\  is a softirq-safe spinlock protecting \ ``queue``\  as well as
at the same time while holding \ ``lock``\ .

\ ``irq_lock``\  is an irq-safe spinlock protecting the INTMASK register
to allow the interrupt handler to modify it directly.  Held for only long
enough to read-modify-write INTMASK and no other locks are grabbed when
holding this one.

The \ ``mrq``\  field of struct dw_mci_slot is also protected by \ ``lock``\ ,
and must always be written at the same time as the slot is added to
\ ``queue``\ .

\ ``pending_events``\  and \ ``completed_events``\  are accessed using atomic bit
operations, so they don't need any locking.

None of the fields touched by the interrupt handler need any
locking. However, ordering is important: Before EVENT_DATA_ERROR or
EVENT_DATA_COMPLETE is set in \ ``pending_events``\ , all data-related
interrupts must be disabled and \ ``data_status``\  updated with a
snapshot of SR. Similarly, before EVENT_CMD_COMPLETE is set, the
CMDRDY interrupt must be disabled and \ ``cmd_status``\  updated with a
snapshot of SR, and before EVENT_XFER_COMPLETE can be set, the
bytes_xfered field of \ ``data``\  must be written. This is ensured by
using barriers.

.. _`dw_mci_slot`:

struct dw_mci_slot
==================

.. c:type:: struct dw_mci_slot

    MMC slot state

.. _`dw_mci_slot.definition`:

Definition
----------

.. code-block:: c

    struct dw_mci_slot {
        struct mmc_host *mmc;
        struct dw_mci *host;
        u32 ctype;
        struct mmc_request *mrq;
        struct list_head queue_node;
        unsigned int clock;
        unsigned int __clk_old;
        unsigned long flags;
    #define DW_MMC_CARD_PRESENT 0
    #define DW_MMC_CARD_NEED_INIT 1
    #define DW_MMC_CARD_NO_LOW_PWR 2
    #define DW_MMC_CARD_NO_USE_HOLD 3
    #define DW_MMC_CARD_NEEDS_POLL 4
        int id;
        int sdio_id;
    }

.. _`dw_mci_slot.members`:

Members
-------

mmc
    The mmc_host representing this slot.

host
    The MMC controller this slot is using.

ctype
    Card type for this slot.

mrq
    mmc_request currently being processed or waiting to be
    processed, or NULL when the slot is idle.

queue_node
    List node for placing this node in the \ ``queue``\  list of
    \ :c:type:`struct dw_mci <dw_mci>`\ .

clock
    Clock rate configured by \ :c:func:`set_ios`\ . Protected by host->lock.

__clk_old
    The last clock value that was requested from core.
    Keeping track of this helps us to avoid spamming the console.

flags
    Random state bits associated with the slot.

id
    Number of this slot.

sdio_id
    Number of this slot in the SDIO interrupt registers.

.. This file was automatic generated / don't edit.

