.. -*- coding: utf-8; mode: rst -*-

.. _API---ffs:

=====
__ffs
=====

*man __ffs(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
