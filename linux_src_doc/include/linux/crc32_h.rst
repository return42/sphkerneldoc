.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/crc32.h

.. _`crc32_le_shift`:

crc32_le_shift
==============

.. c:function:: u32 __attribute_const__ crc32_le_shift(u32 crc, size_t len)

    Combine two crc32 check values into one. For two sequences of bytes, seq1 and seq2 with lengths len1 and len2, \ :c:func:`crc32_le`\  check values were calculated for each, crc1 and crc2.

    :param crc:
        *undescribed*
    :type crc: u32

    :param len:
        *undescribed*
    :type len: size_t

.. _`crc32_le_shift.return`:

Return
------

The \ :c:func:`crc32_le`\  check value of seq1 and seq2 concatenated,
requiring only crc1, crc2, and len2. Note: If seq_full denotes
the concatenated memory area of seq1 with seq2, and crc_full
the \ :c:func:`crc32_le`\  value of seq_full, then crc_full ==
crc32_le_combine(crc1, crc2, len2) when crc_full was seeded
with the same initializer as crc1, and crc2 seed was 0. See
also \ :c:func:`crc32_combine_test`\ .

.. _`__crc32c_le_shift`:

\__crc32c_le_shift
==================

.. c:function:: u32 __attribute_const__ __crc32c_le_shift(u32 crc, size_t len)

    Combine two crc32c check values into one. For two sequences of bytes, seq1 and seq2 with lengths len1 and len2, \__crc32c_le() check values were calculated for each, crc1 and crc2.

    :param crc:
        *undescribed*
    :type crc: u32

    :param len:
        *undescribed*
    :type len: size_t

.. _`__crc32c_le_shift.return`:

Return
------

The \__crc32c_le() check value of seq1 and seq2 concatenated,
requiring only crc1, crc2, and len2. Note: If seq_full denotes
the concatenated memory area of seq1 with seq2, and crc_full
the \__crc32c_le() value of seq_full, then crc_full ==
\__crc32c_le_combine(crc1, crc2, len2) when crc_full was
seeded with the same initializer as crc1, and crc2 seed
was 0. See also \ :c:func:`crc32c_combine_test`\ .

.. This file was automatic generated / don't edit.

