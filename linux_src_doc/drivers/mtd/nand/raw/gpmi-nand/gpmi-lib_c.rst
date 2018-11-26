.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/gpmi-nand/gpmi-lib.c

.. _`gpmi_copy_bits`:

gpmi_copy_bits
==============

.. c:function:: void gpmi_copy_bits(u8 *dst, size_t dst_bit_off, const u8 *src, size_t src_bit_off, size_t nbits)

    copy bits from one memory region to another

    :param dst:
        destination buffer
    :type dst: u8 \*

    :param dst_bit_off:
        bit offset we're starting to write at
    :type dst_bit_off: size_t

    :param src:
        source buffer
    :type src: const u8 \*

    :param src_bit_off:
        bit offset we're starting to read from
    :type src_bit_off: size_t

    :param nbits:
        number of bits to copy
    :type nbits: size_t

.. _`gpmi_copy_bits.description`:

Description
-----------

This functions copies bits from one memory region to another, and is used by
the GPMI driver to copy ECC sections which are not guaranteed to be byte
aligned.

src and dst should not overlap.

.. This file was automatic generated / don't edit.

