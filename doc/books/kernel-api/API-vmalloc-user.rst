
.. _API-vmalloc-user:

============
vmalloc_user
============

*man vmalloc_user(9)*

*4.6.0-rc1*

allocate zeroed virtually contiguous memory for userspace


Synopsis
========

.. c:function:: void ⋆ vmalloc_user( unsigned long size )

Arguments
=========

``size``
    allocation size


Description
===========

The resulting memory area is zeroed so it can be mapped to userspace without leaking data.
