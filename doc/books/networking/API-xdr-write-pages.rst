.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-write-pages:

===============
xdr_write_pages
===============

*man xdr_write_pages(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
