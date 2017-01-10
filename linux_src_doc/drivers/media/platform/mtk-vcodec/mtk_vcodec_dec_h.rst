.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/mtk_vcodec_dec.h

.. _`vdec_fb`:

struct vdec_fb
==============

.. c:type:: struct vdec_fb

    decoder frame buffer

.. _`vdec_fb.definition`:

Definition
----------

.. code-block:: c

    struct vdec_fb {
        struct mtk_vcodec_mem base_y;
        struct mtk_vcodec_mem base_c;
        unsigned int status;
    }

.. _`vdec_fb.members`:

Members
-------

base_y
    Y plane memory info

base_c
    C plane memory info

status
    frame buffer status (vdec_fb_status)

.. _`mtk_video_dec_buf`:

struct mtk_video_dec_buf
========================

.. c:type:: struct mtk_video_dec_buf

    Private data related to each VB2 buffer.

.. _`mtk_video_dec_buf.definition`:

Definition
----------

.. code-block:: c

    struct mtk_video_dec_buf {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        bool used;
        bool ready_to_display;
        bool queued_in_vb2;
        bool queued_in_v4l2;
        bool lastframe;
        struct vdec_fb frame_buffer;
    }

.. _`mtk_video_dec_buf.members`:

Members
-------

vb
    *undescribed*

list
    link list

used
    Capture buffer contain decoded frame data and keep in
    codec data structure

ready_to_display
    Capture buffer not display yet

queued_in_vb2
    Capture buffer is queue in vb2

queued_in_v4l2
    Capture buffer is in v4l2 driver, but not in vb2
    queue yet

lastframe
    Intput buffer is last buffer - EOS

frame_buffer
    Decode status, and buffer information of Capture buffer

.. _`mtk_video_dec_buf.description`:

Description
-----------

Note : These status information help us track and debug buffer state

.. This file was automatic generated / don't edit.

