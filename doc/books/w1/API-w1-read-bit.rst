
.. _API-w1-read-bit:

===========
w1_read_bit
===========

*man w1_read_bit(9)*

*4.6.0-rc1*

Generates a write-1 cycle and samples the level.


Synopsis
========

.. c:function:: u8 w1_read_bit( struct w1_master * dev )

Arguments
=========

``dev``
    the master device


Description
===========

Only call if dev->bus_master->touch_bit is NULL
