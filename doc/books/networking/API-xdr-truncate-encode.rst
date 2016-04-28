.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-truncate-encode:

===================
xdr_truncate_encode
===================

*man xdr_truncate_encode(9)*

*4.6.0-rc5*

truncate an encode buffer


Synopsis
========

.. c:function:: void xdr_truncate_encode( struct xdr_stream * xdr, size_t len )

Arguments
=========

``xdr``
    pointer to xdr_stream

``len``
    new length of buffer


Description
===========

Truncates the xdr stream, so that xdr->buf->len == len, and xdr->p
points at offset len from the start of the buffer, and head, tail, and
page lengths are adjusted to correspond.

If this means moving xdr->p to a different buffer, we assume that that
the end pointer should be set to the end of the current page, except in
the case of the head buffer when we assume the head buffer's current
length represents the end of the available buffer.

This is *not* safe to use on a buffer that already has inlined page
cache pages (as in a zero-copy server read reply), except for the simple
case of truncating from one position in the tail to another.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
