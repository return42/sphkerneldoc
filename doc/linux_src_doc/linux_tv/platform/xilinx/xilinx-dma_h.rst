.. -*- coding: utf-8; mode: rst -*-

============
xilinx-dma.h
============



.. _xref_struct_xvip_pipeline:

struct xvip_pipeline
====================

.. c:type:: struct xvip_pipeline

    Xilinx Video IP pipeline structure



Definition
----------

.. code-block:: c

  struct xvip_pipeline {
    struct media_pipeline pipe;
    struct mutex lock;
    unsigned int use_count;
    unsigned int stream_count;
    unsigned int num_dmas;
    struct xvip_dma * output;
  };



Members
-------

:``struct media_pipeline pipe``:
    media pipeline

:``struct mutex lock``:
    protects the pipeline **stream_count**

:``unsigned int use_count``:
    number of DMA engines using the pipeline

:``unsigned int stream_count``:
    number of DMA engines currently streaming

:``unsigned int num_dmas``:
    number of DMA engines in the pipeline

:``struct xvip_dma * output``:
    DMA engine at the output of the pipeline





.. _xref_struct_xvip_dma:

struct xvip_dma
===============

.. c:type:: struct xvip_dma

    Video DMA channel



Definition
----------

.. code-block:: c

  struct xvip_dma {
    struct list_head list;
    struct video_device video;
    struct media_pad pad;
    struct xvip_composite_device * xdev;
    struct xvip_pipeline pipe;
    unsigned int port;
    struct mutex lock;
    struct v4l2_pix_format format;
    const struct xvip_video_format * fmtinfo;
    struct vb2_queue queue;
    void * alloc_ctx;
    unsigned int sequence;
    struct list_head queued_bufs;
    spinlock_t queued_lock;
    struct dma_chan * dma;
    unsigned int align;
    struct dma_interleaved_template xt;
    struct data_chunk sgl[1];
  };



Members
-------

:``struct list_head list``:
    list entry in a composite device dmas list

:``struct video_device video``:
    V4L2 video device associated with the DMA channel

:``struct media_pad pad``:
    media pad for the video device entity

:``struct xvip_composite_device * xdev``:
    composite device the DMA channel belongs to

:``struct xvip_pipeline pipe``:
    pipeline belonging to the DMA channel

:``unsigned int port``:
    composite device DT node port number for the DMA channel

:``struct mutex lock``:
    protects the **format**, **fmtinfo** and **queue** fields

:``struct v4l2_pix_format format``:
    active V4L2 pixel format

:``const struct xvip_video_format * fmtinfo``:
    format information corresponding to the active **format**

:``struct vb2_queue queue``:
    vb2 buffers queue

:``void * alloc_ctx``:
    allocation context for the vb2 **queue**

:``unsigned int sequence``:
    V4L2 buffers sequence number

:``struct list_head queued_bufs``:
    list of queued buffers

:``spinlock_t queued_lock``:
    protects the buf_queued list

:``struct dma_chan * dma``:
    DMA engine channel

:``unsigned int align``:
    transfer alignment required by the DMA channel (in bytes)

:``struct dma_interleaved_template xt``:
    dma interleaved template for dma configuration

:``struct data_chunk sgl[1]``:
    data chunk structure for dma_interleaved_template



