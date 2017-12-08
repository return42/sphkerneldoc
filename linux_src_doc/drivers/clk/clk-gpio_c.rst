.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-gpio.c

.. _`basic-gpio-gated-clock-which-can-be-enabled-and-disabled`:

basic gpio gated clock which can be enabled and disabled
========================================================

with gpio output
Traits of this clock:
prepare - clk_(un)prepare only ensures parent is (un)prepared
enable - clk_enable and clk_disable are functional & control gpio
rate - inherits rate from parent.  No clk_set_rate support
parent - fixed parent.  No clk_set_parent support

.. _`basic-clock-multiplexer-which-can-be-controlled-with-a-gpio-output`:

basic clock multiplexer which can be controlled with a gpio output
==================================================================

Traits of this clock:
prepare - clk_prepare only ensures that parents are prepared
rate - rate is only affected by parent switching.  No clk_set_rate support
parent - parent is adjustable through clk_set_parent

.. _`clk_hw_register_gpio_gate`:

clk_hw_register_gpio_gate
=========================

.. c:function:: struct clk_hw *clk_hw_register_gpio_gate(struct device *dev, const char *name, const char *parent_name, struct gpio_desc *gpiod, unsigned long flags)

    register a gpio clock gate with the clock framework

    :param struct device \*dev:
        device that is registering this clock

    :param const char \*name:
        name of this clock

    :param const char \*parent_name:
        name of this clock's parent

    :param struct gpio_desc \*gpiod:
        gpio descriptor to gate this clock

    :param unsigned long flags:
        clock flags

.. _`clk_hw_register_gpio_mux`:

clk_hw_register_gpio_mux
========================

.. c:function:: struct clk_hw *clk_hw_register_gpio_mux(struct device *dev, const char *name, const char * const *parent_names, u8 num_parents, struct gpio_desc *gpiod, unsigned long flags)

    register a gpio clock mux with the clock framework

    :param struct device \*dev:
        device that is registering this clock

    :param const char \*name:
        name of this clock

    :param const char \* const \*parent_names:
        names of this clock's parents

    :param u8 num_parents:
        number of parents listed in \ ``parent_names``\ 

    :param struct gpio_desc \*gpiod:
        gpio descriptor to gate this clock

    :param unsigned long flags:
        clock flags

.. This file was automatic generated / don't edit.

