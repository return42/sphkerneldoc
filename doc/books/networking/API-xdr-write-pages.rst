
.. _API-xdr-write-pages:

===============
xdr_write_pages
===============

*man xdr_write_pages(9)*

*4.6.0-rc1*

Insert a list of pages into an XDR buffer for sending


Synopsis
========

.. c:function:: void xdr_write_pages( struct xdr_stream * xdr, struct page ** pages, unsigned int base, unsigned int len )

Arguments
=========

``xdr``
    pointer to xdr_stream

``pages``
    list of pages

``base``
    offset of first byte

``len``
    length of data in bytes
