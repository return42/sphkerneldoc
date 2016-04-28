.. -*- coding: utf-8; mode: rst -*-

.. _API-hrtimer-forward:

===============
hrtimer_forward
===============

*man hrtimer_forward(9)*

*4.6.0-rc5*

forward the timer expiry


Synopsis
========

.. c:function:: u64 hrtimer_forward( struct hrtimer * timer, ktime_t now, ktime_t interval )

Arguments
=========

``timer``
    hrtimer to forward

``now``
    forward past this time

``interval``
    the interval to forward


Description
===========

Forward the timer expiry so it will expire in the future. Returns the
number of overruns.

Can be safely called from the callback function of ``timer``. If called
from other contexts ``timer`` must neither be enqueued nor running the
callback and the caller needs to take care of serialization.


Note
====

This only updates the timer expiry value and does not requeue the timer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
