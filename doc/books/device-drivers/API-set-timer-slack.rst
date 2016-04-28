.. -*- coding: utf-8; mode: rst -*-

.. _API-set-timer-slack:

===============
set_timer_slack
===============

*man set_timer_slack(9)*

*4.6.0-rc5*

set the allowed slack for a timer


Synopsis
========

.. c:function:: void set_timer_slack( struct timer_list * timer, int slack_hz )

Arguments
=========

``timer``
    the timer to be modified

``slack_hz``
    the amount of time (in jiffies) allowed for rounding


Description
===========

Set the amount of time, in jiffies, that a certain timer has in terms of
slack. By setting this value, the timer subsystem will schedule the
actual timer somewhere between the time ``mod_timer`` asks for, and that
time plus the slack.

By setting the slack to -1, a percentage of the delay is used instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
