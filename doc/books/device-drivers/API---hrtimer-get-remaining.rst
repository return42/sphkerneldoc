.. -*- coding: utf-8; mode: rst -*-

.. _API---hrtimer-get-remaining:

=======================
__hrtimer_get_remaining
=======================

*man __hrtimer_get_remaining(9)*

*4.6.0-rc5*

get remaining time for the timer


Synopsis
========

.. c:function:: ktime_t __hrtimer_get_remaining( const struct hrtimer * timer, bool adjust )

Arguments
=========

``timer``
    the timer to read

``adjust``
    adjust relative timers when CONFIG_TIME_LOW_RES=y


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
