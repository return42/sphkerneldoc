
.. _API-clk-set-rate:

============
clk_set_rate
============

*man clk_set_rate(9)*

*4.6.0-rc1*

set the clock rate for a clock source


Synopsis
========

.. c:function:: int clk_set_rate( struct clk * clk, unsigned long rate )

Arguments
=========

``clk``
    clock source

``rate``
    desired clock rate in Hz


Description
===========

Returns success (0) or negative errno.
