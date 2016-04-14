.. -*- coding: utf-8; mode: rst -*-

===========
crc-ccitt.c
===========

.. _`crc_ccitt`:

crc_ccitt
=========

.. c:function:: u16 crc_ccitt (u16 crc, u8 const *buffer, size_t len)

    recompute the CRC for the data buffer

    :param u16 crc:
        previous CRC value

    :param u8 const \*buffer:
        data pointer

    :param size_t len:
        number of bytes in the buffer

