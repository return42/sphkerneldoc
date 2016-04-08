
.. _API-w1-write-bit:

============
w1_write_bit
============

*man w1_write_bit(9)*

*4.6.0-rc1*

Generates a write-0 or write-1 cycle.


Synopsis
========

.. c:function:: void w1_write_bit( struct w1_master * dev, int bit )

Arguments
=========

``dev``
    the master device

``bit``
    bit to write


Description
===========

Only call if dev->bus_master->touch_bit is NULL
