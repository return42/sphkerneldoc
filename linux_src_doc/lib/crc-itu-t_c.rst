.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc-itu-t.c

.. _`crc_itu_t`:

crc_itu_t
=========

.. c:function:: u16 crc_itu_t(u16 crc, const u8 *buffer, size_t len)

    Compute the CRC-ITU-T for the data buffer

    :param u16 crc:
        previous CRC value

    :param const u8 \*buffer:
        data pointer

    :param size_t len:
        number of bytes in the buffer

.. _`crc_itu_t.description`:

Description
-----------

Returns the updated CRC value

.. This file was automatic generated / don't edit.

