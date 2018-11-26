.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-isp.c

.. _`fimc_isp_find_format`:

fimc_isp_find_format
====================

.. c:function:: const struct fimc_fmt *fimc_isp_find_format(const u32 *pixelformat, const u32 *mbus_code, int index)

    lookup color format by fourcc or media bus code

    :param pixelformat:
        fourcc to match, ignored if null
    :type pixelformat: const u32 \*

    :param mbus_code:
        media bus code to match, ignored if null
    :type mbus_code: const u32 \*

    :param index:
        index to the fimc_isp_formats array, ignored if negative
    :type index: int

.. This file was automatic generated / don't edit.

