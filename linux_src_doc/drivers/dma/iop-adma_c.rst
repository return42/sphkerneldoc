.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/iop-adma.c

.. _`iop_adma_free_slots`:

iop_adma_free_slots
===================

.. c:function:: void iop_adma_free_slots(struct iop_adma_desc_slot *slot)

    flags descriptor slots for reuse

    :param struct iop_adma_desc_slot \*slot:
        Slot to free
        Caller must hold \ :c:type:`iop_chan->lock <iop_chan>`\  while calling this function

.. _`iop_adma_alloc_chan_resources`:

iop_adma_alloc_chan_resources
=============================

.. c:function:: int iop_adma_alloc_chan_resources(struct dma_chan *chan)

    returns the number of allocated descriptors \ ``chan``\  - allocate descriptor resources for this channel \ ``client``\  - current client requesting the channel be ready for requests

    :param struct dma_chan \*chan:
        *undescribed*

.. _`iop_adma_alloc_chan_resources.note`:

Note
----

We keep the slots for 1 operation on iop_chan->chain at all times.  To
avoid deadlock, via async_xor, num_descs_in_pool must at a minimum be
greater than 2x the number slots needed to satisfy a device->max_xor
request.

.. _`iop_adma_status`:

iop_adma_status
===============

.. c:function:: enum dma_status iop_adma_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    poll the status of an ADMA transaction

    :param struct dma_chan \*chan:
        ADMA channel handle

    :param dma_cookie_t cookie:
        ADMA transaction identifier

    :param struct dma_tx_state \*txstate:
        a holder for the current state of the channel or NULL

.. This file was automatic generated / don't edit.

