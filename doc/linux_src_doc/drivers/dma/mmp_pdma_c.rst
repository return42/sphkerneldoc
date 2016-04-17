.. -*- coding: utf-8; mode: rst -*-

==========
mmp_pdma.c
==========


.. _`start_pending_queue`:

start_pending_queue
===================

.. c:function:: void start_pending_queue (struct mmp_pdma_chan *chan)

    transfer any pending transactions pending list ==> running list

    :param struct mmp_pdma_chan \*chan:

        *undescribed*



.. _`mmp_pdma_alloc_chan_resources`:

mmp_pdma_alloc_chan_resources
=============================

.. c:function:: int mmp_pdma_alloc_chan_resources (struct dma_chan *dchan)

    Allocate resources for DMA channel.

    :param struct dma_chan \*dchan:

        *undescribed*



.. _`mmp_pdma_alloc_chan_resources.description`:

Description
-----------


This function will create a dma pool for descriptor allocation.
Request irq only when channel is requested
Return - The number of allocated descriptors.



.. _`mmp_pdma_issue_pending`:

mmp_pdma_issue_pending
======================

.. c:function:: void mmp_pdma_issue_pending (struct dma_chan *dchan)

    Issue the DMA start command pending list ==> running list

    :param struct dma_chan \*dchan:

        *undescribed*

