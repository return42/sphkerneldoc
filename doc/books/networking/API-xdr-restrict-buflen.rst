.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-restrict-buflen:

===================
xdr_restrict_buflen
===================

*man xdr_restrict_buflen(9)*

*4.6.0-rc5*

decrease available buffer space


Synopsis
========

.. c:function:: int xdr_restrict_buflen( struct xdr_stream * xdr, int newbuflen )

Arguments
=========

``xdr``
    pointer to xdr_stream

``newbuflen``
    new maximum number of bytes available


Description
===========

Adjust our idea of how much space is available in the buffer. If we've
already used too much space in the buffer, returns -1. If the available
space is already smaller than newbuflen, returns 0 and does nothing.
Otherwise, adjusts xdr->buf->buflen to newbuflen and ensures xdr->end is
set at most offset newbuflen from the start of the buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
