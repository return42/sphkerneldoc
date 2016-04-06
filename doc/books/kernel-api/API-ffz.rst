
.. _API-ffz:

===
ffz
===

*man ffz(9)*

*4.6.0-rc1*

find first zero bit in word


Synopsis
========

.. c:function:: unsigned long ffz( unsigned long word )

Arguments
=========

``word``
    The word to search


Description
===========

Undefined if no zero exists, so code should check against ~0UL first.
