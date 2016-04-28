.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-buf-empty:

===============
relay_buf_empty
===============

*man relay_buf_empty(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
