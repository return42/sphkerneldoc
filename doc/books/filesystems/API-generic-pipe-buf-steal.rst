
.. _API-generic-pipe-buf-steal:

======================
generic_pipe_buf_steal
======================

*man generic_pipe_buf_steal(9)*

*4.6.0-rc1*

attempt to take ownership of a ``pipe_buffer``


Synopsis
========

.. c:function:: int generic_pipe_buf_steal( struct pipe_inode_info * pipe, struct pipe_buffer * buf )

Arguments
=========

``pipe``
    the pipe that the buffer belongs to

``buf``
    the buffer to attempt to steal


Description
===========

This function attempts to steal the ``struct page`` attached to ``buf``. If successful, this function returns 0 and returns with the page locked. The caller may then reuse the page
for whatever he wishes; the typical use is insertion into a different file page cache.
