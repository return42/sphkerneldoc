.. -*- coding: utf-8; mode: rst -*-

.. _API-ktime-before:

============
ktime_before
============

*man ktime_before(9)*

*4.6.0-rc5*

Compare if a ktime_t value is smaller than another one.


Synopsis
========

.. c:function:: bool ktime_before( const ktime_t cmp1, const ktime_t cmp2 )

Arguments
=========

``cmp1``
    comparable1

``cmp2``
    comparable2


Return
======

true if cmp1 happened before cmp2.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
