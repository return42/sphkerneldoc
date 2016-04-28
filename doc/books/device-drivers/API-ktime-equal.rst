.. -*- coding: utf-8; mode: rst -*-

.. _API-ktime-equal:

===========
ktime_equal
===========

*man ktime_equal(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
