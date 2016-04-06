
.. _API-splice-to-pipe:

==============
splice_to_pipe
==============

*man splice_to_pipe(9)*

*4.6.0-rc1*

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

``spd`` contains a map of pages and len/offset tuples, along with the struct pipe_buf_operations associated with these pages. This function will link that data to the pipe.
