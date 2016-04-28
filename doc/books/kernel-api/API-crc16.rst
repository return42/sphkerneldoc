.. -*- coding: utf-8; mode: rst -*-

.. _API-crc16:

=====
crc16
=====

*man crc16(9)*

*4.6.0-rc5*

compute the CRC-16 for the data buffer


Synopsis
========

.. c:function:: u16 crc16( u16 crc, u8 const * buffer, size_t len )

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

Returns the updated CRC value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
