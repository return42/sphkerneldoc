.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ep93xx_dma.c

.. _`ep93xx_dma_desc`:

struct ep93xx_dma_desc
======================

.. c:type:: struct ep93xx_dma_desc

    EP93xx specific transaction descriptor

.. _`ep93xx_dma_desc.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_dma_desc {
        u32 src_addr;
        u32 dst_addr;
        size_t size;
        bool complete;
        struct dma_async_tx_descriptor txd;
        struct list_head tx_list;
        struct list_head node;
    }

.. _`ep93xx_dma_desc.members`:

Members
-------

src_addr
    source address of the transaction

dst_addr
    destination address of the transaction

size
    size of the transaction (in bytes)

complete
    this descriptor is completed

txd
    dmaengine API descriptor

tx_list
    list of linked descriptors

node
    link used for putting this into a channel queue

.. _`ep93xx_dma_chan`:

struct ep93xx_dma_chan
======================

.. c:type:: struct ep93xx_dma_chan

    an EP93xx DMA M2P/M2M channel

.. _`ep93xx_dma_chan.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_dma_chan {
        struct dma_chan chan;
        const struct ep93xx_dma_engine *edma;
        void __iomem *regs;
        int irq;
        struct clk *clk;
        struct tasklet_struct tasklet;
        spinlock_t lock;
        unsigned long flags;
        #define EP93XX_DMA_IS_CYCLIC 0
        int buffer;
        struct list_head active;
        struct list_head queue;
        struct list_head free_list;
        u32 runtime_addr;
        u32 runtime_ctrl;
    }

.. _`ep93xx_dma_chan.members`:

Members
-------

chan
    dmaengine API channel

edma
    pointer to to the engine device

regs
    memory mapped registers

irq
    interrupt number of the channel

clk
    clock used by this channel

tasklet
    channel specific tasklet used for callbacks

lock
    lock protecting the fields following

flags
    flags for the channel

buffer
    which buffer to use next (0/1)

active
    flattened chain of descriptors currently being processed

queue
    pending descriptors which are handled next

free_list
    list of free descriptors which can be used

runtime_addr
    physical address currently used as dest/src (M2M only). This
    is set via .device_config before slave operation is
    prepared

runtime_ctrl
    M2M runtime values for the control register.

.. _`ep93xx_dma_chan.description`:

Description
-----------

As EP93xx DMA controller doesn't support real chained DMA descriptors we

.. _`ep93xx_dma_chan.will-have-slightly-different-scheme-here`:

will have slightly different scheme here
----------------------------------------

\ ``active``\  points to a head of
flattened DMA descriptor chain.

\ ``queue``\  holds pending transactions. These are linked through the first
descriptor in the chain. When a descriptor is moved to the \ ``active``\  queue,
the first and chained descriptors are flattened into a single list.

\ ``chan``\ .private holds pointer to \ :c:type:`struct ep93xx_dma_data <ep93xx_dma_data>`\  which contains
necessary channel configuration information. For memcpy channels this must
be \ ``NULL``\ .

.. _`ep93xx_dma_engine`:

struct ep93xx_dma_engine
========================

.. c:type:: struct ep93xx_dma_engine

    the EP93xx DMA engine instance

