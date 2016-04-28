.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-get-accuracy:

================
clk_get_accuracy
================

*man clk_get_accuracy(9)*

*4.6.0-rc5*

obtain the clock accuracy in ppb (parts per billion) for a clock source.


Synopsis
========

.. c:function:: long clk_get_accuracy( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

This gets the clock source accuracy expressed in ppb. A perfect clock
returns 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
