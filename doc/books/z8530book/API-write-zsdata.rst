
.. _API-write-zsdata:

============
write_zsdata
============

*man write_zsdata(9)*

*4.6.0-rc1*

Write to a Z8530 control register


Synopsis
========

.. c:function:: void write_zsdata( struct z8530_channel * c, u8 val )

Arguments
=========

``c``
    The Z8530 channel

``val``
    Value to write


Description
===========

Write directly to the data register on the Z8530
