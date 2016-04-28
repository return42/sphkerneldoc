.. -*- coding: utf-8; mode: rst -*-

.. _API-aica-rtc-gettimeofday:

=====================
aica_rtc_gettimeofday
=====================

*man aica_rtc_gettimeofday(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
