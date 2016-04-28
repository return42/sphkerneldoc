.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-set-max-rate:

================
clk_set_max_rate
================

*man clk_set_max_rate(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
