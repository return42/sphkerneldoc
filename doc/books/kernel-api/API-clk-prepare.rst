
.. _API-clk-prepare:

===========
clk_prepare
===========

*man clk_prepare(9)*

*4.6.0-rc1*

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
