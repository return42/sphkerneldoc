
.. _API-w1-read-block:

=============
w1_read_block
=============

*man w1_read_block(9)*

*4.6.0-rc1*

Reads a series of bytes.


Synopsis
========

.. c:function:: u8 w1_read_block( struct w1_master * dev, u8 * buf, int len )

Arguments
=========

``dev``
    the master device

``buf``
    pointer to the buffer to fill

``len``
    the number of bytes to read


Return
======

the number of bytes read
