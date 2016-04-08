
.. _API-swap-buf-le16:

=============
swap_buf_le16
=============

*man swap_buf_le16(9)*

*4.6.0-rc1*

swap halves of 16-bit words in place


Synopsis
========

.. c:function:: void swap_buf_le16( u16 * buf, unsigned int buf_words )

Arguments
=========

``buf``
    Buffer to swap

``buf_words``
    Number of 16-bit words in buffer.


Description
===========

Swap halves of 16-bit words if needed to convert from little-endian byte order to native cpu byte order, or vice-versa.


LOCKING
=======

Inherited from caller.
