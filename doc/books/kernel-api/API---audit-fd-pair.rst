
.. _API---audit-fd-pair:

===============
__audit_fd_pair
===============

*man __audit_fd_pair(9)*

*4.6.0-rc1*

record audit data for pipe and socketpair


Synopsis
========

.. c:function:: void __audit_fd_pair( int fd1, int fd2 )

Arguments
=========

``fd1``
    the first file descriptor

``fd2``
    the second file descriptor
