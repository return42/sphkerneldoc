.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-round-rate:

==============
clk_round_rate
==============

*man clk_round_rate(9)*

*4.6.0-rc5*

adjust a rate to the exact rate a clock can provide


Synopsis
========

.. c:function:: long clk_round_rate( struct clk * clk, unsigned long rate )

Arguments
=========

``clk``
    clock source

``rate``
    desired clock rate in Hz


Description
===========

This answers the question “if I were to pass ``rate`` to
``clk_set_rate``, what clock rate would I end up with?” without changing
the hardware in any way. In other words:

rate = clk_round_rate(clk, r);


and
===

clk_set_rate(clk, r); rate = clk_get_rate(clk);

are equivalent except the former does not modify the clock hardware in
any way.

Returns rounded clock rate in Hz, or negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
