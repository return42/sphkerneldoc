.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-fixed-rate.c

.. _`clk_hw_register_fixed_rate_with_accuracy`:

clk_hw_register_fixed_rate_with_accuracy
========================================

.. c:function:: struct clk_hw *clk_hw_register_fixed_rate_with_accuracy(struct device *dev, const char *name, const char *parent_name, unsigned long flags, unsigned long fixed_rate, unsigned long fixed_accuracy)

    register fixed-rate clock with the clock framework

    :param dev:
        device that is registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param flags:
        framework-specific flags
    :type flags: unsigned long

    :param fixed_rate:
        non-adjustable clock rate
    :type fixed_rate: unsigned long

    :param fixed_accuracy:
        non-adjustable clock rate
    :type fixed_accuracy: unsigned long

.. _`clk_hw_register_fixed_rate`:

clk_hw_register_fixed_rate
==========================

.. c:function:: struct clk_hw *clk_hw_register_fixed_rate(struct device *dev, const char *name, const char *parent_name, unsigned long flags, unsigned long fixed_rate)

    register fixed-rate clock with the clock framework

    :param dev:
        device that is registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param flags:
        framework-specific flags
    :type flags: unsigned long

    :param fixed_rate:
        non-adjustable clock rate
    :type fixed_rate: unsigned long

.. _`of_fixed_clk_setup`:

of_fixed_clk_setup
==================

.. c:function:: void of_fixed_clk_setup(struct device_node *node)

    Setup function for simple fixed rate clock

    :param node:
        *undescribed*
    :type node: struct device_node \*

.. This file was automatic generated / don't edit.

