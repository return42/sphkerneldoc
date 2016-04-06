
.. _API-ktime-before:

============
ktime_before
============

*man ktime_before(9)*

*4.6.0-rc1*

Compare if a ktime_t value is smaller than another one.


Synopsis
========

.. c:function:: bool ktime_before( const ktime_t cmp1, const ktime_t cmp2 )

Arguments
=========

``cmp1``
    comparable1

``cmp2``
    comparable2


Return
======

true if cmp1 happened before cmp2.
