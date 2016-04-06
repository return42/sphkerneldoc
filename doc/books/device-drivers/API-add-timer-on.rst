
.. _API-add-timer-on:

============
add_timer_on
============

*man add_timer_on(9)*

*4.6.0-rc1*

start a timer on a particular CPU


Synopsis
========

.. c:function:: void add_timer_on( struct timer_list * timer, int cpu )

Arguments
=========

``timer``
    the timer to be added

``cpu``
    the CPU to start it on


Description
===========

This is not very scalable on SMP. Double adds are not possible.
