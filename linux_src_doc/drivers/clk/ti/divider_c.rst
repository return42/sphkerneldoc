.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/divider.c

.. _`clk_divider_save_context`:

clk_divider_save_context
========================

.. c:function:: int clk_divider_save_context(struct clk_hw *hw)

    Save the divider value

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`clk_divider_save_context.description`:

Description
-----------

Save the divider value

.. _`clk_divider_restore_context`:

clk_divider_restore_context
===========================

.. c:function:: void clk_divider_restore_context(struct clk_hw *hw)

    restore the saved the divider value

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`clk_divider_restore_context.description`:

Description
-----------

Restore the saved the divider value

.. _`of_ti_divider_clk_setup`:

of_ti_divider_clk_setup
=======================

.. c:function:: void of_ti_divider_clk_setup(struct device_node *node)

    Setup function for simple div rate clock

    :param node:
        device node for this clock
    :type node: struct device_node \*

.. _`of_ti_divider_clk_setup.description`:

Description
-----------

Sets up a basic divider clock.

.. This file was automatic generated / don't edit.

