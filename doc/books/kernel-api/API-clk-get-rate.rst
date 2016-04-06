
.. _API-clk-get-rate:

============
clk_get_rate
============

*man clk_get_rate(9)*

*4.6.0-rc1*

obtain the current clock rate (in Hz) for a clock source. This is only valid once the clock source has been enabled.


Synopsis
========

.. c:function:: unsigned long clk_get_rate( struct clk * clk )

Arguments
=========

``clk``
    clock source
