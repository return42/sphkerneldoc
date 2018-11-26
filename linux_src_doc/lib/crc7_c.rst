.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc7.c

.. _`crc7_be`:

crc7_be
=======

.. c:function:: u8 crc7_be(u8 crc, const u8 *buffer, size_t len)

    update the CRC7 for the data buffer

    :param crc:
        previous CRC7 value
    :type crc: u8

    :param buffer:
        data pointer
    :type buffer: const u8 \*

    :param len:
        number of bytes in the buffer
    :type len: size_t

.. _`crc7_be.context`:

Context
-------

any

.. _`crc7_be.description`:

Description
-----------

Returns the updated CRC7 value.
The CRC7 is left-aligned in the byte (the lsbit is always 0), as that
makes the computation easier, and all callers want it in that form.

.. This file was automatic generated / don't edit.

