
.. _API-sock-release:

============
sock_release
============

*man sock_release(9)*

*4.6.0-rc1*

close a socket


Synopsis
========

.. c:function:: void sock_release( struct socket * sock )

Arguments
=========

``sock``
    socket to close


Description
===========

The socket is released from the protocol stack if it has a release callback, and the inode is then released if the socket is bound to an inode not a file.
