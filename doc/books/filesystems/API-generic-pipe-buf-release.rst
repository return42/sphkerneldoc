.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-pipe-buf-release:

========================
generic_pipe_buf_release
========================

*man generic_pipe_buf_release(9)*

*4.6.0-rc5*

put a reference to a ``struct pipe_buffer``


Synopsis
========

.. c:function:: void generic_pipe_buf_release( struct pipe_inode_info * pipe, struct pipe_buffer * buf )

Arguments
=========

``pipe``
    the pipe that the buffer belongs to

``buf``
    the buffer to put a reference to


Description
===========

This function releases a reference to ``buf``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
