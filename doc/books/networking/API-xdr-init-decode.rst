
.. _API-xdr-init-decode:

===============
xdr_init_decode
===============

*man xdr_init_decode(9)*

*4.6.0-rc1*

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
