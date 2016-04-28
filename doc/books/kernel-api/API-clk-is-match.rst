.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-is-match:

============
clk_is_match
============

*man clk_is_match(9)*

*4.6.0-rc5*

check if two clk's point to the same hardware clock


Synopsis
========

.. c:function:: bool clk_is_match( const struct clk * p, const struct clk * q )

Arguments
=========

``p``
    clk compared against q

``q``
    clk compared against p


Description
===========

Returns true if the two struct clk pointers both point to the same
hardware clock node. Put differently, returns true if struct clk *p and
struct clk *q share the same struct clk_core object.

Returns false otherwise. Note that two NULL clks are treated as
matching.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
