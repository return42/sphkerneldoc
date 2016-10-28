.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/dma-coh901318.h

.. _`coh901318_filter_id`:

coh901318_filter_id
===================

.. c:function:: bool coh901318_filter_id(struct dma_chan *chan, void *chan_id)

    DMA channel filter function

    :param struct dma_chan \*chan:
        dma channel handle

    :param void \*chan_id:
        id of dma channel to be filter out

.. _`coh901318_filter_id.description`:

Description
-----------

In \ :c:func:`dma_request_channel`\  it specifies what channel id to be requested

.. This file was automatic generated / don't edit.

