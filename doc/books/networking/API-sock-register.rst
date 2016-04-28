.. -*- coding: utf-8; mode: rst -*-

.. _API-sock-register:

=============
sock_register
=============

*man sock_register(9)*

*4.6.0-rc5*

add a socket protocol handler


Synopsis
========

.. c:function:: int sock_register( const struct net_proto_family * ops )

Arguments
=========

``ops``
    description of protocol


Description
===========

This function is called by a protocol handler that wants to advertise
its address family, and have it linked into the socket interface. The
value ops->family corresponds to the socket system call protocol family.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
