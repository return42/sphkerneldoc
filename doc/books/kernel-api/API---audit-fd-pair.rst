.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-fd-pair:

===============
__audit_fd_pair
===============

*man __audit_fd_pair(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
