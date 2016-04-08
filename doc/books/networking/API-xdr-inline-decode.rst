
.. _API-xdr-inline-decode:

=================
xdr_inline_decode
=================

*man xdr_inline_decode(9)*

*4.6.0-rc1*

Retrieve XDR data to decode


Synopsis
========

.. c:function:: __be32 ⋆ xdr_inline_decode( struct xdr_stream * xdr, size_t nbytes )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``nbytes``
    number of bytes of data to decode


Description
===========

Check if the input buffer is long enough to enable us to decode 'nbytes' more bytes of data starting at the current position. If so return the current pointer, then update the
current pointer position.
