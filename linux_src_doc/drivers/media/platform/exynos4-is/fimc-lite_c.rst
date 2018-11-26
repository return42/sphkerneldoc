.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-lite.c

.. _`fimc_lite_find_format`:

fimc_lite_find_format
=====================

.. c:function:: const struct fimc_fmt *fimc_lite_find_format(const u32 *pixelformat, const u32 *mbus_code, unsigned int mask, int index)

    lookup fimc color format by fourcc or media bus code

    :param pixelformat:
        fourcc to match, ignored if null
    :type pixelformat: const u32 \*

    :param mbus_code:
        media bus code to match, ignored if null
    :type mbus_code: const u32 \*

    :param mask:
        the color format flags to match
    :type mask: unsigned int

    :param index:
        index to the fimc_lite_formats array, ignored if negative
    :type index: int

.. This file was automatic generated / don't edit.

