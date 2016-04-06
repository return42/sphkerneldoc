
.. _API-abs:

===
abs
===

*man abs(9)*

*4.6.0-rc1*

return absolute value of an argument


Synopsis
========

.. c:function:: abs( x )

Arguments
=========

``x``
    the value. If it is unsigned type, it is converted to signed type first. char is treated as if it was signed (regardless of whether it really is) but the macro's return type is
    preserved as char.


Return
======

an absolute value of x.
