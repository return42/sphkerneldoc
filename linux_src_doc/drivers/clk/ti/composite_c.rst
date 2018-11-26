.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/composite.c

.. _`ti_clk_add_component`:

ti_clk_add_component
====================

.. c:function:: int ti_clk_add_component(struct device_node *node, struct clk_hw *hw, int type)

    add a component clock to the pool

    :param node:
        device node of the component clock
    :type node: struct device_node \*

    :param hw:
        hardware clock definition for the component clock
    :type hw: struct clk_hw \*

    :param type:
        type of the component clock
    :type type: int

.. _`ti_clk_add_component.description`:

Description
-----------

Adds a component clock to the list of available components, so that
it can be registered by a composite clock.

.. This file was automatic generated / don't edit.

