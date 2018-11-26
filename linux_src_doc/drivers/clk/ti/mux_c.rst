.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/mux.c

.. _`clk_mux_save_context`:

clk_mux_save_context
====================

.. c:function:: int clk_mux_save_context(struct clk_hw *hw)

    Save the parent selcted in the mux

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`clk_mux_save_context.description`:

Description
-----------

Save the parent mux value.

.. _`clk_mux_restore_context`:

clk_mux_restore_context
=======================

.. c:function:: void clk_mux_restore_context(struct clk_hw *hw)

    Restore the parent in the mux

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`clk_mux_restore_context.description`:

Description
-----------

Restore the saved parent mux value.

.. _`of_mux_clk_setup`:

of_mux_clk_setup
================

.. c:function:: void of_mux_clk_setup(struct device_node *node)

    Setup function for simple mux rate clock

    :param node:
        DT node for the clock
    :type node: struct device_node \*

.. _`of_mux_clk_setup.description`:

Description
-----------

Sets up a basic clock multiplexer.

.. This file was automatic generated / don't edit.

