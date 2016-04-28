.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-unprepare:

=============
clk_unprepare
=============

*man clk_unprepare(9)*

*4.6.0-rc5*

undo preparation of a clock source


Synopsis
========

.. c:function:: void clk_unprepare( struct clk * clk )

Arguments
=========

``clk``
    clock source


Description
===========

This undoes a previously prepared clock. The caller must balance the
number of prepare and unprepare calls.

Must not be called from within atomic context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
