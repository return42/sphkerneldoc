
.. _API-vzalloc:

=======
vzalloc
=======

*man vzalloc(9)*

*4.6.0-rc1*

allocate virtually contiguous memory with zero fill


Synopsis
========

.. c:function:: void ⋆ vzalloc( unsigned long size )

Arguments
=========

``size``
    allocation size Allocate enough pages to cover ``size`` from the page level allocator and map them into contiguous kernel virtual space. The memory allocated is set to zero.


Description
===========

For tight control over page level allocator and protection flags use ``__vmalloc`` instead.
