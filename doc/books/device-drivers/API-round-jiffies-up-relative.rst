
.. _API-round-jiffies-up-relative:

=========================
round_jiffies_up_relative
=========================

*man round_jiffies_up_relative(9)*

*4.6.0-rc1*

function to round jiffies up to a full second


Synopsis
========

.. c:function:: unsigned long round_jiffies_up_relative( unsigned long j )

Arguments
=========

``j``
    the time in (relative) jiffies that should be rounded


Description
===========

This is the same as ``round_jiffies_relative`` except that it will never round down. This is useful for timeouts for which the exact time of firing does not matter too much, as
long as they don't fire too early.
