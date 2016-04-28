.. -*- coding: utf-8; mode: rst -*-

.. _API-ktime-after:

===========
ktime_after
===========

*man ktime_after(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
