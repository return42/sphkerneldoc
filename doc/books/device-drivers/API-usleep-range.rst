
.. _API-usleep-range:

============
usleep_range
============

*man usleep_range(9)*

*4.6.0-rc1*

Drop in replacement for udelay where wakeup is flexible


Synopsis
========

.. c:function:: void __sched usleep_range( unsigned long min, unsigned long max )

Arguments
=========

``min``
    Minimum time in usecs to sleep

``max``
    Maximum time in usecs to sleep
