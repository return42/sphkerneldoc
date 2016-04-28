.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-buf-trim:

============
xdr_buf_trim
============

*man xdr_buf_trim(9)*

*4.6.0-rc5*

lop at most “len” bytes off the end of “buf”


Synopsis
========

.. c:function:: void xdr_buf_trim( struct xdr_buf * buf, unsigned int len )

Arguments
=========

``buf``
    buf to be trimmed

``len``
    number of bytes to reduce “buf” by


Description
===========

Trim an xdr_buf by the given number of bytes by fixing up the lengths.
Note that it's possible that we'll trim less than that amount if the
xdr_buf is too small, or if (for instance) it's all in the head and the
parser has already read too far into it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
