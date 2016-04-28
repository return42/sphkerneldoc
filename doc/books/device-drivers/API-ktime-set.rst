.. -*- coding: utf-8; mode: rst -*-

.. _API-ktime-set:

=========
ktime_set
=========

*man ktime_set(9)*

*4.6.0-rc5*

Set a ktime_t variable from a seconds/nanoseconds value


Synopsis
========

.. c:function:: ktime_t ktime_set( const s64 secs, const unsigned long nsecs )

Arguments
=========

``secs``
    seconds to set

``nsecs``
    nanoseconds to set


Return
======

The ktime_t representation of the value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
