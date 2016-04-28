.. -*- coding: utf-8; mode: rst -*-

.. _API-aica-rtc-settimeofday:

=====================
aica_rtc_settimeofday
=====================

*man aica_rtc_settimeofday(9)*

*4.6.0-rc5*

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

Adjusts the given ``tv`` to the AICA Epoch and sets the RTC seconds
counter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
