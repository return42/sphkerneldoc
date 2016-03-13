.. -*- coding: utf-8; mode: rst -*-

==========
fimc-isp.c
==========



.. _xref_fimc_isp_find_format:

fimc_isp_find_format
====================

.. c:function:: const struct fimc_fmt * fimc_isp_find_format (const u32 * pixelformat, const u32 * mbus_code, int index)

    lookup color format by fourcc or media bus code

    :param const u32 * pixelformat:
        fourcc to match, ignored if null

    :param const u32 * mbus_code:
        media bus code to match, ignored if null

    :param int index:
        index to the fimc_isp_formats array, ignored if negative


