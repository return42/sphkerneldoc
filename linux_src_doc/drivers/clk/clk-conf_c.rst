.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-conf.c

.. _`of_clk_set_defaults`:

of_clk_set_defaults
===================

.. c:function:: int of_clk_set_defaults(struct device_node *node, bool clk_supplier)

    parse and set assigned clocks configuration

    :param struct device_node \*node:
        device node to apply clock settings for

    :param bool clk_supplier:
        true if clocks supplied by \ ``node``\  should also be considered

.. _`of_clk_set_defaults.description`:

Description
-----------

This function parses 'assigned-{clocks/clock-parents/clock-rates}' properties
and sets any specified clock parents and rates. The \ ``clk_supplier``\  argument
should be set to true if \ ``node``\  may be also a clock supplier of any clock
listed in its 'assigned-clocks' or 'assigned-clock-parents' properties.
If \ ``clk_supplier``\  is false the function exits returning 0 as soon as it
determines the \ ``node``\  is also a supplier of any of the clocks.

.. This file was automatic generated / don't edit.

