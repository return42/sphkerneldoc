.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/coda/coda-h264.c

.. _`coda_h264_sps_fixup`:

coda_h264_sps_fixup
===================

.. c:function:: int coda_h264_sps_fixup(struct coda_ctx *ctx, int width, int height, char *buf, int *size, int max_size)

    fixes frame cropping values in h.264 SPS

    :param ctx:
        encoder context
    :type ctx: struct coda_ctx \*

    :param width:
        visible width
    :type width: int

    :param height:
        visible height
    :type height: int

    :param buf:
        buffer containing h.264 SPS RBSP, starting with NAL header
    :type buf: char \*

    :param size:
        modified RBSP size return value
    :type size: int \*

    :param max_size:
        available size in buf
    :type max_size: int

.. _`coda_h264_sps_fixup.description`:

Description
-----------

Rewrites the frame cropping values in an h.264 SPS RBSP correctly for the
given visible width and height.

.. This file was automatic generated / don't edit.