.. _`ep93xx_dma_engine.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_dma_engine {
        struct dma_device dma_dev;
        bool m2m;
        int (*hw_setup)(struct ep93xx_dma_chan *);
        void (*hw_shutdown)(struct ep93xx_dma_chan *);
        void (*hw_submit)(struct ep93xx_dma_chan *);
        int (*hw_interrupt)(struct ep93xx_dma_chan *);
        #define INTERRUPT_UNKNOWN 0
        #define INTERRUPT_DONE 1
        #define INTERRUPT_NEXT_BUFFER 2
        size_t num_channels;
        struct ep93xx_dma_chan channels[];
    }

.. _`ep93xx_dma_engine.members`:

Members
-------

dma_dev
    holds the dmaengine device

m2m
    is this an M2M or M2P device

hw_setup
    method which sets the channel up for operation

hw_shutdown
    shuts the channel down and flushes whatever is left

hw_submit
    pushes active descriptor(s) to the hardware

hw_interrupt
    handle the interrupt

num_channels
    number of channels for this instance

channels
    array of channels

.. _`ep93xx_dma_engine.description`:

Description
-----------

There is one instance of this struct for the M2P channels and one for the
M2M channels. \ :c:func:`hw_xxx`\  methods are used to perform operations which are
different on M2M and M2P channels. These methods are called with channel
lock held and interrupts disabled so they cannot sleep.

.. _`ep93xx_dma_set_active`:

ep93xx_dma_set_active
=====================

.. c:function:: void ep93xx_dma_set_active(struct ep93xx_dma_chan *edmac, struct ep93xx_dma_desc *desc)

    set new active descriptor chain

    :param struct ep93xx_dma_chan \*edmac:
        channel

    :param struct ep93xx_dma_desc \*desc:
        head of the new active descriptor chain

.. _`ep93xx_dma_set_active.description`:

Description
-----------

Sets \ ``desc``\  to be the head of the new active descriptor chain. This is the
chain which is processed next. The active list must be empty before calling
this function.

Called with \ ``edmac``\ ->lock held and interrupts disabled.

.. _`ep93xx_dma_advance_active`:

ep93xx_dma_advance_active
=========================

.. c:function:: bool ep93xx_dma_advance_active(struct ep93xx_dma_chan *edmac)

    advances to the next active descriptor

    :param struct ep93xx_dma_chan \*edmac:
        channel

.. _`ep93xx_dma_advance_active.description`:

Description
-----------

Function advances active descriptor to the next in the \ ``edmac``\ ->active and
returns \ ``true``\  if we still have descriptors in the chain to process.
Otherwise returns \ ``false``\ .

When the channel is in cyclic mode always returns \ ``true``\ .

Called with \ ``edmac``\ ->lock held and interrupts disabled.

.. _`ep93xx_dma_advance_work`:

ep93xx_dma_advance_work
=======================

.. c:function:: void ep93xx_dma_advance_work(struct ep93xx_dma_chan *edmac)

    start processing the next pending transaction

    :param struct ep93xx_dma_chan \*edmac:
        channel

.. _`ep93xx_dma_advance_work.description`:

Description
-----------

If we have pending transactions queued and we are currently idling, this
function takes the next queued transaction from the \ ``edmac``\ ->queue and
pushes it to the hardware for execution.

.. _`ep93xx_dma_tx_submit`:

ep93xx_dma_tx_submit
====================

.. c:function:: dma_cookie_t ep93xx_dma_tx_submit(struct dma_async_tx_descriptor *tx)

    set the prepared descriptor(s) to be executed

    :param struct dma_async_tx_descriptor \*tx:
        descriptor to be executed

.. _`ep93xx_dma_tx_submit.description`:

Description
-----------

Function will execute given descriptor on the hardware or if the hardware
is busy, queue the descriptor to be executed later on. Returns cookie which
can be used to poll the status of the descriptor.

.. _`ep93xx_dma_alloc_chan_resources`:

ep93xx_dma_alloc_chan_resources
===============================

.. c:function:: int ep93xx_dma_alloc_chan_resources(struct dma_chan *chan)

    allocate resources for the channel

    :param struct dma_chan \*chan:
        channel to allocate resources

.. _`ep93xx_dma_alloc_chan_resources.description`:

Description
-----------

Function allocates necessary resources for the given DMA channel and
returns number of allocated descriptors for the channel. Negative errno
is returned in case of failure.

.. _`ep93xx_dma_free_chan_resources`:

ep93xx_dma_free_chan_resources
==============================

.. c:function:: void ep93xx_dma_free_chan_resources(struct dma_chan *chan)

    release resources for the channel

    :param struct dma_chan \*chan:
        channel

.. _`ep93xx_dma_free_chan_resources.description`:

Description
-----------

Function releases all the resources allocated for the given channel.
The channel must be idle when this is called.

.. _`ep93xx_dma_prep_dma_memcpy`:

ep93xx_dma_prep_dma_memcpy
==========================

.. c:function:: struct dma_async_tx_descriptor *ep93xx_dma_prep_dma_memcpy(struct dma_chan *chan, dma_addr_t dest, dma_addr_t src, size_t len, unsigned long flags)

    prepare a memcpy DMA operation

    :param struct dma_chan \*chan:
        channel

    :param dma_addr_t dest:
        destination bus address

    :param dma_addr_t src:
        source bus address

    :param size_t len:
        size of the transaction

    :param unsigned long flags:
        flags for the descriptor

.. _`ep93xx_dma_prep_dma_memcpy.description`:

Description
-----------

Returns a valid DMA descriptor or \ ``NULL``\  in case of failure.

.. _`ep93xx_dma_prep_slave_sg`:

ep93xx_dma_prep_slave_sg
========================

.. c:function:: struct dma_async_tx_descriptor *ep93xx_dma_prep_slave_sg(struct dma_chan *chan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction dir, unsigned long flags, void *context)

    prepare a slave DMA operation

    :param struct dma_chan \*chan:
        channel

    :param struct scatterlist \*sgl:
        list of buffers to transfer

    :param unsigned int sg_len:
        number of entries in \ ``sgl``\ 

    :param enum dma_transfer_direction dir:
        direction of tha DMA transfer

    :param unsigned long flags:
        flags for the descriptor

    :param void \*context:
        operation context (ignored)

.. _`ep93xx_dma_prep_slave_sg.description`:

Description
-----------

Returns a valid DMA descriptor or \ ``NULL``\  in case of failure.

.. _`ep93xx_dma_prep_dma_cyclic`:

ep93xx_dma_prep_dma_cyclic
==========================

.. c:function:: struct dma_async_tx_descriptor *ep93xx_dma_prep_dma_cyclic(struct dma_chan *chan, dma_addr_t dma_addr, size_t buf_len, size_t period_len, enum dma_transfer_direction dir, unsigned long flags)

    prepare a cyclic DMA operation

    :param struct dma_chan \*chan:
        channel

    :param dma_addr_t dma_addr:
        DMA mapped address of the buffer

    :param size_t buf_len:
        length of the buffer (in bytes)

    :param size_t period_len:
        length of a single period

    :param enum dma_transfer_direction dir:
        direction of the operation

    :param unsigned long flags:
        tx descriptor status flags

.. _`ep93xx_dma_prep_dma_cyclic.description`:

Description
-----------

Prepares a descriptor for cyclic DMA operation. This means that once the
descriptor is submitted, we will be submitting in a \ ``period_len``\  sized
buffers and calling callback once the period has been elapsed. Transfer
terminates only when client calls \ :c:func:`dmaengine_terminate_all`\  for this
channel.

Returns a valid DMA descriptor or \ ``NULL``\  in case of failure.

.. _`ep93xx_dma_terminate_all`:

ep93xx_dma_terminate_all
========================

.. c:function:: int ep93xx_dma_terminate_all(struct dma_chan *chan)

    terminate all transactions

    :param struct dma_chan \*chan:
        channel

.. _`ep93xx_dma_terminate_all.description`:

Description
-----------

Stops all DMA transactions. All descriptors are put back to the
\ ``edmac``\ ->free_list and callbacks are \_not\_ called.

.. _`ep93xx_dma_tx_status`:

ep93xx_dma_tx_status
====================

.. c:function:: enum dma_status ep93xx_dma_tx_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *state)

    check if a transaction is completed

    :param struct dma_chan \*chan:
        channel

    :param dma_cookie_t cookie:
        transaction specific cookie

    :param struct dma_tx_state \*state:
        state of the transaction is stored here if given

.. _`ep93xx_dma_tx_status.description`:

Description
-----------

This function can be used to query state of a given transaction.

.. _`ep93xx_dma_issue_pending`:

ep93xx_dma_issue_pending
========================

.. c:function:: void ep93xx_dma_issue_pending(struct dma_chan *chan)

    push pending transactions to the hardware

    :param struct dma_chan \*chan:
        channel

.. _`ep93xx_dma_issue_pending.description`:

Description
-----------

When this function is called, all pending transactions are pushed to the
hardware and executed.

.. This file was automatic generated / don't edit.

