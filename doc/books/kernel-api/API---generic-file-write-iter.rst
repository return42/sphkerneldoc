
.. _API---generic-file-write-iter:

=========================
__generic_file_write_iter
=========================

*man __generic_file_write_iter(9)*

*4.6.0-rc1*

write data to a file


Synopsis
========

.. c:function:: ssize_t __generic_file_write_iter( struct kiocb * iocb, struct iov_iter * from )

Arguments
=========

``iocb``
    IO state structure (file, offset, etc.)

``from``
    iov_iter with data to write


Description
===========

This function does all the work needed for actually writing data to a file. It does all basic checks, removes SUID from the file, updates modification times and calls proper
subroutines depending on whether we do direct IO or a standard buffered write.

It expects i_mutex to be grabbed unless we work on a block device or similar object which does not need locking at all.

This function does ⋆not⋆ take care of syncing data in case of O_SYNC write. A caller has to handle it. This is mainly due to the fact that we want to avoid syncing under i_mutex.
