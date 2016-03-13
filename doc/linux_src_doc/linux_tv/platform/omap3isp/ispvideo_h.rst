.. -*- coding: utf-8; mode: rst -*-

==========
ispvideo.h
==========



.. _xref_struct_isp_buffer:

struct isp_buffer
=================

.. c:type:: struct isp_buffer

    ISP video buffer



Definition
----------

.. code-block:: c

  struct isp_buffer {
    struct vb2_v4l2_buffer vb;
    struct list_head irqlist;
    dma_addr_t dma;
  };



Members
-------

:``struct vb2_v4l2_buffer vb``:
    videobuf2 buffer

:``struct list_head irqlist``:
    List head for insertion into IRQ queue

:``dma_addr_t dma``:
    DMA address



