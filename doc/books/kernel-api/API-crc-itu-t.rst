
.. _API-crc-itu-t:

=========
crc_itu_t
=========

*man crc_itu_t(9)*

*4.6.0-rc1*

Compute the CRC-ITU-T for the data buffer


Synopsis
========

.. c:function:: u16 crc_itu_t( u16 crc, const u8 * buffer, size_t len )

Arguments
=========

``crc``
    previous CRC value

``buffer``
    data pointer

``len``
    number of bytes in the buffer


Description
===========

Returns the updated CRC value
