
.. _API-clk-set-min-rate:

================
clk_set_min_rate
================

*man clk_set_min_rate(9)*

*4.6.0-rc1*

set a minimum clock rate for a clock source


Synopsis
========

.. c:function:: int clk_set_min_rate( struct clk * clk, unsigned long rate )

Arguments
=========

``clk``
    clock source

``rate``
    desired minimum clock rate in Hz, inclusive


Description
===========

Returns success (0) or negative errno.
