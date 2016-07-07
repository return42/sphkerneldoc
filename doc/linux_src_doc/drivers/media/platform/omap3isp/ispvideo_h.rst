.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/omap3isp/ispvideo.h

.. _`isp_buffer`:

struct isp_buffer
=================

.. c:type:: struct isp_buffer

    ISP video buffer

.. _`isp_buffer.definition`:

Definition
----------

.. code-block:: c

    struct isp_buffer {
        struct vb2_v4l2_buffer vb;
        struct list_head irqlist;
        dma_addr_t dma;
    }

.. _`isp_buffer.members`:

Members
-------

vb
    videobuf2 buffer

irqlist
    List head for insertion into IRQ queue

dma
    DMA address

.. This file was automatic generated / don't edit.

