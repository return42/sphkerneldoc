.. -*- coding: utf-8; mode: rst -*-

.. _API-hrtimer-init:

============
hrtimer_init
============

*man hrtimer_init(9)*

*4.6.0-rc5*

initialize a timer to the given clock


Synopsis
========

.. c:function:: void hrtimer_init( struct hrtimer * timer, clockid_t clock_id, enum hrtimer_mode mode )

Arguments
=========

``timer``
    the timer to be initialized

``clock_id``
    the clock to be used

``mode``
    timer mode abs/rel


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
