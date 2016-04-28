.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-set-rate:

============
clk_set_rate
============

*man clk_set_rate(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
