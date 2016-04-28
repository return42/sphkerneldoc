.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-wmem-alloc-get:

=================
sk_wmem_alloc_get
=================

*man sk_wmem_alloc_get(9)*

*4.6.0-rc5*

returns write allocations


Synopsis
========

.. c:function:: int sk_wmem_alloc_get( const struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

Returns sk_wmem_alloc minus initial offset of one


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
