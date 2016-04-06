
.. _API-generic-file-read-iter:

======================
generic_file_read_iter
======================

*man generic_file_read_iter(9)*

*4.6.0-rc1*

generic filesystem read routine


Synopsis
========

.. c:function:: ssize_t generic_file_read_iter( struct kiocb * iocb, struct iov_iter * iter )

Arguments
=========

``iocb``
    kernel I/O control block

``iter``
    destination for the data read


Description
===========

This is the “``read_iter``” routine for all filesystems that can use the page cache directly.
