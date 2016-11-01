.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/mtk_vcodec_enc.h

.. _`mtk_video_enc_buf`:

struct mtk_video_enc_buf
========================

.. c:type:: struct mtk_video_enc_buf

    Private data related to each VB2 buffer.

.. _`mtk_video_enc_buf.definition`:

Definition
----------

.. code-block:: c

    struct mtk_video_enc_buf {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        u32 param_change;
        struct mtk_enc_params enc_params;
    }

.. _`mtk_video_enc_buf.members`:

Members
-------

vb
    Pointer to related VB2 buffer.

list
    list that buffer link to

param_change
    Types of encode parameter change before encoding this
    buffer

enc_params
    Encode parameters changed before encode this buffer

.. This file was automatic generated / don't edit.

