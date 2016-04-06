
.. _API-clk-unprepare:

=============
clk_unprepare
=============

*man clk_unprepare(9)*

*4.6.0-rc1*

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

This undoes a previously prepared clock. The caller must balance the number of prepare and unprepare calls.

Must not be called from within atomic context.
