
.. _API-clk-disable:

===========
clk_disable
===========

*man clk_disable(9)*

*4.6.0-rc1*

inform the system when the clock source is no longer required.


Synopsis
========

.. c:function:: void clk_disable( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

Inform the system that a clock source is no longer required by a driver and may be shut down.

May be called from atomic contexts.


Implementation detail
=====================

if the clock source is shared between multiple drivers, ``clk_enable`` calls must be balanced by the same number of ``clk_disable`` calls for the clock source to be disabled.
