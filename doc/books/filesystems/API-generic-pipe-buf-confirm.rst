.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-pipe-buf-confirm:

========================
generic_pipe_buf_confirm
========================

*man generic_pipe_buf_confirm(9)*

*4.6.0-rc5*

verify contents of the pipe buffer


Synopsis
========

.. c:function:: int generic_pipe_buf_confirm( struct pipe_inode_info * info, struct pipe_buffer * buf )

Arguments
=========

``info``
    the pipe that the buffer belongs to

``buf``
    the buffer to confirm


Description
===========

This function does nothing, because the generic pipe code uses pages
that are always good when inserted into the pipe.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
