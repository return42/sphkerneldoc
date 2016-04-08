
.. _API-aica-rtc-settimeofday:

=====================
aica_rtc_settimeofday
=====================

*man aica_rtc_settimeofday(9)*

*4.6.0-rc1*

Set the AICA RTC to the current time


Synopsis
========

.. c:function:: int aica_rtc_settimeofday( const time_t secs )

Arguments
=========

``secs``
    contains the time_t to set


Description
===========

Adjusts the given ``tv`` to the AICA Epoch and sets the RTC seconds counter.
