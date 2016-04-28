.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-set-scratch-buffer:

======================
xdr_set_scratch_buffer
======================

*man xdr_set_scratch_buffer(9)*

*4.6.0-rc5*

Attach a scratch buffer for decoding data.


Synopsis
========

.. c:function:: void xdr_set_scratch_buffer( struct xdr_stream * xdr, void * buf, size_t buflen )

Arguments
=========

``xdr``
    pointer to xdr_stream struct

``buf``
    pointer to an empty buffer

``buflen``
    size of 'buf'


Description
===========

The scratch buffer is used when decoding from an array of pages. If an
``xdr_inline_decode`` call spans across page boundaries, then we copy
the data into the scratch buffer in order to allow linear access.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
