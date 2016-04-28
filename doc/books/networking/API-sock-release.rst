.. -*- coding: utf-8; mode: rst -*-

.. _API-sock-release:

============
sock_release
============

*man sock_release(9)*

*4.6.0-rc5*

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

The socket is released from the protocol stack if it has a release
callback, and the inode is then released if the socket is bound to an
inode not a file.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
