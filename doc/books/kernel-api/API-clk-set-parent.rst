.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-set-parent:

==============
clk_set_parent
==============

*man clk_set_parent(9)*

*4.6.0-rc5*

set the parent clock source for this clock


Synopsis
========

.. c:function:: int clk_set_parent( struct clk * clk, struct clk * parent )

Arguments
=========

``clk``
    clock source

``parent``
    parent clock source


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
