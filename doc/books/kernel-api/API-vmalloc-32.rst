.. -*- coding: utf-8; mode: rst -*-

.. _API-vmalloc-32:

==========
vmalloc_32
==========

*man vmalloc_32(9)*

*4.6.0-rc5*

allocate virtually contiguous memory (32bit addressable)


Synopsis
========

.. c:function:: void * vmalloc_32( unsigned long size )

Arguments
=========

``size``
    allocation size


Description
===========

Allocate enough 32bit PA addressable pages to cover ``size`` from the
page level allocator and map them into contiguous kernel virtual space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
