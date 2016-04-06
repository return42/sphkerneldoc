
.. _API-generic-file-splice-read:

========================
generic_file_splice_read
========================

*man generic_file_splice_read(9)*

*4.6.0-rc1*

splice data from file to a pipe


Synopsis
========

.. c:function:: ssize_t generic_file_splice_read( struct file * in, loff_t * ppos, struct pipe_inode_info * pipe, size_t len, unsigned int flags )

Arguments
=========

``in``
    file to splice from

``ppos``
    position in ``in``

``pipe``
    pipe to splice to

``len``
    number of bytes to splice

``flags``
    splice modifier flags


Description
===========

Will read pages from given file and fill them into a pipe. Can be used as long as the address_space operations for the source implements a ``readpage`` hook.
