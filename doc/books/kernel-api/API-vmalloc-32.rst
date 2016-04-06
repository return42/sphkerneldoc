
.. _API-vmalloc-32:

==========
vmalloc_32
==========

*man vmalloc_32(9)*

*4.6.0-rc1*

allocate virtually contiguous memory (32bit addressable)


Synopsis
========

.. c:function:: void ⋆ vmalloc_32( unsigned long size )

Arguments
=========

``size``
    allocation size


Description
===========

Allocate enough 32bit PA addressable pages to cover ``size`` from the page level allocator and map them into contiguous kernel virtual space.
