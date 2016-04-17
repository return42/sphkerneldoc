.. -*- coding: utf-8; mode: rst -*-

========
fsldma.c
========


.. _`fsl_chan_set_src_loop_size`:

fsl_chan_set_src_loop_size
==========================

.. c:function:: void fsl_chan_set_src_loop_size (struct fsldma_chan *chan, int size)

    Set source address hold transfer size

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param int size:
        Address loop size, 0 for disable loop



.. _`fsl_chan_set_src_loop_size.description`:

Description
-----------

The set source address hold transfer size. The source
address hold or loop transfer size is when the DMA transfer
data from source address (SA), if the loop size is 4, the DMA will
read data from SA, SA + 1, SA + 2, SA + 3, then loop back to SA,
SA + 1 ... and so on.



.. _`fsl_chan_set_dst_loop_size`:

fsl_chan_set_dst_loop_size
==========================

.. c:function:: void fsl_chan_set_dst_loop_size (struct fsldma_chan *chan, int size)

    Set destination address hold transfer size

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param int size:
        Address loop size, 0 for disable loop



.. _`fsl_chan_set_dst_loop_size.description`:

Description
-----------

The set destination address hold transfer size. The destination
address hold or loop transfer size is when the DMA transfer
data to destination address (TA), if the loop size is 4, the DMA will
write data to TA, TA + 1, TA + 2, TA + 3, then loop back to TA,
TA + 1 ... and so on.



.. _`fsl_chan_set_request_count`:

fsl_chan_set_request_count
==========================

.. c:function:: void fsl_chan_set_request_count (struct fsldma_chan *chan, int size)

    Set DMA Request Count for external control

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param int size:
        Number of bytes to transfer in a single request



.. _`fsl_chan_set_request_count.description`:

Description
-----------

The Freescale DMA channel can be controlled by the external signal DREQ#.
The DMA request count is how many bytes are allowed to transfer before
pausing the channel, after which a new assertion of DREQ# resumes channel
operation.

A size of 0 disables external pause control. The maximum size is 1024.



.. _`fsl_chan_toggle_ext_pause`:

fsl_chan_toggle_ext_pause
=========================

.. c:function:: void fsl_chan_toggle_ext_pause (struct fsldma_chan *chan, int enable)

    Toggle channel external pause status

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param int enable:
        0 is disabled, 1 is enabled.



.. _`fsl_chan_toggle_ext_pause.description`:

Description
-----------

The Freescale DMA channel can be controlled by the external signal DREQ#.
The DMA Request Count feature should be used in addition to this feature
to set the number of bytes to transfer before pausing the channel.



.. _`fsl_chan_toggle_ext_start`:

fsl_chan_toggle_ext_start
=========================

.. c:function:: void fsl_chan_toggle_ext_start (struct fsldma_chan *chan, int enable)

    Toggle channel external start status

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param int enable:
        0 is disabled, 1 is enabled.



.. _`fsl_chan_toggle_ext_start.description`:

Description
-----------

If enable the external start, the channel can be started by an
external DMA start pin. So the :c:func:`dma_start` does not start the
transfer immediately. The DMA channel will wait for the
control pin asserted.



.. _`fsl_dma_free_descriptor`:

fsl_dma_free_descriptor
=======================

.. c:function:: void fsl_dma_free_descriptor (struct fsldma_chan *chan, struct fsl_desc_sw *desc)

    Free descriptor from channel's DMA pool.

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param struct fsl_desc_sw \*desc:
        descriptor to be freed



.. _`fsl_dma_alloc_descriptor`:

fsl_dma_alloc_descriptor
========================

.. c:function:: struct fsl_desc_sw *fsl_dma_alloc_descriptor (struct fsldma_chan *chan)

    Allocate descriptor from channel's DMA pool.

    :param struct fsldma_chan \*chan:
        Freescale DMA channel



.. _`fsl_dma_alloc_descriptor.description`:

Description
-----------

Return - The descriptor allocated. NULL for failed.



.. _`fsldma_clean_completed_descriptor`:

fsldma_clean_completed_descriptor
=================================

.. c:function:: void fsldma_clean_completed_descriptor (struct fsldma_chan *chan)

    free all descriptors which has been completed and acked

    :param struct fsldma_chan \*chan:
        Freescale DMA channel



.. _`fsldma_clean_completed_descriptor.description`:

