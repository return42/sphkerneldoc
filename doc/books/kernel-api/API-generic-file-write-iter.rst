
.. _API-generic-file-write-iter:

=======================
generic_file_write_iter
=======================

*man generic_file_write_iter(9)*

*4.6.0-rc1*

write data to a file


Synopsis
========

.. c:function:: ssize_t generic_file_write_iter( struct kiocb * iocb, struct iov_iter * from )

Arguments
=========

``iocb``
    IO state structure

``from``
    iov_iter with data to write


Description
===========

This is a wrapper around ``__generic_file_write_iter`` to be used by most filesystems. It takes care of syncing the file in case of O_SYNC file and acquires i_mutex as needed.
