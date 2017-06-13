.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc32.c

.. _`crc32_le_generic`:

crc32_le_generic
================

.. c:function:: u32 __pure crc32_le_generic(u32 crc, unsigned char const *p, size_t len, const u32 tab, u32 polynomial)

    Calculate bitwise little-endian Ethernet AUTODIN II CRC32/CRC32C

    :param u32 crc:
        seed value for computation.  ~0 for Ethernet, sometimes 0 for other
        uses, or the previous crc32/crc32c value if computing incrementally.

    :param unsigned char const \*p:
        pointer to buffer over which CRC32/CRC32C is run

    :param size_t len:
        length of buffer \ ``p``\ 

    :param const u32 tab:
        little-endian Ethernet table

    :param u32 polynomial:
        CRC32/CRC32c LE polynomial

.. _`crc32_generic_shift`:

crc32_generic_shift
===================

.. c:function:: u32 __attribute_const__ crc32_generic_shift(u32 crc, size_t len, u32 polynomial)

    Append len 0 bytes to crc, in logarithmic time

    :param u32 crc:
        The original little-endian CRC (i.e. lsbit is x^31 coefficient)

    :param size_t len:
        The number of bytes. \ ``crc``\  is multiplied by x^(8*@len)

    :param u32 polynomial:
        The modulus used to reduce the result to 32 bits.

.. _`crc32_generic_shift.description`:

Description
-----------

It's possible to parallelize CRC computations by computing a CRC
over separate ranges of a buffer, then summing them.
This shifts the given CRC by 8*len bits (i.e. produces the same effect
as appending len bytes of zero to the data), in time proportional
to log(len).

.. _`crc32_be_generic`:

crc32_be_generic
================

.. c:function:: u32 __pure crc32_be_generic(u32 crc, unsigned char const *p, size_t len, const u32 tab, u32 polynomial)

    Calculate bitwise big-endian Ethernet AUTODIN II CRC32

    :param u32 crc:
        seed value for computation.  ~0 for Ethernet, sometimes 0 for
        other uses, or the previous crc32 value if computing incrementally.

    :param unsigned char const \*p:
        pointer to buffer over which CRC32 is run

    :param size_t len:
        length of buffer \ ``p``\ 

    :param const u32 tab:
        big-endian Ethernet table

    :param u32 polynomial:
        CRC32 BE polynomial

.. This file was automatic generated / don't edit.

