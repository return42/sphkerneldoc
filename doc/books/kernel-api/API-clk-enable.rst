
.. _API-clk-enable:

==========
clk_enable
==========

*man clk_enable(9)*

*4.6.0-rc1*

inform the system when the clock source should be running.


Synopsis
========

.. c:function:: int clk_enable( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

If the clock can not be enabled/disabled, this should return success.

May be called from atomic contexts.

Returns success (0) or negative errno.
