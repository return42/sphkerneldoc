
.. _API-xdr-commit-encode:

=================
xdr_commit_encode
=================

*man xdr_commit_encode(9)*

*4.6.0-rc1*

Ensure all data is written to buffer


Synopsis
========

.. c:function:: void xdr_commit_encode( struct xdr_stream * xdr )

Arguments
=========

``xdr``
    pointer to xdr_stream


Description
===========

We handle encoding across page boundaries by giving the caller a temporary location to write to, then later copying the data into place; xdr_commit_encode does that copying.

Normally the caller doesn't need to call this directly, as the following xdr_reserve_space will do it. But an explicit call may be required at the end of encoding, or any other
time when the xdr_buf data might be read.
