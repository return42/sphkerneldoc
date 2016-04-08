
.. _API-w1-touch-block:

==============
w1_touch_block
==============

*man w1_touch_block(9)*

*4.6.0-rc1*

Touches a series of bytes.


Synopsis
========

.. c:function:: void w1_touch_block( struct w1_master * dev, u8 * buf, int len )

Arguments
=========

``dev``
    the master device

``buf``
    pointer to the data to write

``len``
    the number of bytes to write
