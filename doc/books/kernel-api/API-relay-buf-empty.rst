
.. _API-relay-buf-empty:

===============
relay_buf_empty
===============

*man relay_buf_empty(9)*

*4.6.0-rc1*

boolean, is the channel buffer empty?


Synopsis
========

.. c:function:: int relay_buf_empty( struct rchan_buf * buf )

Arguments
=========

``buf``
    channel buffer


Description
===========

Returns 1 if the buffer is empty, 0 otherwise.
