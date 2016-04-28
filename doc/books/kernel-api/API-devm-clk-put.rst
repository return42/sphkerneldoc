.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-clk-put:

============
devm_clk_put
============

*man devm_clk_put(9)*

*4.6.0-rc5*

"free" a managed clock source


Synopsis
========

.. c:function:: void devm_clk_put( struct device * dev, struct clk * clk )

Arguments
=========

``dev``
    device used to acquire the clock

``clk``
    clock source acquired with ``devm_clk_get``


Note
====

drivers must ensure that all clk_enable calls made on this clock source
are balanced by clk_disable calls prior to calling this function.

clk_put should not be called from within interrupt context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
