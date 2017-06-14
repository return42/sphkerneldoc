.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/imx/clk-gate2.c

.. _`basic-gatable-clock-which-can-gate-and-ungate-it-s-ouput`:

basic gatable clock which can gate and ungate it's ouput
========================================================

Traits of this clock:
prepare - clk_(un)prepare only ensures parent is (un)prepared
enable - clk_enable and clk_disable are functional & control gating
rate - inherits rate from parent.  No clk_set_rate support
parent - fixed parent.  No clk_set_parent support

.. This file was automatic generated / don't edit.

