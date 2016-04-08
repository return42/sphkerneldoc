
.. _API-xdr-buf-subsegment:

==================
xdr_buf_subsegment
==================

*man xdr_buf_subsegment(9)*

*4.6.0-rc1*

set subbuf to a portion of buf


Synopsis
========

.. c:function:: int xdr_buf_subsegment( struct xdr_buf * buf, struct xdr_buf * subbuf, unsigned int base, unsigned int len )

Arguments
=========

``buf``
    an xdr buffer

``subbuf``
    the result buffer

``base``
    beginning of range in bytes

``len``
    length of range in bytes


Description
===========

sets ``subbuf`` to an xdr buffer representing the portion of ``buf`` of length ``len`` starting at offset ``base``.

``buf`` and ``subbuf`` may be pointers to the same struct xdr_buf.

Returns -1 if base of length are out of bounds.
