
.. _API-kzalloc:

=======
kzalloc
=======

*man kzalloc(9)*

*4.6.0-rc1*

allocate memory. The memory is set to zero.


Synopsis
========

.. c:function:: void ⋆ kzalloc( size_t size, gfp_t flags )

Arguments
=========

``size``
    how many bytes of memory are required.

``flags``
    the type of memory to allocate (see kmalloc).
