
.. _API-read-zsdata:

===========
read_zsdata
===========

*man read_zsdata(9)*

*4.6.0-rc1*

Read the data port of a Z8530 channel


Synopsis
========

.. c:function:: u8 read_zsdata( struct z8530_channel * c )

Arguments
=========

``c``
    The Z8530 channel to read the data port from


Description
===========

The data port provides fast access to some things. We still have all the 5uS delays to worry about.
