.. -*- coding: utf-8; mode: rst -*-

.. _API-hrtimer-try-to-cancel:

=====================
hrtimer_try_to_cancel
=====================

*man hrtimer_try_to_cancel(9)*

*4.6.0-rc5*

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

0 when the timer was not active 1 when the timer was active -1 when the
timer is currently excuting the callback function and cannot be stopped


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
