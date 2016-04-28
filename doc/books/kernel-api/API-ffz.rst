.. -*- coding: utf-8; mode: rst -*-

.. _API-ffz:

===
ffz
===

*man ffz(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
