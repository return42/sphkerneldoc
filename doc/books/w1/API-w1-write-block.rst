
.. _API-w1-write-block:

==============
w1_write_block
==============

*man w1_write_block(9)*

*4.6.0-rc1*

Writes a series of bytes.


Synopsis
========

.. c:function:: void w1_write_block( struct w1_master * dev, const u8 * buf, int len )

Arguments
=========

``dev``
    the master device

``buf``
    pointer to the data to write

``len``
    the number of bytes to write
