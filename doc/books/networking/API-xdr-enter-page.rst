.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-enter-page:

==============
xdr_enter_page
==============

*man xdr_enter_page(9)*

*4.6.0-rc5*

decode data from the XDR page


Synopsis
========

.. c:function:: void xdr_enter_page( struct xdr_stream * xdr, unsigned int len )

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
“len” bytes is moved into the XDR tail[]. The current pointer is then
repositioned at the beginning of the first XDR page.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
