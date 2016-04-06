
.. _API-hrtimer-cancel:

==============
hrtimer_cancel
==============

*man hrtimer_cancel(9)*

*4.6.0-rc1*

cancel a timer and wait for the handler to finish.


Synopsis
========

.. c:function:: int hrtimer_cancel( struct hrtimer * timer )

Arguments
=========

``timer``
    the timer to be cancelled


Returns
=======

0 when the timer was not active 1 when the timer was active
