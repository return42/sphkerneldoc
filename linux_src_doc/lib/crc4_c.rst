.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc4.c

.. _`crc4`:

crc4
====

.. c:function:: uint8_t crc4(uint8_t c, uint64_t x, int bits)

    calculate the 4-bit crc of a value.

    :param uint8_t c:
        *undescribed*

    :param uint64_t x:
        value to checksum

    :param int bits:
        number of bits in \ ``x``\  to checksum

.. _`crc4.description`:

Description
-----------

Returns the crc4 value of \ ``x``\ , using polynomial 0b10111.

The \ ``x``\  value is treated as left-aligned, and bits above \ ``bits``\  are ignored
in the crc calculations.

.. This file was automatic generated / don't edit.

