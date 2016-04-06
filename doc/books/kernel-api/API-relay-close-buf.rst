
.. _API-relay-close-buf:

===============
relay_close_buf
===============

*man relay_close_buf(9)*

*4.6.0-rc1*

close a channel buffer


Synopsis
========

.. c:function:: void relay_close_buf( struct rchan_buf * buf )

Arguments
=========

``buf``
    channel buffer


Description
===========

Marks the buffer finalized and restores the default callbacks. The channel buffer and channel buffer data structure are then freed automatically when the last reference is given
up.
