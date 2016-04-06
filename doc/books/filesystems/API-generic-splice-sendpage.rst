
.. _API-generic-splice-sendpage:

=======================
generic_splice_sendpage
=======================

*man generic_splice_sendpage(9)*

*4.6.0-rc1*

splice data from a pipe to a socket


Synopsis
========

.. c:function:: ssize_t generic_splice_sendpage( struct pipe_inode_info * pipe, struct file * out, loff_t * ppos, size_t len, unsigned int flags )

Arguments
=========

``pipe``
    pipe to splice from

``out``
    socket to write to

``ppos``
    position in ``out``

``len``
    number of bytes to splice

``flags``
    splice modifier flags


Description
===========

Will send ``len`` bytes from the pipe to a network socket. No data copying is involved.
