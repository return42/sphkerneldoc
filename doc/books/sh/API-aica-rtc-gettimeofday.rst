
.. _API-aica-rtc-gettimeofday:

=====================
aica_rtc_gettimeofday
=====================

*man aica_rtc_gettimeofday(9)*

*4.6.0-rc1*

Get the time from the AICA RTC


Synopsis
========

.. c:function:: void aica_rtc_gettimeofday( struct timespec * ts )

Arguments
=========

``ts``
    pointer to resulting timespec


Description
===========

Grabs the current RTC seconds counter and adjusts it to the Unix Epoch.
