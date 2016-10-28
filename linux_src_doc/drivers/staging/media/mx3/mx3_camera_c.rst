.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/mx3/mx3_camera.c

.. _`mx3_camera_dev`:

struct mx3_camera_dev
=====================

.. c:type:: struct mx3_camera_dev

    i.MX3x camera (CSI) object

.. _`mx3_camera_dev.definition`:

Definition
----------

.. code-block:: c

    struct mx3_camera_dev {
        struct clk *clk;
        void __iomem *base;
        struct mx3_camera_pdata *pdata;
        unsigned long platform_flags;
        unsigned long mclk;
        u16 width_flags;
        struct list_head capture;
        spinlock_t lock;
        struct mx3_camera_buffer *active;
        size_t buf_total;
        struct vb2_alloc_ctx *alloc_ctx;
        enum v4l2_field field;
        int sequence;
        struct idmac_channel  *idmac_channel[1];
        struct soc_camera_host soc_host;
    }

.. _`mx3_camera_dev.members`:

Members
-------

clk
    pointer to clock

base
    remapped register base address

pdata
    platform data

platform_flags
    platform flags

mclk
    master clock frequency in Hz

width_flags
    *undescribed*

capture
    list of capture videobuffers

lock
    protects video buffer lists

active
    active video buffer

buf_total
    *undescribed*

alloc_ctx
    *undescribed*

field
    *undescribed*

sequence
    *undescribed*

idmac_channel
    array of pointers to IPU DMAC DMA channels

soc_host
    embedded soc_host object

.. This file was automatic generated / don't edit.

