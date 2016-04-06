
.. _API-ktime-after:

===========
ktime_after
===========

*man ktime_after(9)*

*4.6.0-rc1*

Compare if a ktime_t value is bigger than another one.


Synopsis
========

.. c:function:: bool ktime_after( const ktime_t cmp1, const ktime_t cmp2 )

Arguments
=========

``cmp1``
    comparable1

``cmp2``
    comparable2


Return
======

true if cmp1 happened after cmp2.
