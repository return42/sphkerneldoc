
.. _API-xdr-encode-opaque:

=================
xdr_encode_opaque
=================

*man xdr_encode_opaque(9)*

*4.6.0-rc1*

Encode variable length opaque data


Synopsis
========

.. c:function:: __be32 ⋆ xdr_encode_opaque( __be32 * p, const void * ptr, unsigned int nbytes )

Arguments
=========

``p``
    pointer to current position in XDR buffer.

``ptr``
    pointer to data to encode (or NULL)

``nbytes``
    size of data.


Description
===========

Returns the updated current XDR buffer position
