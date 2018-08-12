.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/gpmi-nand/gpmi-lib.c

.. _`gpmi_copy_bits`:

gpmi_copy_bits
==============

.. c:function:: void gpmi_copy_bits(u8 *dst, size_t dst_bit_off, const u8 *src, size_t src_bit_off, size_t nbits)

    copy bits from one memory region to another

    :param u8 \*dst:
        destination buffer

    :param size_t dst_bit_off:
        bit offset we're starting to write at

    :param const u8 \*src:
        source buffer

    :param size_t src_bit_off:
        bit offset we're starting to read from

    :param size_t nbits:
        number of bits to copy

.. _`gpmi_copy_bits.description`:

Description
-----------

This functions copies bits from one memory region to another, and is used by
the GPMI driver to copy ECC sections which are not guaranteed to be byte
aligned.

src and dst should not overlap.

.. This file was automatic generated / don't edit.

