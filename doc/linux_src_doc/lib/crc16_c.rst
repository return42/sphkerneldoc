.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc16.c

.. _`crc16`:

crc16
=====

.. c:function:: u16 crc16(u16 crc, u8 const *buffer, size_t len)

    compute the CRC-16 for the data buffer

    :param u16 crc:
        previous CRC value

    :param u8 const \*buffer:
        data pointer

    :param size_t len:
        number of bytes in the buffer

.. _`crc16.description`:

Description
-----------

Returns the updated CRC value.

.. This file was automatic generated / don't edit.

