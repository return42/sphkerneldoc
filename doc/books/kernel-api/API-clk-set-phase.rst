.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-set-phase:

=============
clk_set_phase
=============

*man clk_set_phase(9)*

*4.6.0-rc5*

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

Shifts the phase of a clock signal by the specified degrees. Returns 0
on success, -EERROR otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
