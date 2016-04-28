.. -*- coding: utf-8; mode: rst -*-

.. _API-read-zsdata:

===========
read_zsdata
===========

*man read_zsdata(9)*

*4.6.0-rc5*

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

The data port provides fast access to some things. We still have all the
5uS delays to worry about.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
