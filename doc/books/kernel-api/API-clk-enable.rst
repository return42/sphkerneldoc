.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-enable:

==========
clk_enable
==========

*man clk_enable(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
