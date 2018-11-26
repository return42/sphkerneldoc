.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/dpll.c

.. _`_register_dpll`:

\_register_dpll
===============

.. c:function:: void _register_dpll(void *user, struct device_node *node)

    low level registration of a DPLL clock

    :param user:
        *undescribed*
    :type user: void \*

    :param node:
        device node for the clock
    :type node: struct device_node \*

.. _`_register_dpll.description`:

Description
-----------

Finalizes DPLL registration process. In case a failure (clk-ref or
clk-bypass is missing), the clock is added to retry list and
the initialization is retried on later stage.

.. _`_register_dpll_x2`:

\_register_dpll_x2
==================

.. c:function:: void _register_dpll_x2(struct device_node *node, const struct clk_ops *ops, const struct clk_hw_omap_ops *hw_ops)

    Registers a DPLLx2 clock

    :param node:
        device node for this clock
    :type node: struct device_node \*

    :param ops:
        clk_ops for this clock
    :type ops: const struct clk_ops \*

    :param hw_ops:
        clk_hw_ops for this clock
    :type hw_ops: const struct clk_hw_omap_ops \*

.. _`_register_dpll_x2.description`:

Description
-----------

Initializes a DPLL x 2 clock from device tree data.

.. _`of_ti_dpll_setup`:

of_ti_dpll_setup
================

.. c:function:: void of_ti_dpll_setup(struct device_node *node, const struct clk_ops *ops, const struct dpll_data *ddt)

    Setup function for OMAP DPLL clocks

    :param node:
        device node containing the DPLL info
    :type node: struct device_node \*

    :param ops:
        ops for the DPLL
    :type ops: const struct clk_ops \*

    :param ddt:
        DPLL data template to use
    :type ddt: const struct dpll_data \*

.. _`of_ti_dpll_setup.description`:

Description
-----------

Initializes a DPLL clock from device tree data.

.. This file was automatic generated / don't edit.

