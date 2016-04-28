.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-encode-opaque-fixed:

=======================
xdr_encode_opaque_fixed
=======================

*man xdr_encode_opaque_fixed(9)*

*4.6.0-rc5*

Encode fixed length opaque data


Synopsis
========

.. c:function:: __be32 * xdr_encode_opaque_fixed( __be32 * p, const void * ptr, unsigned int nbytes )

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

Copy the array of data of length nbytes at ptr to the XDR buffer at
position p, then align to the next 32-bit boundary by padding with zero
bytes (see RFC1832).


Note
====

if ptr is NULL, only the padding is performed.

Returns the updated current XDR buffer position


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
