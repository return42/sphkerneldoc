.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-inline-decode:

=================
xdr_inline_decode
=================

*man xdr_inline_decode(9)*

*4.6.0-rc5*

Retrieve XDR data to decode


Synopsis
========

.. c:function:: __be32 * xdr_inline_decode( struct xdr_stream * xdr, size_t nbytes )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``nbytes``
    number of bytes of data to decode


Description
===========

Check if the input buffer is long enough to enable us to decode 'nbytes'
more bytes of data starting at the current position. If so return the
current pointer, then update the current pointer position.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
