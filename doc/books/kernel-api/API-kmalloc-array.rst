
.. _API-kmalloc-array:

=============
kmalloc_array
=============

*man kmalloc_array(9)*

*4.6.0-rc1*

allocate memory for an array.


Synopsis
========

.. c:function:: void ⋆ kmalloc_array( size_t n, size_t size, gfp_t flags )

Arguments
=========

``n``
    number of elements.

``size``
    element size.

``flags``
    the type of memory to allocate (see kmalloc).
