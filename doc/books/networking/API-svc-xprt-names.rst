.. -*- coding: utf-8; mode: rst -*-

.. _API-svc-xprt-names:

==============
svc_xprt_names
==============

*man svc_xprt_names(9)*

*4.6.0-rc5*

format a buffer with a list of transport names


Synopsis
========

.. c:function:: int svc_xprt_names( struct svc_serv * serv, char * buf, const int buflen )

Arguments
=========

``serv``
    pointer to an RPC service

``buf``
    pointer to a buffer to be filled in

``buflen``
    length of buffer to be filled in


Description
===========

Fills in ``buf`` with a string containing a list of transport names,
each name terminated with '\\n'.

Returns positive length of the filled-in string on success; otherwise a
negative errno value is returned if an error occurs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
