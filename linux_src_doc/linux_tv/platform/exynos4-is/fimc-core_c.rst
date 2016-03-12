.. -*- coding: utf-8; mode: rst -*-

===========
fimc-core.c
===========



.. _xref_fimc_adjust_mplane_format:

fimc_adjust_mplane_format
=========================

.. c:function:: void fimc_adjust_mplane_format (struct fimc_fmt * fmt, u32 width, u32 height, struct v4l2_pix_format_mplane * pix)

    adjust bytesperline/sizeimage for each plane

    :param struct fimc_fmt * fmt:
        fimc pixel format description (input)

    :param u32 width:
        requested pixel width

    :param u32 height:
        requested pixel height

    :param struct v4l2_pix_format_mplane * pix:
        multi-plane format to adjust




.. _xref_fimc_find_format:

fimc_find_format
================

.. c:function:: struct fimc_fmt * fimc_find_format (const u32 * pixelformat, const u32 * mbus_code, unsigned int mask, int index)

    lookup fimc color format by fourcc or media bus format

    :param const u32 * pixelformat:
        fourcc to match, ignored if null

    :param const u32 * mbus_code:
        media bus code to match, ignored if null

    :param unsigned int mask:
        the color flags to match

    :param int index:
        offset in the fimc_formats array, ignored if negative