Description
-----------

This function is used on all completed and acked descriptors.
All descriptors should only be freed in this function.



.. _`fsldma_run_tx_complete_actions`:

fsldma_run_tx_complete_actions
==============================

.. c:function:: dma_cookie_t fsldma_run_tx_complete_actions (struct fsldma_chan *chan, struct fsl_desc_sw *desc, dma_cookie_t cookie)

    cleanup a single link descriptor

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param struct fsl_desc_sw \*desc:
        descriptor to cleanup and free

    :param dma_cookie_t cookie:
        Freescale DMA transaction identifier



.. _`fsldma_run_tx_complete_actions.description`:

Description
-----------

This function is used on a descriptor which has been executed by the DMA
controller. It will run any callbacks, submit any dependencies.



.. _`fsldma_clean_running_descriptor`:

fsldma_clean_running_descriptor
===============================

.. c:function:: void fsldma_clean_running_descriptor (struct fsldma_chan *chan, struct fsl_desc_sw *desc)

    move the completed descriptor from ld_running to ld_completed

    :param struct fsldma_chan \*chan:
        Freescale DMA channel

    :param struct fsl_desc_sw \*desc:
        the descriptor which is completed



.. _`fsldma_clean_running_descriptor.description`:

Description
-----------

Free the descriptor directly if acked by async_tx api, or move it to
queue ld_completed.



.. _`fsl_chan_xfer_ld_queue`:

fsl_chan_xfer_ld_queue
======================

.. c:function:: void fsl_chan_xfer_ld_queue (struct fsldma_chan *chan)

    transfer any pending transactions

    :param struct fsldma_chan \*chan:
        Freescale DMA channel



.. _`fsl_chan_xfer_ld_queue.hardware-state`:

HARDWARE STATE
--------------

idle



.. _`fsl_chan_xfer_ld_queue.locking`:

LOCKING
-------

must hold chan->desc_lock



.. _`fsldma_cleanup_descriptors`:

fsldma_cleanup_descriptors
==========================

.. c:function:: void fsldma_cleanup_descriptors (struct fsldma_chan *chan)

    cleanup link descriptors which are completed and move them to ld_completed to free until flag 'ack' is set

    :param struct fsldma_chan \*chan:
        Freescale DMA channel



.. _`fsldma_cleanup_descriptors.description`:

Description
-----------

This function is used on descriptors which have been executed by the DMA
controller. It will run any callbacks, submit any dependencies, then
free these descriptors if flag 'ack' is set.



.. _`fsl_dma_alloc_chan_resources`:

fsl_dma_alloc_chan_resources
============================

.. c:function:: int fsl_dma_alloc_chan_resources (struct dma_chan *dchan)

    Allocate resources for DMA channel.

    :param struct dma_chan \*dchan:

        *undescribed*



.. _`fsl_dma_alloc_chan_resources.description`:

Description
-----------

This function will create a dma pool for descriptor allocation.

Return - The number of descriptors allocated.



.. _`fsldma_free_desc_list`:

fsldma_free_desc_list
=====================

.. c:function:: void fsldma_free_desc_list (struct fsldma_chan *chan, struct list_head *list)

    Free all descriptors in a queue

    :param struct fsldma_chan \*chan:
        Freescae DMA channel

    :param struct list_head \*list:
        the list to free



.. _`fsldma_free_desc_list.locking`:

LOCKING
-------

must hold chan->desc_lock



.. _`fsl_dma_free_chan_resources`:

fsl_dma_free_chan_resources
===========================

.. c:function:: void fsl_dma_free_chan_resources (struct dma_chan *dchan)

    Free all resources of the channel.

    :param struct dma_chan \*dchan:

        *undescribed*



.. _`fsl_dma_memcpy_issue_pending`:

fsl_dma_memcpy_issue_pending
============================

.. c:function:: void fsl_dma_memcpy_issue_pending (struct dma_chan *dchan)

    Issue the DMA start command

    :param struct dma_chan \*dchan:

        *undescribed*



.. _`fsl_tx_status`:

fsl_tx_status
=============

.. c:function:: enum dma_status fsl_tx_status (struct dma_chan *dchan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    Determine the DMA status

    :param struct dma_chan \*dchan:

        *undescribed*

    :param dma_cookie_t cookie:

        *undescribed*

    :param struct dma_tx_state \*txstate:

        *undescribed*

