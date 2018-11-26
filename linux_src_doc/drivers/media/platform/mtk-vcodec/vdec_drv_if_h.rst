.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/vdec_drv_if.h

.. _`vdec_fb_node`:

struct vdec_fb_node
===================

.. c:type:: struct vdec_fb_node

    decoder frame buffer node

.. _`vdec_fb_node.definition`:

Definition
----------

.. code-block:: c

    struct vdec_fb_node {
        struct list_head list;
        struct vdec_fb *fb;
    }

.. _`vdec_fb_node.members`:

Members
-------

list
    list to hold this node

fb
    point to frame buffer (vdec_fb), fb could point to frame buffer and
    working buffer this is for maintain buffers in different state

.. _`vdec_if_init`:

vdec_if_init
============

.. c:function:: int vdec_if_init(struct mtk_vcodec_ctx *ctx, unsigned int fourcc)

    initialize decode driver

    :param ctx:
        [in] v4l2 context
    :type ctx: struct mtk_vcodec_ctx \*

    :param fourcc:
        [in] video format fourcc, V4L2_PIX_FMT_H264/VP8/VP9..
    :type fourcc: unsigned int

.. _`vdec_if_deinit`:

vdec_if_deinit
==============

.. c:function:: void vdec_if_deinit(struct mtk_vcodec_ctx *ctx)

    deinitialize decode driver

    :param ctx:
        [in] v4l2 context
    :type ctx: struct mtk_vcodec_ctx \*

.. _`vdec_if_decode`:

vdec_if_decode
==============

.. c:function:: int vdec_if_decode(struct mtk_vcodec_ctx *ctx, struct mtk_vcodec_mem *bs, struct vdec_fb *fb, bool *res_chg)

    trigger decode

    :param ctx:
        [in] v4l2 context
    :type ctx: struct mtk_vcodec_ctx \*

    :param bs:
        [in] input bitstream
    :type bs: struct mtk_vcodec_mem \*

    :param fb:
        [in] frame buffer to store decoded frame, when null menas parse
        header only
    :type fb: struct vdec_fb \*

    :param res_chg:
        [out] resolution change happens if current bs have different
        picture width/height
    :type res_chg: bool \*

.. _`vdec_if_decode.note`:

Note
----

To flush the decoder when reaching EOF, set input bitstream as NULL.

.. _`vdec_if_decode.return`:

Return
------

0 on success. -EIO on unrecoverable error.

.. _`vdec_if_get_param`:

vdec_if_get_param
=================

.. c:function:: int vdec_if_get_param(struct mtk_vcodec_ctx *ctx, enum vdec_get_param_type type, void *out)

    get driver's parameter

    :param ctx:
        [in] v4l2 context
    :type ctx: struct mtk_vcodec_ctx \*

    :param type:
        [in] input parameter type
    :type type: enum vdec_get_param_type

    :param out:
        [out] buffer to store query result
    :type out: void \*

.. This file was automatic generated / don't edit.

