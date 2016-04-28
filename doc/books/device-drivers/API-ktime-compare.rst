.. -*- coding: utf-8; mode: rst -*-

.. _API-ktime-compare:

=============
ktime_compare
=============

*man ktime_compare(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
