
.. _API-clk-set-rate-range:

==================
clk_set_rate_range
==================

*man clk_set_rate_range(9)*

*4.6.0-rc1*

set a rate range for a clock source


Synopsis
========

.. c:function:: int clk_set_rate_range( struct clk * clk, unsigned long min, unsigned long max )

Arguments
=========

``clk``
    clock source

``min``
    desired minimum clock rate in Hz, inclusive

``max``
    desired maximum clock rate in Hz, inclusive


Description
===========

Returns success (0) or negative errno.
