.. -*- coding: utf-8; mode: rst -*-

.. _API-crc-ccitt:

=========
crc_ccitt
=========

*man crc_ccitt(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
