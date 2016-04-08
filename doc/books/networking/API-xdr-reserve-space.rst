
.. _API-xdr-reserve-space:

=================
xdr_reserve_space
=================

*man xdr_reserve_space(9)*

*4.6.0-rc1*

Reserve buffer space for sending


Synopsis
========

.. c:function:: __be32 ⋆ xdr_reserve_space( struct xdr_stream * xdr, size_t nbytes )

Arguments
=========

``xdr``
    pointer to xdr_stream

``nbytes``
    number of bytes to reserve


Description
===========

Checks that we have enough buffer space to encode 'nbytes' more bytes of data. If so, update the total xdr_buf length, and adjust the length of the current kvec.
