.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/vdec/vdec_h264_if.c

.. _`h264_fb`:

struct h264_fb
==============

.. c:type:: struct h264_fb

    h264 decode frame buffer information

.. _`h264_fb.definition`:

Definition
----------

.. code-block:: c

    struct h264_fb {
        uint64_t vdec_fb_va;
        uint64_t y_fb_dma;
        uint64_t c_fb_dma;
        int32_t poc;
        uint32_t reserved;
    }

.. _`h264_fb.members`:

Members
-------

vdec_fb_va
    virtual address of struct vdec_fb

y_fb_dma
    dma address of Y frame buffer (luma)

c_fb_dma
    dma address of C frame buffer (chroma)

poc
    picture order count of frame buffer

reserved
    for 8 bytes alignment

.. _`h264_ring_fb_list`:

struct h264_ring_fb_list
========================

.. c:type:: struct h264_ring_fb_list

    ring frame buffer list

.. _`h264_ring_fb_list.definition`:

Definition
----------

.. code-block:: c

    struct h264_ring_fb_list {
        struct h264_fb fb_list;
        unsigned int read_idx;
        unsigned int write_idx;
        unsigned int count;
        unsigned int reserved;
    }

.. _`h264_ring_fb_list.members`:

Members
-------

fb_list
    frame buffer arrary

read_idx
    read index

write_idx
    write index

count
    buffer count in list

reserved
    *undescribed*

.. _`vdec_h264_dec_info`:

struct vdec_h264_dec_info
=========================

.. c:type:: struct vdec_h264_dec_info

    decode information

.. _`vdec_h264_dec_info.definition`:

Definition
----------

.. code-block:: c

    struct vdec_h264_dec_info {
        uint32_t dpb_sz;
        uint32_t resolution_changed;
        uint32_t realloc_mv_buf;
        uint32_t reserved;
        uint64_t bs_dma;
        uint64_t y_fb_dma;
        uint64_t c_fb_dma;
        uint64_t vdec_fb_va;
    }

.. _`vdec_h264_dec_info.members`:

Members
-------

dpb_sz
    decoding picture buffer size

resolution_changed
    resoltion change happen

realloc_mv_buf
    flag to notify driver to re-allocate mv buffer

reserved
    for 8 bytes alignment

bs_dma
    Input bit-stream buffer dma address

y_fb_dma
    Y frame buffer dma address

c_fb_dma
    C frame buffer dma address

vdec_fb_va
    VDEC frame buffer struct virtual address

.. _`vdec_h264_vsi`:

struct vdec_h264_vsi
====================

.. c:type:: struct vdec_h264_vsi

    shared memory for decode information exchange between VPU and Host. The memory is allocated by VPU then mapping to Host in \ :c:func:`vpu_dec_init`\  and freed in \ :c:func:`vpu_dec_deinit`\  by VPU. AP-W/R : AP is writer/reader on this item VPU-W/R: VPU is write/reader on this item

.. _`vdec_h264_vsi.definition`:

Definition
----------

.. code-block:: c

    struct vdec_h264_vsi {
        unsigned char hdr_buf;
        uint64_t pred_buf_dma;
        uint64_t mv_buf_dma;
        struct h264_ring_fb_list list_free;
        struct h264_ring_fb_list list_disp;
        struct vdec_h264_dec_info dec;
        struct vdec_pic_info pic;
        struct v4l2_rect crop;
    }

.. _`vdec_h264_vsi.members`:

Members
-------

hdr_buf
    Header parsing buffer (AP-W, VPU-R)

pred_buf_dma
    HW working predication buffer dma address (AP-W, VPU-R)

mv_buf_dma
    HW working motion vector buffer dma address (AP-W, VPU-R)

list_free
    free frame buffer ring list (AP-W/R, VPU-W)

list_disp
    display frame buffer ring list (AP-R, VPU-W)

dec
    decode information (AP-R, VPU-W)

pic
    picture information (AP-R, VPU-W)

crop
    crop information (AP-R, VPU-W)

.. _`vdec_h264_inst`:

struct vdec_h264_inst
=====================

.. c:type:: struct vdec_h264_inst

    h264 decoder instance

.. _`vdec_h264_inst.definition`:

Definition
----------

.. code-block:: c

    struct vdec_h264_inst {
        unsigned int num_nalu;
        struct mtk_vcodec_ctx *ctx;
        struct mtk_vcodec_mem pred_buf;
        struct mtk_vcodec_mem mv_buf;
        struct vdec_vpu_inst vpu;
        struct vdec_h264_vsi *vsi;
    }

.. _`vdec_h264_inst.members`:

Members
-------

num_nalu
    how many nalus be decoded

ctx
    point to mtk_vcodec_ctx

pred_buf
    HW working predication buffer

mv_buf
    HW working motion vector buffer

vpu
    VPU instance

vsi
    VPU shared information

.. This file was automatic generated / don't edit.

