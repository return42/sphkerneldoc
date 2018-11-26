.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/at_hdmac.c

.. _`atc_alloc_descriptor`:

atc_alloc_descriptor
====================

.. c:function:: struct at_desc *atc_alloc_descriptor(struct dma_chan *chan, gfp_t gfp_flags)

    allocate and return an initialized descriptor

    :param chan:
        the channel to allocate descriptors for
    :type chan: struct dma_chan \*

    :param gfp_flags:
        GFP allocation flags
    :type gfp_flags: gfp_t

.. _`atc_alloc_descriptor.note`:

Note
----

The ack-bit is positioned in the descriptor flag at creation time
to make initial allocation more convenient. This bit will be cleared
and control will be given to client at usage time (during
preparation functions).

.. _`atc_desc_get`:

atc_desc_get
============

.. c:function:: struct at_desc *atc_desc_get(struct at_dma_chan *atchan)

    get an unused descriptor from free_list

    :param atchan:
        channel we want a new descriptor for
    :type atchan: struct at_dma_chan \*

.. _`atc_desc_put`:

atc_desc_put
============

.. c:function:: void atc_desc_put(struct at_dma_chan *atchan, struct at_desc *desc)

    move a descriptor, including any children, to the free list

    :param atchan:
        channel we work on
    :type atchan: struct at_dma_chan \*

    :param desc:
        descriptor, at the head of a chain, to move to free list
    :type desc: struct at_desc \*

.. _`atc_desc_chain`:

atc_desc_chain
==============

.. c:function:: void atc_desc_chain(struct at_desc **first, struct at_desc **prev, struct at_desc *desc)

    build chain adding a descriptor

    :param first:
        address of first descriptor of the chain
    :type first: struct at_desc \*\*

    :param prev:
        address of previous descriptor of the chain
    :type prev: struct at_desc \*\*

    :param desc:
        descriptor to queue
    :type desc: struct at_desc \*

.. _`atc_desc_chain.description`:

Description
-----------

Called from prep\_\* functions

.. _`atc_dostart`:

atc_dostart
===========

.. c:function:: void atc_dostart(struct at_dma_chan *atchan, struct at_desc *first)

    starts the DMA engine for real

    :param atchan:
        the channel we want to start
    :type atchan: struct at_dma_chan \*

    :param first:
        first descriptor in the list we want to begin with
    :type first: struct at_desc \*

.. _`atc_dostart.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_calc_bytes_left`:

atc_calc_bytes_left
===================

.. c:function:: int atc_calc_bytes_left(int current_len, u32 ctrla)

    calculates the number of bytes left according to the value read from CTRLA.

    :param current_len:
        the number of bytes left before reading CTRLA
    :type current_len: int

    :param ctrla:
        the value of CTRLA
    :type ctrla: u32

.. _`atc_get_bytes_left`:

atc_get_bytes_left
==================

.. c:function:: int atc_get_bytes_left(struct dma_chan *chan, dma_cookie_t cookie)

    get the number of bytes residue for a cookie

    :param chan:
        DMA channel
    :type chan: struct dma_chan \*

    :param cookie:
        transaction identifier to check status of
    :type cookie: dma_cookie_t

.. _`atc_chain_complete`:

atc_chain_complete
==================

.. c:function:: void atc_chain_complete(struct at_dma_chan *atchan, struct at_desc *desc)

    finish work for one transaction chain

    :param atchan:
        channel we work on
    :type atchan: struct at_dma_chan \*

    :param desc:
        descriptor at the head of the chain we want do complete
    :type desc: struct at_desc \*

.. _`atc_complete_all`:

atc_complete_all
================

.. c:function:: void atc_complete_all(struct at_dma_chan *atchan)

    finish work for all transactions

    :param atchan:
        channel to complete transactions for
    :type atchan: struct at_dma_chan \*

.. _`atc_complete_all.description`:

Description
-----------

Eventually submit queued descriptors if any

