
.. _API-crc-ccitt:

=========
crc_ccitt
=========

*man crc_ccitt(9)*

*4.6.0-rc1*

recompute the CRC for the data buffer


Synopsis
========

.. c:function:: u16 crc_ccitt( u16 crc, u8 const * buffer, size_t len )

Arguments
=========

``crc``
    previous CRC value

``buffer``
    data pointer

``len``
    number of bytes in the buffer
