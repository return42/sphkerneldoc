.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/vdec/vdec_vp8_if.c

.. _`vdec_vp8_dec_info`:

struct vdec_vp8_dec_info
========================

.. c:type:: struct vdec_vp8_dec_info

    decode misc information

.. _`vdec_vp8_dec_info.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vp8_dec_info {
        uint64_t working_buf_dma;
        uint64_t prev_y_dma;
        uint64_t cur_y_fb_dma;
        uint64_t cur_c_fb_dma;
        uint64_t bs_dma;
        uint32_t bs_sz;
        uint32_t resolution_changed;
        uint32_t show_frame;
        uint32_t wait_key_frame;
    }

.. _`vdec_vp8_dec_info.members`:

Members
-------

working_buf_dma
    working buffer dma address

prev_y_dma
    previous decoded frame buffer Y plane address

cur_y_fb_dma
    current plane Y frame buffer dma address

cur_c_fb_dma
    current plane C frame buffer dma address

bs_dma
    bitstream dma address

bs_sz
    bitstream size

resolution_changed
    resolution change flag 1 - changed,  0 - not change

show_frame
    display this frame or not

wait_key_frame
    wait key frame coming

.. _`vdec_vp8_vsi`:

struct vdec_vp8_vsi
===================

.. c:type:: struct vdec_vp8_vsi

    VPU shared information

.. _`vdec_vp8_vsi.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vp8_vsi {
        struct vdec_vp8_dec_info dec;
        struct vdec_pic_info pic;
        uint32_t dec_table;
        uint32_t segment_buf;
        uint32_t load_data;
    }

.. _`vdec_vp8_vsi.members`:

Members
-------

dec
    decoding information

pic
    picture information

dec_table
    decoder coefficient table

segment_buf
    segmentation buffer

load_data
    flag to indicate reload decode data

.. _`vdec_vp8_hw_reg_base`:

struct vdec_vp8_hw_reg_base
===========================

.. c:type:: struct vdec_vp8_hw_reg_base

    HW register base

.. _`vdec_vp8_hw_reg_base.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vp8_hw_reg_base {
        void __iomem *sys;
        void __iomem *misc;
        void __iomem *ld;
        void __iomem *top;
        void __iomem *cm;
        void __iomem *hwd;
        void __iomem *hwb;
    }

.. _`vdec_vp8_hw_reg_base.members`:

Members
-------

sys
    base address for sys

misc
    base address for misc

ld
    base address for ld

top
    base address for top

cm
    base address for cm

hwd
    base address for hwd

hwb
    base address for hwb

.. _`vdec_vp8_vpu_inst`:

struct vdec_vp8_vpu_inst
========================

.. c:type:: struct vdec_vp8_vpu_inst

    VPU instance for VP8 decode

.. _`vdec_vp8_vpu_inst.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vp8_vpu_inst {
        wait_queue_head_t wq_hd;
        int signaled;
        int failure;
        uint32_t inst_addr;
    }

.. _`vdec_vp8_vpu_inst.members`:

Members
-------

wq_hd
    Wait queue to wait VPU message ack

signaled
    1 - Host has received ack message from VPU, 0 - not recevie

failure
    VPU execution result status 0 - success, others - fail

inst_addr
    VPU decoder instance address

.. _`vdec_vp8_inst`:

struct vdec_vp8_inst
====================

.. c:type:: struct vdec_vp8_inst

    VP8 decoder instance

.. _`vdec_vp8_inst.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vp8_inst {
        struct vdec_fb *cur_fb;
        struct vdec_fb_node dec_fb;
        struct list_head available_fb_node_list;
        struct list_head fb_use_list;
        struct list_head fb_free_list;
        struct list_head fb_disp_list;
        struct mtk_vcodec_mem working_buf;
        struct vdec_vp8_hw_reg_base reg_base;
        unsigned int frm_cnt;
        struct mtk_vcodec_ctx *ctx;
        struct vdec_vpu_inst vpu;
        struct vdec_vp8_vsi *vsi;
    }

.. _`vdec_vp8_inst.members`:

Members
-------

cur_fb
    current frame buffer

dec_fb
    decode frame buffer node

available_fb_node_list
    list to store available frame buffer node

fb_use_list
    list to store frame buffer in use

fb_free_list
    list to store free frame buffer

fb_disp_list
    list to store display ready frame buffer

working_buf
    HW decoder working buffer

reg_base
    HW register base address

frm_cnt
    decode frame count

ctx
    V4L2 context

vpu
    VPU instance for decoder

vsi
    VPU share information

.. This file was automatic generated / don't edit.

