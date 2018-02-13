.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/dpll.c

.. _`_register_dpll`:

_register_dpll
==============

.. c:function:: void _register_dpll(void *user, struct device_node *node)

    low level registration of a DPLL clock

    :param void \*user:
        *undescribed*

    :param struct device_node \*node:
        device node for the clock

.. _`_register_dpll.description`:

Description
-----------

Finalizes DPLL registration process. In case a failure (clk-ref or
clk-bypass is missing), the clock is added to retry list and
the initialization is retried on later stage.

.. _`_register_dpll_x2`:

_register_dpll_x2
=================

.. c:function:: void _register_dpll_x2(struct device_node *node, const struct clk_ops *ops, const struct clk_hw_omap_ops *hw_ops)

    Registers a DPLLx2 clock

    :param struct device_node \*node:
        device node for this clock

    :param const struct clk_ops \*ops:
        clk_ops for this clock

    :param const struct clk_hw_omap_ops \*hw_ops:
        clk_hw_ops for this clock

.. _`_register_dpll_x2.description`:

Description
-----------

Initializes a DPLL x 2 clock from device tree data.

.. _`of_ti_dpll_setup`:

of_ti_dpll_setup
================

.. c:function:: void of_ti_dpll_setup(struct device_node *node, const struct clk_ops *ops, const struct dpll_data *ddt)

    Setup function for OMAP DPLL clocks

    :param struct device_node \*node:
        device node containing the DPLL info

    :param const struct clk_ops \*ops:
        ops for the DPLL

    :param const struct dpll_data \*ddt:
        DPLL data template to use

.. _`of_ti_dpll_setup.description`:

Description
-----------

Initializes a DPLL clock from device tree data.

.. This file was automatic generated / don't edit.

