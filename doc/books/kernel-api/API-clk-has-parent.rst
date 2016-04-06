
.. _API-clk-has-parent:

==============
clk_has_parent
==============

*man clk_has_parent(9)*

*4.6.0-rc1*

check if a clock is a possible parent for another


Synopsis
========

.. c:function:: bool clk_has_parent( struct clk * clk, struct clk * parent )

Arguments
=========

``clk``
    clock source

``parent``
    parent clock source


Description
===========

This function can be used in drivers that need to check that a clock can be the parent of another without actually changing the parent.

Returns true if ``parent`` is a possible parent for ``clk``, false otherwise.
