.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/atmel-mci.c

.. _`atmel_mci`:

struct atmel_mci
================

.. c:type:: struct atmel_mci

    MMC controller state shared between all slots

.. _`atmel_mci.definition`:

Definition
----------

.. code-block:: c

    struct atmel_mci {
        spinlock_t lock;
        void __iomem *regs;
        struct scatterlist *sg;
        unsigned int sg_len;
        unsigned int pio_offset;
        unsigned int *buffer;
        unsigned int buf_size;
        dma_addr_t buf_phys_addr;
        struct atmel_mci_slot *cur_slot;
        struct mmc_request *mrq;
        struct mmc_command *cmd;
        struct mmc_data *data;
        unsigned int data_size;
        struct atmel_mci_dma dma;
        struct dma_chan *data_chan;
        struct dma_slave_config dma_conf;
        u32 cmd_status;
        u32 data_status;
        u32 stop_cmdr;
        struct tasklet_struct tasklet;
        unsigned long pending_events;
        unsigned long completed_events;
        enum atmel_mci_state state;
        struct list_head queue;
        bool need_clock_update;
        bool need_reset;
        struct timer_list timer;
        u32 mode_reg;
        u32 cfg_reg;
        unsigned long bus_hz;
        unsigned long mapbase;
        struct clk *mck;
        struct platform_device *pdev;
        struct atmel_mci_slot  *slot[ATMCI_MAX_NR_SLOTS];
        struct atmel_mci_caps caps;
        u32 (*prepare_data)(struct atmel_mci *host, struct mmc_data *data);
        void (*submit_data)(struct atmel_mci *host, struct mmc_data *data);
        void (*stop_transfer)(struct atmel_mci *host);
    }

.. _`atmel_mci.members`:

Members
-------

lock
    Spinlock protecting the queue and associated data.

regs
    Pointer to MMIO registers.

sg
    Scatterlist entry currently being processed by PIO or PDC code.

sg_len
    *undescribed*

pio_offset
    Offset into the current scatterlist entry.

buffer
    Buffer used if we don't have the r/w proof capability. We
    don't have the time to switch pdc buffers so we have to use only
    one buffer for the full transaction.

buf_size
    size of the buffer.

buf_phys_addr
    *undescribed*

cur_slot
    The slot which is currently using the controller.

mrq
    The request currently being processed on \ ``cur_slot``\ ,
    or NULL if the controller is idle.

cmd
    The command currently being sent to the card, or NULL.

data
    The data currently being transferred, or NULL if no data
    transfer is in progress.

data_size
    just data->blocks \* data->blksz.

dma
    DMA client state.

data_chan
    DMA channel being used for the current data transfer.

dma_conf
    *undescribed*

cmd_status
    Snapshot of SR taken upon completion of the current
    command. Only valid when EVENT_CMD_COMPLETE is pending.

data_status
    Snapshot of SR taken upon completion of the current
    data transfer. Only valid when EVENT_DATA_COMPLETE or
    EVENT_DATA_ERROR is pending.

stop_cmdr
    Value to be loaded into CMDR when the stop command is
    to be sent.

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

need_clock_update
    Update the clock rate before the next request.

need_reset
    Reset controller before next request.

timer
    Timer to balance the data timeout error flag which cannot rise.

mode_reg
    Value of the MR register.

cfg_reg
    Value of the CFG register.

bus_hz
    The rate of \ ``mck``\  in Hz. This forms the basis for MMC bus
    rate and timeout calculations.

mapbase
    Physical address of the MMIO registers.

mck
    The peripheral bus clock hooked up to the MMC controller.

pdev
    Platform device associated with the MMC controller.

slot
    Slots sharing this MMC controller.

caps
    MCI capabilities depending on MCI version.

prepare_data
    function to setup MCI before data transfer which
    depends on MCI capabilities.

submit_data
    function to start data transfer which depends on MCI
    capabilities.

stop_transfer
    function to stop data transfer which depends on MCI
    capabilities.

.. _`atmel_mci.description`:

Description
-----------

Locking
=======

\ ``lock``\  is a softirq-safe spinlock protecting \ ``queue``\  as well as
\ ``cur_slot``\ , \ ``mrq``\  and \ ``state``\ . These must always be updated
at the same time while holding \ ``lock``\ .

\ ``lock``\  also protects mode_reg and need_clock_update since these are
used to synchronize mode register updates with the queue
processing.

The \ ``mrq``\  field of struct atmel_mci_slot is also protected by \ ``lock``\ ,
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

.. _`atmel_mci_slot`:

struct atmel_mci_slot
=====================

.. c:type:: struct atmel_mci_slot

    MMC slot state

.. _`atmel_mci_slot.definition`:

Definition
----------

.. code-block:: c

    struct atmel_mci_slot {
        struct mmc_host *mmc;
        struct atmel_mci *host;
        u32 sdc_reg;
        u32 sdio_irq;
        struct mmc_request *mrq;
        struct list_head queue_node;
        unsigned int clock;
        unsigned long flags;
        #define ATMCI_CARD_PRESENT 0
        #define ATMCI_CARD_NEED_INIT 1
        #define ATMCI_SHUTDOWN 2
        int detect_pin;
        int wp_pin;
        bool detect_is_active_high;
        struct timer_list detect_timer;
    }

.. _`atmel_mci_slot.members`:

Members
-------

mmc
    The mmc_host representing this slot.

host
    The MMC controller this slot is using.

sdc_reg
    Value of SDCR to be written before using this slot.

sdio_irq
    SDIO irq mask for this slot.

mrq
    mmc_request currently being processed or waiting to be
    processed, or NULL when the slot is idle.

queue_node
    List node for placing this node in the \ ``queue``\  list of
    \ :c:type:`struct atmel_mci <atmel_mci>`\ .

clock
    Clock rate configured by \ :c:func:`set_ios`\ . Protected by host->lock.

flags
    Random state bits associated with the slot.

detect_pin
    GPIO pin used for card detection, or negative if not
    available.

wp_pin
    GPIO pin used for card write protect sending, or negative
    if not available.

detect_is_active_high
    The state of the detect pin when it is active.

detect_timer
    Timer used for debouncing \ ``detect_pin``\  interrupts.

.. This file was automatic generated / don't edit.

