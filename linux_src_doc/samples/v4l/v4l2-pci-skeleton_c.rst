.. -*- coding: utf-8; mode: rst -*-
.. src-file: samples/v4l/v4l2-pci-skeleton.c

.. _`skeleton`:

struct skeleton
===============

.. c:type:: struct skeleton

    All internal data for one instance of device

.. _`skeleton.definition`:

Definition
----------

.. code-block:: c

    struct skeleton {
        struct pci_dev *pdev;
        struct v4l2_device v4l2_dev;
        struct video_device vdev;
        struct v4l2_ctrl_handler ctrl_handler;
        struct mutex lock;
        v4l2_std_id std;
        struct v4l2_dv_timings timings;
        struct v4l2_pix_format format;
        unsigned input;
        struct vb2_queue queue;
        struct vb2_alloc_ctx *alloc_ctx;
        spinlock_t qlock;
        struct list_head buf_list;
        unsigned field;
        unsigned sequence;
    }

.. _`skeleton.members`:

Members
-------

pdev
    PCI device

v4l2_dev
    top-level v4l2 device struct

vdev
    video node structure

ctrl_handler
    control handler structure

lock
    ioctl serialization mutex

std
    current SDTV standard

timings
    current HDTV timings

format
    current pix format

input
    current video input (0 = SDTV, 1 = HDTV)

queue
    vb2 video capture queue

alloc_ctx
    vb2 contiguous DMA context

qlock
    spinlock controlling access to buf_list and sequence

buf_list
    list of buffers queued for DMA

field
    *undescribed*

sequence
    frame sequence counter

.. This file was automatic generated / don't edit.

