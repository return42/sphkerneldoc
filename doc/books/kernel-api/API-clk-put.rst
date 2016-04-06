
.. _API-clk-put:

=======
clk_put
=======

*man clk_put(9)*

*4.6.0-rc1*

"free" the clock source


Synopsis
========

.. c:function:: void clk_put( struct clk * clk )

Arguments
=========

``clk``
    clock source


Note
====

drivers must ensure that all clk_enable calls made on this clock source are balanced by clk_disable calls prior to calling this function.

clk_put should not be called from within interrupt context.
