
.. _API-vmalloc:

=======
vmalloc
=======

*man vmalloc(9)*

*4.6.0-rc1*

allocate virtually contiguous memory


Synopsis
========

.. c:function:: void ⋆ vmalloc( unsigned long size )

Arguments
=========

``size``
    allocation size Allocate enough pages to cover ``size`` from the page level allocator and map them into contiguous kernel virtual space.


Description
===========

For tight control over page level allocator and protection flags use ``__vmalloc`` instead.
