
.. _API-ktime-to-timespec-cond:

======================
ktime_to_timespec_cond
======================

*man ktime_to_timespec_cond(9)*

*4.6.0-rc1*

convert a ktime_t variable to timespec format only if the variable contains data


Synopsis
========

.. c:function:: bool ktime_to_timespec_cond( const ktime_t kt, struct timespec * ts )

Arguments
=========

``kt``
    the ktime_t variable to convert

``ts``
    the timespec variable to store the result in


Return
======

``true`` if there was a successful conversion, ``false`` if kt was 0.
