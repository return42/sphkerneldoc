
.. _API-ktime-equal:

===========
ktime_equal
===========

*man ktime_equal(9)*

*4.6.0-rc1*

Compares two ktime_t variables to see if they are equal


Synopsis
========

.. c:function:: int ktime_equal( const ktime_t cmp1, const ktime_t cmp2 )

Arguments
=========

``cmp1``
    comparable1

``cmp2``
    comparable2


Description
===========

Compare two ktime_t variables.


Return
======

1 if equal.
