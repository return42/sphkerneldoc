.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-init-decode:

===============
xdr_init_decode
===============

*man xdr_init_decode(9)*

*4.6.0-rc5*

Initialize an xdr_stream for decoding data.


Synopsis
========

.. c:function:: void xdr_init_decode( struct xdr_stream * xdr, struct xdr_buf * buf, __be32 * p )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``buf``
    pointer to XDR buffer from which to decode data

``p``
    current pointer inside XDR buffer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
