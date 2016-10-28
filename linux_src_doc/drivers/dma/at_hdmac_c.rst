.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/at_hdmac.c

.. _`atc_alloc_descriptor`:

atc_alloc_descriptor
====================

.. c:function:: struct at_desc *atc_alloc_descriptor(struct dma_chan *chan, gfp_t gfp_flags)

    allocate and return an initialized descriptor

    :param struct dma_chan \*chan:
        the channel to allocate descriptors for

    :param gfp_t gfp_flags:
        GFP allocation flags

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

    :param struct at_dma_chan \*atchan:
        channel we want a new descriptor for

.. _`atc_desc_put`:

atc_desc_put
============

.. c:function:: void atc_desc_put(struct at_dma_chan *atchan, struct at_desc *desc)

    move a descriptor, including any children, to the free list

    :param struct at_dma_chan \*atchan:
        channel we work on

    :param struct at_desc \*desc:
        descriptor, at the head of a chain, to move to free list

.. _`atc_desc_chain`:

atc_desc_chain
==============

.. c:function:: void atc_desc_chain(struct at_desc **first, struct at_desc **prev, struct at_desc *desc)

    build chain adding a descriptor

    :param struct at_desc \*\*first:
        address of first descriptor of the chain

    :param struct at_desc \*\*prev:
        address of previous descriptor of the chain

    :param struct at_desc \*desc:
        descriptor to queue

.. _`atc_desc_chain.description`:

Description
-----------

Called from prep\_\* functions

.. _`atc_dostart`:

atc_dostart
===========

.. c:function:: void atc_dostart(struct at_dma_chan *atchan, struct at_desc *first)

    starts the DMA engine for real

    :param struct at_dma_chan \*atchan:
        the channel we want to start

    :param struct at_desc \*first:
        first descriptor in the list we want to begin with

.. _`atc_dostart.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_calc_bytes_left`:

atc_calc_bytes_left
===================

.. c:function:: int atc_calc_bytes_left(int current_len, u32 ctrla)

    calculates the number of bytes left according to the value read from CTRLA.

    :param int current_len:
        the number of bytes left before reading CTRLA

    :param u32 ctrla:
        the value of CTRLA

.. _`atc_get_bytes_left`:

atc_get_bytes_left
==================

.. c:function:: int atc_get_bytes_left(struct dma_chan *chan, dma_cookie_t cookie)

    get the number of bytes residue for a cookie

    :param struct dma_chan \*chan:
        DMA channel

    :param dma_cookie_t cookie:
        transaction identifier to check status of

.. _`atc_chain_complete`:

atc_chain_complete
==================

.. c:function:: void atc_chain_complete(struct at_dma_chan *atchan, struct at_desc *desc)

    finish work for one transaction chain

    :param struct at_dma_chan \*atchan:
        channel we work on

    :param struct at_desc \*desc:
        descriptor at the head of the chain we want do complete

.. _`atc_complete_all`:

atc_complete_all
================

.. c:function:: void atc_complete_all(struct at_dma_chan *atchan)

    finish work for all transactions

    :param struct at_dma_chan \*atchan:
        channel to complete transactions for

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

    :param struct at_dma_chan \*atchan:
        channel where the transaction ended

.. _`atc_advance_work.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_handle_error`:

atc_handle_error
================

.. c:function:: void atc_handle_error(struct at_dma_chan *atchan)

    handle errors reported by DMA controller

    :param struct at_dma_chan \*atchan:
        channel where error occurs

.. _`atc_handle_error.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_handle_cyclic`:

atc_handle_cyclic
=================

.. c:function:: void atc_handle_cyclic(struct at_dma_chan *atchan)

    at the end of a period, run callback function

    :param struct at_dma_chan \*atchan:
        channel used for cyclic operations

.. _`atc_handle_cyclic.description`:

Description
-----------

Called with atchan->lock held and bh disabled

.. _`atc_tx_submit`:

atc_tx_submit
=============

.. c:function:: dma_cookie_t atc_tx_submit(struct dma_async_tx_descriptor *tx)

    set the prepared descriptor(s) to be executed by the engine

    :param struct dma_async_tx_descriptor \*tx:
        *undescribed*

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

    :param struct dma_chan \*chan:
        the channel to prepare operation on

    :param struct dma_interleaved_template \*xt:
        Interleaved transfer template

    :param unsigned long flags:
        tx descriptor status flags

.. _`atc_prep_dma_memcpy`:

atc_prep_dma_memcpy
===================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_memcpy(struct dma_chan *chan, dma_addr_t dest, dma_addr_t src, size_t len, unsigned long flags)

    prepare a memcpy operation

    :param struct dma_chan \*chan:
        the channel to prepare operation on

    :param dma_addr_t dest:
        operation virtual destination address

    :param dma_addr_t src:
        operation virtual source address

    :param size_t len:
        operation length

    :param unsigned long flags:
        tx descriptor status flags

.. _`atc_prep_dma_memset`:

