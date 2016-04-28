.. -*- coding: utf-8; mode: rst -*-

.. _API-svc-find-xprt:

=============
svc_find_xprt
=============

*man svc_find_xprt(9)*

*4.6.0-rc5*

find an RPC transport instance


Synopsis
========

.. c:function:: struct svc_xprt * svc_find_xprt( struct svc_serv * serv, const char * xcl_name, struct net * net, const sa_family_t af, const unsigned short port )

Arguments
=========

``serv``
    pointer to svc_serv to search

``xcl_name``
    C string containing transport's class name

``net``
    owner net pointer

``af``
    Address family of transport's local address

``port``
    transport's IP port number


Description
===========

Return the transport instance pointer for the endpoint accepting
connections/peer traffic from the specified transport class, address
family and port.

Specifying 0 for the address family or port is effectively a wild-card,
and will result in matching the first transport in the service's list
that has a matching class name.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
