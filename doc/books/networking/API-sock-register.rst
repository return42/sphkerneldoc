
.. _API-sock-register:

=============
sock_register
=============

*man sock_register(9)*

*4.6.0-rc1*

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

This function is called by a protocol handler that wants to advertise its address family, and have it linked into the socket interface. The value ops->family corresponds to the
socket system call protocol family.
