.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-set-rate-range:

==================
clk_set_rate_range
==================

*man clk_set_rate_range(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
