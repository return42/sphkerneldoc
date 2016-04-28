.. -*- coding: utf-8; mode: rst -*-

.. _API-splice-to-pipe:

==============
splice_to_pipe
==============

*man splice_to_pipe(9)*

*4.6.0-rc5*

fill passed data into a pipe


Synopsis
========

.. c:function:: ssize_t splice_to_pipe( struct pipe_inode_info * pipe, struct splice_pipe_desc * spd )

Arguments
=========

``pipe``
    pipe to fill

``spd``
    data to fill


Description
===========

``spd`` contains a map of pages and len/offset tuples, along with the
struct pipe_buf_operations associated with these pages. This function
will link that data to the pipe.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
