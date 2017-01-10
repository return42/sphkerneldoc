.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/dw_mmc.h

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

