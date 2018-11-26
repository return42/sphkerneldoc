.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/string_64.h

.. _`memcpy_mcsafe`:

memcpy_mcsafe
=============

.. c:function:: unsigned long memcpy_mcsafe(void *dst, const void *src, size_t cnt)

    copy memory with indication if a machine check happened

    :param dst:
        destination address
    :type dst: void \*

    :param src:
        source address
    :type src: const void \*

    :param cnt:
        number of bytes to copy
    :type cnt: size_t

.. _`memcpy_mcsafe.description`:

Description
-----------

Low level memory copy function that catches machine checks
We only call into the "safe" function on systems that can
actually do machine check recovery. Everyone else can just
use \ :c:func:`memcpy`\ .

Return 0 for success, or number of bytes not copied if there was an
exception.

.. This file was automatic generated / don't edit.

