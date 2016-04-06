
.. _API-hrtimer-try-to-cancel:

=====================
hrtimer_try_to_cancel
=====================

*man hrtimer_try_to_cancel(9)*

*4.6.0-rc1*

try to deactivate a timer


Synopsis
========

.. c:function:: int hrtimer_try_to_cancel( struct hrtimer * timer )

Arguments
=========

``timer``
    hrtimer to stop


Returns
=======

0 when the timer was not active 1 when the timer was active -1 when the timer is currently excuting the callback function and cannot be stopped
