.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-pipe-buf-steal:

======================
generic_pipe_buf_steal
======================

*man generic_pipe_buf_steal(9)*

*4.6.0-rc5*

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

This function attempts to steal the ``struct page`` attached to ``buf``.
If successful, this function returns 0 and returns with the page locked.
The caller may then reuse the page for whatever he wishes; the typical
use is insertion into a different file page cache.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
