.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc64.c

.. _`crc64_be`:

crc64_be
========

.. c:function:: u64 __pure crc64_be(u64 crc, const void *p, size_t len)

    Calculate bitwise big-endian ECMA-182 CRC64

    :param crc:
        seed value for computation. 0 or (u64)~0 for a new CRC calculation,
    :type crc: u64

    :param p:
        pointer to buffer over which CRC64 is run
    :type p: const void \*

    :param len:
        length of buffer \ ``p``\ 
    :type len: size_t

.. This file was automatic generated / don't edit.

