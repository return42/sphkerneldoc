
.. _API---ffs:

=====
__ffs
=====

*man __ffs(9)*

*4.6.0-rc1*

find first set bit in word


Synopsis
========

.. c:function:: unsigned long __ffs( unsigned long word )

Arguments
=========

``word``
    The word to search


Description
===========

Undefined if no bit exists, so code should check against 0 first.
