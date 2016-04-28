.. -*- coding: utf-8; mode: rst -*-

.. _API-add-timer-on:

============
add_timer_on
============

*man add_timer_on(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
