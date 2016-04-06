
.. _API-crc7-be:

=======
crc7_be
=======

*man crc7_be(9)*

*4.6.0-rc1*

update the CRC7 for the data buffer


Synopsis
========

.. c:function:: u8 crc7_be( u8 crc, const u8 * buffer, size_t len )

Arguments
=========

``crc``
    previous CRC7 value

``buffer``
    data pointer

``len``
    number of bytes in the buffer


Context
=======

any


Description
===========

Returns the updated CRC7 value. The CRC7 is left-aligned in the byte (the lsbit is always 0), as that makes the computation easier, and all callers want it in that form.
