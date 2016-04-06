
.. _API-clk-set-phase:

=============
clk_set_phase
=============

*man clk_set_phase(9)*

*4.6.0-rc1*

adjust the phase shift of a clock signal


Synopsis
========

.. c:function:: int clk_set_phase( struct clk * clk, int degrees )

Arguments
=========

``clk``
    clock signal source

``degrees``
    number of degrees the signal is shifted


Description
===========

Shifts the phase of a clock signal by the specified degrees. Returns 0 on success, -EERROR otherwise.
