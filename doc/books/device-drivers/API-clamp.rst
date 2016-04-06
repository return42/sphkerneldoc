
.. _API-clamp:

=====
clamp
=====

*man clamp(9)*

*4.6.0-rc1*

return a value clamped to a given range with strict typechecking


Synopsis
========

.. c:function:: clamp( val, lo, hi )

Arguments
=========

``val``
    current value

``lo``
    lowest allowable value

``hi``
    highest allowable value


Description
===========

This macro does strict typechecking of lo/hi to make sure they are of the same type as val. See the unnecessary pointer comparisons.
