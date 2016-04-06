
.. _API-relay-buf-full:

==============
relay_buf_full
==============

*man relay_buf_full(9)*

*4.6.0-rc1*

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
