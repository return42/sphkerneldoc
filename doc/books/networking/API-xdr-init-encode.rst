.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-init-encode:

===============
xdr_init_encode
===============

*man xdr_init_encode(9)*

*4.6.0-rc5*

Initialize a struct xdr_stream for sending data.


Synopsis
========

.. c:function:: void xdr_init_encode( struct xdr_stream * xdr, struct xdr_buf * buf, __be32 * p )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``buf``
    pointer to XDR buffer in which to encode data

``p``
    current pointer inside XDR buffer


Note
====

at the moment the RPC client only passes the length of our scratch
buffer in the xdr_buf's header kvec. Previously this meant we needed to
call ``xdr_adjust_iovec`` after encoding the data. With the new scheme,
the xdr_stream manages the details of the buffer length, and takes care
of adjusting the kvec length for us.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
