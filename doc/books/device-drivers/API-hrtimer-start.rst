.. -*- coding: utf-8; mode: rst -*-

.. _API-hrtimer-start:

=============
hrtimer_start
=============

*man hrtimer_start(9)*

*4.6.0-rc5*

(re)start an hrtimer on the current CPU


Synopsis
========

.. c:function:: void hrtimer_start( struct hrtimer * timer, ktime_t tim, const enum hrtimer_mode mode )

Arguments
=========

``timer``
    the timer to be added

``tim``
    expiry time

``mode``
    expiry mode: absolute (HRTIMER_MODE_ABS) or relative
    (HRTIMER_MODE_REL)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
