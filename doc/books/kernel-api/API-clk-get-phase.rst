.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-get-phase:

=============
clk_get_phase
=============

*man clk_get_phase(9)*

*4.6.0-rc5*

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

Returns the phase shift of a clock node in degrees, otherwise returns
-EERROR.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
