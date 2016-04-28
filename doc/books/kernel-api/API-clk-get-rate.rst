.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-get-rate:

============
clk_get_rate
============

*man clk_get_rate(9)*

*4.6.0-rc5*

obtain the current clock rate (in Hz) for a clock source. This is only
valid once the clock source has been enabled.


Synopsis
========

.. c:function:: unsigned long clk_get_rate( struct clk * clk )

Arguments
=========

``clk``
    clock source


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
