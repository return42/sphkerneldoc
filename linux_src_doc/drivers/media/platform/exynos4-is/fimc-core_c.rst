.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-core.c

.. _`fimc_adjust_mplane_format`:

fimc_adjust_mplane_format
=========================

.. c:function:: void fimc_adjust_mplane_format(struct fimc_fmt *fmt, u32 width, u32 height, struct v4l2_pix_format_mplane *pix)

    adjust bytesperline/sizeimage for each plane

    :param fmt:
        fimc pixel format description (input)
    :type fmt: struct fimc_fmt \*

    :param width:
        requested pixel width
    :type width: u32

    :param height:
        requested pixel height
    :type height: u32

    :param pix:
        multi-plane format to adjust
    :type pix: struct v4l2_pix_format_mplane \*

.. _`fimc_find_format`:

fimc_find_format
================

.. c:function:: struct fimc_fmt *fimc_find_format(const u32 *pixelformat, const u32 *mbus_code, unsigned int mask, int index)

    lookup fimc color format by fourcc or media bus format

    :param pixelformat:
        fourcc to match, ignored if null
    :type pixelformat: const u32 \*

    :param mbus_code:
        media bus code to match, ignored if null
    :type mbus_code: const u32 \*

    :param mask:
        the color flags to match
    :type mask: unsigned int

    :param index:
        offset in the fimc_formats array, ignored if negative
    :type index: int

.. This file was automatic generated / don't edit.

