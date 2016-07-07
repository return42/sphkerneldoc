.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-lite.c

.. _`fimc_lite_find_format`:

fimc_lite_find_format
=====================

.. c:function:: const struct fimc_fmt *fimc_lite_find_format(const u32 *pixelformat, const u32 *mbus_code, unsigned int mask, int index)

    lookup fimc color format by fourcc or media bus code

    :param const u32 \*pixelformat:
        fourcc to match, ignored if null

    :param const u32 \*mbus_code:
        media bus code to match, ignored if null

    :param unsigned int mask:
        the color format flags to match

    :param int index:
        index to the fimc_lite_formats array, ignored if negative

.. This file was automatic generated / don't edit.

