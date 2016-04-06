
.. _API-kcalloc:

=======
kcalloc
=======

*man kcalloc(9)*

*4.6.0-rc1*

allocate memory for an array. The memory is set to zero.


Synopsis
========

.. c:function:: void ⋆ kcalloc( size_t n, size_t size, gfp_t flags )

Arguments
=========

``n``
    number of elements.

``size``
    element size.

``flags``
    the type of memory to allocate (see kmalloc).
