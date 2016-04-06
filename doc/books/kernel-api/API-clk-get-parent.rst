
.. _API-clk-get-parent:

==============
clk_get_parent
==============

*man clk_get_parent(9)*

*4.6.0-rc1*

get the parent clock source for this clock


Synopsis
========

.. c:function:: struct clk ⋆ clk_get_parent( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

Returns struct clk corresponding to parent clock source, or valid ``IS_ERR`` condition containing errno.
