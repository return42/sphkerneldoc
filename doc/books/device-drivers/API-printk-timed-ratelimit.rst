
.. _API-printk-timed-ratelimit:

======================
printk_timed_ratelimit
======================

*man printk_timed_ratelimit(9)*

*4.6.0-rc1*

caller-controlled printk ratelimiting


Synopsis
========

.. c:function:: bool printk_timed_ratelimit( unsigned long * caller_jiffies, unsigned int interval_msecs )

Arguments
=========

``caller_jiffies``
    pointer to caller's state

``interval_msecs``
    minimum interval between prints


Description
===========

``printk_timed_ratelimit`` returns true if more than ``interval_msecs`` milliseconds have elapsed since the last time ``printk_timed_ratelimit`` returned true.
