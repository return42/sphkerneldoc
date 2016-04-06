
.. _API-clk-get-phase:

=============
clk_get_phase
=============

*man clk_get_phase(9)*

*4.6.0-rc1*

return the phase shift of a clock signal


Synopsis
========

.. c:function:: int clk_get_phase( struct clk * clk )

Arguments
=========

``clk``
    clock signal source


Description
===========

Returns the phase shift of a clock node in degrees, otherwise returns -EERROR.
