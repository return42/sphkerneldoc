.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-get-parent:

==============
clk_get_parent
==============

*man clk_get_parent(9)*

*4.6.0-rc5*

get the parent clock source for this clock


Synopsis
========

.. c:function:: struct clk * clk_get_parent( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

Returns struct clk corresponding to parent clock source, or valid
``IS_ERR`` condition containing errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
