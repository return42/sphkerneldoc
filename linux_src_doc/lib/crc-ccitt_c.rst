.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc-ccitt.c

.. _`crc_ccitt`:

crc_ccitt
=========

.. c:function:: u16 crc_ccitt(u16 crc, u8 const *buffer, size_t len)

    recompute the CRC (CRC-CCITT variant) for the data buffer

    :param u16 crc:
        previous CRC value

    :param u8 const \*buffer:
        data pointer

    :param size_t len:
        number of bytes in the buffer

.. _`crc_ccitt_false`:

crc_ccitt_false
===============

.. c:function:: u16 crc_ccitt_false(u16 crc, u8 const *buffer, size_t len)

    recompute the CRC (CRC-CCITT-FALSE variant) for the data buffer

    :param u16 crc:
        previous CRC value

    :param u8 const \*buffer:
        data pointer

    :param size_t len:
        number of bytes in the buffer

.. This file was automatic generated / don't edit.

