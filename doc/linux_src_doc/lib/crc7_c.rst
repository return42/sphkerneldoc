.. -*- coding: utf-8; mode: rst -*-

======
crc7.c
======

.. _`crc7_be`:

crc7_be
=======

.. c:function:: u8 crc7_be (u8 crc, const u8 *buffer, size_t len)

    update the CRC7 for the data buffer

    :param u8 crc:
        previous CRC7 value

    :param const u8 \*buffer:
        data pointer

    :param size_t len:
        number of bytes in the buffer
        Context: any


.. _`crc7_be.description`:

Description
-----------

Returns the updated CRC7 value.
The CRC7 is left-aligned in the byte (the lsbit is always 0), as that
makes the computation easier, and all callers want it in that form.

