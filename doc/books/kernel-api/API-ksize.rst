.. -*- coding: utf-8; mode: rst -*-

.. _API-ksize:

=====
ksize
=====

*man ksize(9)*

*4.6.0-rc5*

get the actual amount of memory allocated for a given object


Synopsis
========

.. c:function:: size_t ksize( const void * objp )

Arguments
=========

``objp``
    Pointer to the object


Description
===========

kmalloc may internally round up allocations and return more memory than
requested. ``ksize`` can be used to determine the actual amount of
memory allocated. The caller may use this additional memory, even though
a smaller amount of memory was initially specified with the kmalloc
call. The caller must guarantee that objp points to a valid object
previously allocated with either ``kmalloc`` or ``kmem_cache_alloc``.
The object must not be freed during the duration of the call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
