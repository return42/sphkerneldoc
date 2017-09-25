.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/vdec/vdec_vp9_if.c

.. _`vp9_dram_buf`:

struct vp9_dram_buf
===================

.. c:type:: struct vp9_dram_buf

    contains buffer info for vpu

.. _`vp9_dram_buf.definition`:

Definition
----------

.. code-block:: c

    struct vp9_dram_buf {
        unsigned long va;
        unsigned long pa;
        unsigned int sz;
        unsigned int padding;
    }

.. _`vp9_dram_buf.members`:

Members
-------

va
    cpu address

pa
    iova address

sz
    buffer size

padding
    for 64 bytes alignment

.. _`vp9_fb_info`:

struct vp9_fb_info
==================

.. c:type:: struct vp9_fb_info

    contains frame buffer info

.. _`vp9_fb_info.definition`:

Definition
----------

.. code-block:: c

    struct vp9_fb_info {
        struct vdec_fb *fb;
        unsigned int reserved[32];
    }

.. _`vp9_fb_info.members`:

Members
-------

fb
    frmae buffer

reserved
    reserved field used by vpu

.. _`vp9_ref_cnt_buf`:

struct vp9_ref_cnt_buf
======================

.. c:type:: struct vp9_ref_cnt_buf

    contains reference buffer information

.. _`vp9_ref_cnt_buf.definition`:

Definition
----------

.. code-block:: c

    struct vp9_ref_cnt_buf {
        struct vp9_fb_info buf;
        unsigned int ref_cnt;
    }

.. _`vp9_ref_cnt_buf.members`:

Members
-------

buf
    referenced frame buffer

ref_cnt
    referenced frame buffer's reference count.
    When reference count=0, remove it from reference list

.. _`vp9_ref_buf`:

struct vp9_ref_buf
==================

.. c:type:: struct vp9_ref_buf

    contains current frame's reference buffer information

.. _`vp9_ref_buf.definition`:

Definition
----------

.. code-block:: c

    struct vp9_ref_buf {
        struct vp9_fb_info *buf;
        unsigned int idx;
        unsigned int reserved[6];
    }

.. _`vp9_ref_buf.members`:

Members
-------

buf
    reference buffer

idx
    reference buffer index to frm_bufs

reserved
    reserved field used by vpu

.. _`vp9_sf_ref_fb`:

struct vp9_sf_ref_fb
====================

.. c:type:: struct vp9_sf_ref_fb

    contains frame buffer info

.. _`vp9_sf_ref_fb.definition`:

Definition
----------

.. code-block:: c

    struct vp9_sf_ref_fb {
        struct vdec_fb fb;
        int used;
        int padding;
    }

.. _`vp9_sf_ref_fb.members`:

Members
-------

fb
    super frame reference frame buffer

used
    this reference frame info entry is used

padding
    for 64 bytes size align

.. This file was automatic generated / don't edit.

