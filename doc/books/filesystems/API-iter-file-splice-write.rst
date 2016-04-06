
.. _API-iter-file-splice-write:

======================
iter_file_splice_write
======================

*man iter_file_splice_write(9)*

*4.6.0-rc1*

splice data from a pipe to a file


Synopsis
========

.. c:function:: ssize_t iter_file_splice_write( struct pipe_inode_info * pipe, struct file * out, loff_t * ppos, size_t len, unsigned int flags )

Arguments
=========

``pipe``
    pipe info

``out``
    file to write to

``ppos``
    position in ``out``

``len``
    number of bytes to splice

``flags``
    splice modifier flags


Description
===========

Will either move or copy pages (determined by ``flags`` options) from the given pipe inode to the given file. This one is ->write_iter-based.
