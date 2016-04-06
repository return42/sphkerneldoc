
.. _API-hrtimer-init:

============
hrtimer_init
============

*man hrtimer_init(9)*

*4.6.0-rc1*

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
