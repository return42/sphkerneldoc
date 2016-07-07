.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-dma.h

.. _`xvip_pipeline`:

struct xvip_pipeline
====================

.. c:type:: struct xvip_pipeline

    Xilinx Video IP pipeline structure

.. _`xvip_pipeline.definition`:

Definition
----------

.. code-block:: c

    struct xvip_pipeline {
        struct media_pipeline pipe;
        struct mutex lock;
        unsigned int use_count;
        unsigned int stream_count;
        unsigned int num_dmas;
        struct xvip_dma *output;
    }

.. _`xvip_pipeline.members`:

Members
-------

pipe
    media pipeline

lock
    protects the pipeline \ ``stream_count``\ 

use_count
    number of DMA engines using the pipeline

stream_count
    number of DMA engines currently streaming

num_dmas
    number of DMA engines in the pipeline

output
    DMA engine at the output of the pipeline

.. _`xvip_dma`:

struct xvip_dma
===============

.. c:type:: struct xvip_dma

    Video DMA channel

.. _`xvip_dma.definition`:

Definition
----------

.. code-block:: c

    struct xvip_dma {
        struct list_head list;
        struct video_device video;
        struct media_pad pad;
        struct xvip_composite_device *xdev;
        struct xvip_pipeline pipe;
        unsigned int port;
        struct mutex lock;
        struct v4l2_pix_format format;
        const struct xvip_video_format *fmtinfo;
        struct vb2_queue queue;
        void *alloc_ctx;
        unsigned int sequence;
        struct list_head queued_bufs;
        spinlock_t queued_lock;
        struct dma_chan *dma;
        unsigned int align;
        struct dma_interleaved_template xt;
        struct data_chunk sgl[1];
    }

.. _`xvip_dma.members`:

Members
-------

list
    list entry in a composite device dmas list

video
    V4L2 video device associated with the DMA channel

pad
    media pad for the video device entity

xdev
    composite device the DMA channel belongs to

pipe
    pipeline belonging to the DMA channel

port
    composite device DT node port number for the DMA channel

lock
    protects the \ ``format``\ , \ ``fmtinfo``\  and \ ``queue``\  fields

format
    active V4L2 pixel format

fmtinfo
    format information corresponding to the active \ ``format``\ 

queue
    vb2 buffers queue

alloc_ctx
    allocation context for the vb2 \ ``queue``\ 

sequence
    V4L2 buffers sequence number

queued_bufs
    list of queued buffers

queued_lock
    protects the buf_queued list

dma
    DMA engine channel

align
    transfer alignment required by the DMA channel (in bytes)

xt
    dma interleaved template for dma configuration

sgl
    data chunk structure for dma_interleaved_template

.. This file was automatic generated / don't edit.

