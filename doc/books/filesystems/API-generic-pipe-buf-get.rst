.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-pipe-buf-get:

====================
generic_pipe_buf_get
====================

*man generic_pipe_buf_get(9)*

*4.6.0-rc5*

get a reference to a ``struct pipe_buffer``


Synopsis
========

.. c:function:: void generic_pipe_buf_get( struct pipe_inode_info * pipe, struct pipe_buffer * buf )

Arguments
=========

``pipe``
    the pipe that the buffer belongs to

``buf``
    the buffer to get a reference to


Description
===========

This function grabs an extra reference to ``buf``. It's used in in the
``tee`` system call, when we duplicate the buffers in one pipe into
another.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
