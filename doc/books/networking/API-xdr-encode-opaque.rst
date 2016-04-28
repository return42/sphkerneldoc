.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-encode-opaque:

=================
xdr_encode_opaque
=================

*man xdr_encode_opaque(9)*

*4.6.0-rc5*

Encode variable length opaque data


Synopsis
========

.. c:function:: __be32 * xdr_encode_opaque( __be32 * p, const void * ptr, unsigned int nbytes )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
