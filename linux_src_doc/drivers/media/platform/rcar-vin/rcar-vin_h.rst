.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/rcar-vin/rcar-vin.h

.. _`rvin_source_fmt`:

struct rvin_source_fmt
======================

.. c:type:: struct rvin_source_fmt

    Source information

.. _`rvin_source_fmt.definition`:

Definition
----------

.. code-block:: c

    struct rvin_source_fmt {
        u32 width;
        u32 height;
    }

.. _`rvin_source_fmt.members`:

Members
-------

width
    Width from source

height
    Height from source

.. _`rvin_video_format`:

struct rvin_video_format
========================

.. c:type:: struct rvin_video_format

    Data format stored in memory

.. _`rvin_video_format.definition`:

Definition
----------

.. code-block:: c

    struct rvin_video_format {
        u32 fourcc;
        u8 bpp;
    }

.. _`rvin_video_format.members`:

Members
-------

fourcc
    Pixelformat

bpp
    Bytes per pixel

.. _`rvin_graph_entity`:

struct rvin_graph_entity
========================

.. c:type:: struct rvin_graph_entity

    Video endpoint from async framework

.. _`rvin_graph_entity.definition`:

Definition
----------

.. code-block:: c

    struct rvin_graph_entity {
        struct v4l2_async_subdev asd;
        struct v4l2_subdev *subdev;
        u32 code;
        struct v4l2_mbus_config mbus_cfg;
        unsigned int source_pad;
        unsigned int sink_pad;
    }

.. _`rvin_graph_entity.members`:

Members
-------

asd
    sub-device descriptor for async framework

subdev
    subdevice matched using async framework

code
    Media bus format from source

mbus_cfg
    Media bus format from DT

source_pad
    source pad of remote subdevice

sink_pad
    sink pad of remote subdevice

.. _`rvin_dev`:

struct rvin_dev
===============

.. c:type:: struct rvin_dev

    Renesas VIN device structure

.. _`rvin_dev.definition`:

Definition
----------

.. code-block:: c

    struct rvin_dev {
        struct device *dev;
        void __iomem *base;
        enum chip_id chip;
        struct video_device vdev;
        struct v4l2_device v4l2_dev;
        struct v4l2_ctrl_handler ctrl_handler;
        struct v4l2_async_notifier notifier;
        struct rvin_graph_entity digital;
        struct mutex lock;
        struct vb2_queue queue;
        spinlock_t qlock;
        struct vb2_v4l2_buffer *queue_buf[HW_BUFFER_NUM];
        struct list_head buf_list;
        bool continuous;
        unsigned int sequence;
        enum rvin_dma_state state;
        struct rvin_source_fmt source;
        struct v4l2_pix_format format;
        struct v4l2_rect crop;
        struct v4l2_rect compose;
    }

.. _`rvin_dev.members`:

Members
-------

dev
    (OF) device

base
    device I/O register space remapped to virtual memory

chip
    type of VIN chip

vdev
    V4L2 video device associated with VIN

v4l2_dev
    V4L2 device

ctrl_handler
    V4L2 control handler

notifier
    V4L2 asynchronous subdevs notifier

digital
    entity in the DT for local digital subdevice

lock
    protects \ ``queue``\ 

queue
    vb2 buffers queue

qlock
    protects \ ``queue_buf``\ , \ ``buf_list``\ , \ ``continuous``\ , \ ``sequence``\ 
    \ ``state``\ 

queue_buf
    Keeps track of buffers given to HW slot

buf_list
    list of queued buffers

continuous
    tracks if active operation is continuous or single mode

sequence
    V4L2 buffers sequence number

state
    keeps track of operation state

source
    active format from the video source

format
    active V4L2 pixel format

crop
    active cropping

compose
    active composing

.. This file was automatic generated / don't edit.

