.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-close-buf:

===============
relay_close_buf
===============

*man relay_close_buf(9)*

*4.6.0-rc5*

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

Marks the buffer finalized and restores the default callbacks. The
channel buffer and channel buffer data structure are then freed
automatically when the last reference is given up.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
