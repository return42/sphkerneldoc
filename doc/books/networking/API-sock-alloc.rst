
.. _API-sock-alloc:

==========
sock_alloc
==========

*man sock_alloc(9)*

*4.6.0-rc1*

allocate a socket


Synopsis
========

.. c:function:: struct socket ⋆ sock_alloc( void )

Arguments
=========

``void``
    no arguments


Description
===========

Allocate a new inode and socket object. The two are bound together and initialised. The socket is then returned. If we are out of inodes NULL is returned.
