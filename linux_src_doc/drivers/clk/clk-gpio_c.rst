.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-gpio.c

.. _`clk_hw_register_gpio_gate`:

clk_hw_register_gpio_gate
=========================

.. c:function:: struct clk_hw *clk_hw_register_gpio_gate(struct device *dev, const char *name, const char *parent_name, unsigned gpio, bool active_low, unsigned long flags)

    register a gpio clock gate with the clock framework

    :param struct device \*dev:
        device that is registering this clock

    :param const char \*name:
        name of this clock

    :param const char \*parent_name:
        name of this clock's parent

    :param unsigned gpio:
        gpio number to gate this clock

    :param bool active_low:
        true if gpio should be set to 0 to enable clock

    :param unsigned long flags:
        clock flags

.. _`clk_hw_register_gpio_mux`:

clk_hw_register_gpio_mux
========================

.. c:function:: struct clk_hw *clk_hw_register_gpio_mux(struct device *dev, const char *name, const char * const *parent_names, u8 num_parents, unsigned gpio, bool active_low, unsigned long flags)

    register a gpio clock mux with the clock framework

    :param struct device \*dev:
        device that is registering this clock

    :param const char \*name:
        name of this clock

    :param const char \* const \*parent_names:
        names of this clock's parents

    :param u8 num_parents:
        number of parents listed in \ ``parent_names``\ 

    :param unsigned gpio:
        gpio number to gate this clock

    :param bool active_low:
        true if gpio should be set to 0 to enable clock

    :param unsigned long flags:
        clock flags

.. This file was automatic generated / don't edit.

