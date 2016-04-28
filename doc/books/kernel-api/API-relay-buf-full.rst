.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-buf-full:

==============
relay_buf_full
==============

*man relay_buf_full(9)*

*4.6.0-rc5*

boolean, is the channel buffer full?


Synopsis
========

.. c:function:: int relay_buf_full( struct rchan_buf * buf )

Arguments
=========

``buf``
    channel buffer


Description
===========

Returns 1 if the buffer is full, 0 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
