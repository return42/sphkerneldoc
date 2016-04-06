
.. _API-generic-pipe-buf-release:

========================
generic_pipe_buf_release
========================

*man generic_pipe_buf_release(9)*

*4.6.0-rc1*

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