Assume channel is idle while calling this function
Called with atchan->lock held and bh disabled

.. _`atc_advance_work`:

atc_advance_work
================

.. c:function:: void atc_advance_work(struct at_dma_chan *atchan)

    at the end of a transaction, move forward

    :param atchan:
        channel where the transaction ended
    :type atchan: struct at_dma_chan \*

.. _`atc_advance_work.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_handle_error`:

atc_handle_error
================

.. c:function:: void atc_handle_error(struct at_dma_chan *atchan)

    handle errors reported by DMA controller

    :param atchan:
        channel where error occurs
    :type atchan: struct at_dma_chan \*

.. _`atc_handle_error.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_handle_cyclic`:

atc_handle_cyclic
=================

.. c:function:: void atc_handle_cyclic(struct at_dma_chan *atchan)

    at the end of a period, run callback function

    :param atchan:
        channel used for cyclic operations
    :type atchan: struct at_dma_chan \*

.. _`atc_handle_cyclic.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_tx_submit`:

atc_tx_submit
=============

.. c:function:: dma_cookie_t atc_tx_submit(struct dma_async_tx_descriptor *tx)

    set the prepared descriptor(s) to be executed by the engine

    :param tx:
        *undescribed*
    :type tx: struct dma_async_tx_descriptor \*

.. _`atc_tx_submit.description`:

Description
-----------

Queue chain if DMA engine is working already

Cookie increment and adding to active_list or queue must be atomic

.. _`atc_prep_dma_interleaved`:

atc_prep_dma_interleaved
========================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_interleaved(struct dma_chan *chan, struct dma_interleaved_template *xt, unsigned long flags)

    prepare memory to memory interleaved operation

    :param chan:
        the channel to prepare operation on
    :type chan: struct dma_chan \*

    :param xt:
        Interleaved transfer template
    :type xt: struct dma_interleaved_template \*

    :param flags:
        tx descriptor status flags
    :type flags: unsigned long

.. _`atc_prep_dma_memcpy`:

atc_prep_dma_memcpy
===================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_memcpy(struct dma_chan *chan, dma_addr_t dest, dma_addr_t src, size_t len, unsigned long flags)

    prepare a memcpy operation

    :param chan:
        the channel to prepare operation on
    :type chan: struct dma_chan \*

    :param dest:
        operation virtual destination address
    :type dest: dma_addr_t

    :param src:
        operation virtual source address
    :type src: dma_addr_t

    :param len:
        operation length
    :type len: size_t

    :param flags:
        tx descriptor status flags
    :type flags: unsigned long

.. _`atc_prep_dma_memset`:

atc_prep_dma_memset
===================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_memset(struct dma_chan *chan, dma_addr_t dest, int value, size_t len, unsigned long flags)

    prepare a memcpy operation

    :param chan:
        the channel to prepare operation on
    :type chan: struct dma_chan \*

    :param dest:
        operation virtual destination address
    :type dest: dma_addr_t

    :param value:
        value to set memory buffer to
    :type value: int

    :param len:
        operation length
    :type len: size_t

    :param flags:
        tx descriptor status flags
    :type flags: unsigned long

.. _`atc_prep_slave_sg`:

atc_prep_slave_sg
=================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_slave_sg(struct dma_chan *chan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction direction, unsigned long flags, void *context)

    prepare descriptors for a DMA_SLAVE transaction

    :param chan:
        DMA channel
    :type chan: struct dma_chan \*

    :param sgl:
        scatterlist to transfer to/from
    :type sgl: struct scatterlist \*

    :param sg_len:
        number of entries in \ ``scatterlist``\ 
    :type sg_len: unsigned int

    :param direction:
        DMA direction
    :type direction: enum dma_transfer_direction

    :param flags:
        tx descriptor status flags
    :type flags: unsigned long

    :param context:
        transaction context (ignored)
    :type context: void \*

.. _`atc_dma_cyclic_check_values`:

atc_dma_cyclic_check_values
===========================

