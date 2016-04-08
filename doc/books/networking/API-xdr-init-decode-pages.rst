
.. _API-xdr-init-decode-pages:

=====================
xdr_init_decode_pages
=====================

*man xdr_init_decode_pages(9)*

*4.6.0-rc1*

Initialize an xdr_stream for decoding data.


Synopsis
========

.. c:function:: void xdr_init_decode_pages( struct xdr_stream * xdr, struct xdr_buf * buf, struct page ** pages, unsigned int len )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``buf``
    pointer to XDR buffer from which to decode data

``pages``
    list of pages to decode into

``len``
    length in bytes of buffer in pages
