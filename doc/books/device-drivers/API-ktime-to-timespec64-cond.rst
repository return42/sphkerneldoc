.. -*- coding: utf-8; mode: rst -*-

.. _API-ktime-to-timespec64-cond:

========================
ktime_to_timespec64_cond
========================

*man ktime_to_timespec64_cond(9)*

*4.6.0-rc5*

convert a ktime_t variable to timespec64 format only if the variable
contains data


Synopsis
========

.. c:function:: bool ktime_to_timespec64_cond( const ktime_t kt, struct timespec64 * ts )

Arguments
=========

``kt``
    the ktime_t variable to convert

``ts``
    the timespec variable to store the result in


Return
======

``true`` if there was a successful conversion, ``false`` if kt was 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
