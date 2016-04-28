.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-read-pages:

==============
xdr_read_pages
==============

*man xdr_read_pages(9)*

*4.6.0-rc5*

Ensure page-based XDR data to decode is aligned at current pointer
position


Synopsis
========

.. c:function:: unsigned int xdr_read_pages( struct xdr_stream * xdr, unsigned int len )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``len``
    number of bytes of page data


Description
===========

Moves data beyond the current pointer position from the XDR head[]
buffer into the page list. Any data that lies beyond current position +
“len” bytes is moved into the XDR tail[].

Returns the number of XDR encoded bytes now contained in the pages


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
