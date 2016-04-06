
.. _API-ktime-compare:

=============
ktime_compare
=============

*man ktime_compare(9)*

*4.6.0-rc1*

Compares two ktime_t variables for less, greater or equal


Synopsis
========

.. c:function:: int ktime_compare( const ktime_t cmp1, const ktime_t cmp2 )

Arguments
=========

``cmp1``
    comparable1

``cmp2``
    comparable2


Return
======

... cmp1 < cmp2: return <0 cmp1 == cmp2: return 0 cmp1 > cmp2: return >0
