
.. _API-clk-set-parent:

==============
clk_set_parent
==============

*man clk_set_parent(9)*

*4.6.0-rc1*

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
