.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-prepare:

===========
clk_prepare
===========

*man clk_prepare(9)*

*4.6.0-rc5*

prepare a clock source


Synopsis
========

.. c:function:: int clk_prepare( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

This prepares the clock source for use.

Must not be called from within atomic context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