.. c:function:: int atc_dma_cyclic_check_values(unsigned int reg_width, dma_addr_t buf_addr, size_t period_len)

    Check for too big/unaligned periods and unaligned DMA buffer

    :param reg_width:
        *undescribed*
    :type reg_width: unsigned int

    :param buf_addr:
        *undescribed*
    :type buf_addr: dma_addr_t

    :param period_len:
        *undescribed*
    :type period_len: size_t

.. _`atc_dma_cyclic_fill_desc`:

atc_dma_cyclic_fill_desc
========================

.. c:function:: int atc_dma_cyclic_fill_desc(struct dma_chan *chan, struct at_desc *desc, unsigned int period_index, dma_addr_t buf_addr, unsigned int reg_width, size_t period_len, enum dma_transfer_direction direction)

    Fill one period descriptor

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param desc:
        *undescribed*
    :type desc: struct at_desc \*

    :param period_index:
        *undescribed*
    :type period_index: unsigned int

    :param buf_addr:
        *undescribed*
    :type buf_addr: dma_addr_t

    :param reg_width:
        *undescribed*
    :type reg_width: unsigned int

    :param period_len:
        *undescribed*
    :type period_len: size_t

    :param direction:
        *undescribed*
    :type direction: enum dma_transfer_direction

.. _`atc_prep_dma_cyclic`:

atc_prep_dma_cyclic
===================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_cyclic(struct dma_chan *chan, dma_addr_t buf_addr, size_t buf_len, size_t period_len, enum dma_transfer_direction direction, unsigned long flags)

    prepare the cyclic DMA transfer

    :param chan:
        the DMA channel to prepare
    :type chan: struct dma_chan \*

    :param buf_addr:
        physical DMA address where the buffer starts
    :type buf_addr: dma_addr_t

    :param buf_len:
        total number of bytes for the entire buffer
    :type buf_len: size_t

    :param period_len:
        number of bytes for each period
    :type period_len: size_t

    :param direction:
        transfer direction, to or from device
    :type direction: enum dma_transfer_direction

    :param flags:
        tx descriptor status flags
    :type flags: unsigned long

.. _`atc_tx_status`:

atc_tx_status
=============

.. c:function:: enum dma_status atc_tx_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    poll for transaction completion

    :param chan:
        DMA channel
    :type chan: struct dma_chan \*

    :param cookie:
        transaction identifier to check status of
    :type cookie: dma_cookie_t

    :param txstate:
        if not \ ``NULL``\  updated with transaction state
    :type txstate: struct dma_tx_state \*

.. _`atc_tx_status.description`:

Description
-----------

If \ ``txstate``\  is passed in, upon return it reflect the driver
internal state and can be used with \ :c:func:`dma_async_is_complete`\  to check
the status of multiple cookies without re-checking hardware state.

.. _`atc_issue_pending`:

atc_issue_pending
=================

.. c:function:: void atc_issue_pending(struct dma_chan *chan)

    try to finish work

    :param chan:
        target DMA channel
    :type chan: struct dma_chan \*

.. _`atc_alloc_chan_resources`:

atc_alloc_chan_resources
========================

.. c:function:: int atc_alloc_chan_resources(struct dma_chan *chan)

    allocate resources for DMA channel

    :param chan:
        allocate descriptor resources for this channel
    :type chan: struct dma_chan \*

.. _`atc_alloc_chan_resources.description`:

Description
-----------

return - the number of allocated descriptors

.. _`atc_free_chan_resources`:

atc_free_chan_resources
=======================

.. c:function:: void atc_free_chan_resources(struct dma_chan *chan)

    free all channel resources

    :param chan:
        DMA channel
    :type chan: struct dma_chan \*

.. _`at_dma_off`:

at_dma_off
==========

.. c:function:: void at_dma_off(struct at_dma *atdma)

    disable DMA controller

    :param atdma:
        the Atmel HDAMC device
    :type atdma: struct at_dma \*

.. This file was automatic generated / don't edit.

