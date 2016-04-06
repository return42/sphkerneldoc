
.. _API-clk-set-max-rate:

================
clk_set_max_rate
================

*man clk_set_max_rate(9)*

*4.6.0-rc1*

set a maximum clock rate for a clock source


Synopsis
========

.. c:function:: int clk_set_max_rate( struct clk * clk, unsigned long rate )

Arguments
=========

``clk``
    clock source

``rate``
    desired maximum clock rate in Hz, inclusive


Description
===========

Returns success (0) or negative errno.
