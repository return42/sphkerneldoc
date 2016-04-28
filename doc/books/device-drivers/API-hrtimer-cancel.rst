.. -*- coding: utf-8; mode: rst -*-

.. _API-hrtimer-cancel:

==============
hrtimer_cancel
==============

*man hrtimer_cancel(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
