.. -*- coding: utf-8; mode: rst -*-

.. _API-sock-alloc:

==========
sock_alloc
==========

*man sock_alloc(9)*

*4.6.0-rc5*

allocate a socket


Synopsis
========

.. c:function:: struct socket * sock_alloc( void )

Arguments
=========

``void``
    no arguments


Description
===========

Allocate a new inode and socket object. The two are bound together and
initialised. The socket is then returned. If we are out of inodes NULL
is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
