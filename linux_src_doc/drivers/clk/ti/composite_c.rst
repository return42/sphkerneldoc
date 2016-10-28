.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/composite.c

.. _`ti_clk_add_component`:

ti_clk_add_component
====================

.. c:function:: int ti_clk_add_component(struct device_node *node, struct clk_hw *hw, int type)

    add a component clock to the pool

    :param struct device_node \*node:
        device node of the component clock

    :param struct clk_hw \*hw:
        hardware clock definition for the component clock

    :param int type:
        type of the component clock

.. _`ti_clk_add_component.description`:

Description
-----------

Adds a component clock to the list of available components, so that
it can be registered by a composite clock.

.. This file was automatic generated / don't edit.

