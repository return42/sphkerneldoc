.. -*- coding: utf-8; mode: rst -*-

.. _API-kernel-recvmsg:

==============
kernel_recvmsg
==============

*man kernel_recvmsg(9)*

*4.6.0-rc5*

Receive a message from a socket (kernel space)


Synopsis
========

.. c:function:: int kernel_recvmsg( struct socket * sock, struct msghdr * msg, struct kvec * vec, size_t num, size_t size, int flags )

Arguments
=========

``sock``
    The socket to receive the message from

``msg``
    Received message

``vec``
    Input s/g array for message data

``num``
    Size of input s/g array

``size``
    Number of bytes to read

``flags``
    Message flags (MSG_DONTWAIT, etc...)


Description
===========

On return the msg structure contains the scatter/gather array passed in
the vec argument. The array is modified so that it consists of the
unfilled portion of the original array.

The returned value is the total number of bytes received, or an error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
