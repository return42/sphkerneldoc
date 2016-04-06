
.. _API-vmalloc-32-user:

===============
vmalloc_32_user
===============

*man vmalloc_32_user(9)*

*4.6.0-rc1*

allocate zeroed virtually contiguous 32bit memory


Synopsis
========

.. c:function:: void ⋆ vmalloc_32_user( unsigned long size )

Arguments
=========

``size``
    allocation size


Description
===========

The resulting memory area is 32bit addressable and zeroed so it can be mapped to userspace without leaking data.
