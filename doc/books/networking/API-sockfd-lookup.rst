.. -*- coding: utf-8; mode: rst -*-

.. _API-sockfd-lookup:

=============
sockfd_lookup
=============

*man sockfd_lookup(9)*

*4.6.0-rc5*

Go from a file number to its socket slot


Synopsis
========

.. c:function:: struct socket * sockfd_lookup( int fd, int * err )

Arguments
=========

``fd``
    file handle

``err``
    pointer to an error code return


Description
===========

The file handle passed in is locked and the socket it is bound too is
returned. If an error occurs the err pointer is overwritten with a
negative errno code and NULL is returned. The function checks for both
invalid handles and passing a handle which is not a socket.

On a success the socket object pointer is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