atc_prep_dma_memset
===================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_memset(struct dma_chan *chan, dma_addr_t dest, int value, size_t len, unsigned long flags)

    prepare a memcpy operation

    :param struct dma_chan \*chan:
        the channel to prepare operation on

    :param dma_addr_t dest:
        operation virtual destination address

    :param int value:
        value to set memory buffer to

    :param size_t len:
        operation length

    :param unsigned long flags:
        tx descriptor status flags

.. _`atc_prep_slave_sg`:

atc_prep_slave_sg
=================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_slave_sg(struct dma_chan *chan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction direction, unsigned long flags, void *context)

    prepare descriptors for a DMA_SLAVE transaction

    :param struct dma_chan \*chan:
        DMA channel

    :param struct scatterlist \*sgl:
        scatterlist to transfer to/from

    :param unsigned int sg_len:
        number of entries in \ ``scatterlist``\ 

    :param enum dma_transfer_direction direction:
        DMA direction

    :param unsigned long flags:
        tx descriptor status flags

    :param void \*context:
        transaction context (ignored)

.. _`atc_prep_dma_sg`:

atc_prep_dma_sg
===============

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_sg(struct dma_chan *chan, struct scatterlist *dst_sg, unsigned int dst_nents, struct scatterlist *src_sg, unsigned int src_nents, unsigned long flags)

    prepare memory to memory scather-gather operation

    :param struct dma_chan \*chan:
        the channel to prepare operation on

    :param struct scatterlist \*dst_sg:
        destination scatterlist

    :param unsigned int dst_nents:
        number of destination scatterlist entries

    :param struct scatterlist \*src_sg:
        source scatterlist

    :param unsigned int src_nents:
        number of source scatterlist entries

    :param unsigned long flags:
        tx descriptor status flags

.. _`atc_dma_cyclic_check_values`:

atc_dma_cyclic_check_values
===========================

.. c:function:: int atc_dma_cyclic_check_values(unsigned int reg_width, dma_addr_t buf_addr, size_t period_len)

    Check for too big/unaligned periods and unaligned DMA buffer

    :param unsigned int reg_width:
        *undescribed*

    :param dma_addr_t buf_addr:
        *undescribed*

    :param size_t period_len:
        *undescribed*

.. _`atc_dma_cyclic_fill_desc`:

atc_dma_cyclic_fill_desc
========================

.. c:function:: int atc_dma_cyclic_fill_desc(struct dma_chan *chan, struct at_desc *desc, unsigned int period_index, dma_addr_t buf_addr, unsigned int reg_width, size_t period_len, enum dma_transfer_direction direction)

    Fill one period descriptor

    :param struct dma_chan \*chan:
        *undescribed*

    :param struct at_desc \*desc:
        *undescribed*

    :param unsigned int period_index:
        *undescribed*

    :param dma_addr_t buf_addr:
        *undescribed*

    :param unsigned int reg_width:
        *undescribed*

    :param size_t period_len:
        *undescribed*

    :param enum dma_transfer_direction direction:
        *undescribed*

.. _`atc_prep_dma_cyclic`:

atc_prep_dma_cyclic
===================

.. c:function:: struct dma_async_tx_descriptor *atc_prep_dma_cyclic(struct dma_chan *chan, dma_addr_t buf_addr, size_t buf_len, size_t period_len, enum dma_transfer_direction direction, unsigned long flags)

    prepare the cyclic DMA transfer

    :param struct dma_chan \*chan:
        the DMA channel to prepare

    :param dma_addr_t buf_addr:
        physical DMA address where the buffer starts

    :param size_t buf_len:
        total number of bytes for the entire buffer

    :param size_t period_len:
        number of bytes for each period

    :param enum dma_transfer_direction direction:
        transfer direction, to or from device

    :param unsigned long flags:
        tx descriptor status flags

.. _`atc_tx_status`:

atc_tx_status
=============

.. c:function:: enum dma_status atc_tx_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    poll for transaction completion

    :param struct dma_chan \*chan:
        DMA channel

    :param dma_cookie_t cookie:
        transaction identifier to check status of

    :param struct dma_tx_state \*txstate:
        if not \ ``NULL``\  updated with transaction state

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

    :param struct dma_chan \*chan:
        target DMA channel

.. _`atc_alloc_chan_resources`:

atc_alloc_chan_resources
========================

.. c:function:: int atc_alloc_chan_resources(struct dma_chan *chan)

    allocate resources for DMA channel

    :param struct dma_chan \*chan:
        allocate descriptor resources for this channel

.. _`atc_alloc_chan_resources.description`:

Description
-----------

return - the number of allocated descriptors

.. _`atc_free_chan_resources`:

atc_free_chan_resources
=======================

.. c:function:: void atc_free_chan_resources(struct dma_chan *chan)

    free all channel resources

    :param struct dma_chan \*chan:
        DMA channel

.. _`at_dma_off`:

at_dma_off
==========

.. c:function:: void at_dma_off(struct at_dma *atdma)

    disable DMA controller

    :param struct at_dma \*atdma:
        the Atmel HDAMC device

.. This file was automatic generated / don't edit.

