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

    :param dev:
        device that is registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of this clock's parent
    :type parent_name: const char \*

    :param gpiod:
        gpio descriptor to gate this clock
    :type gpiod: struct gpio_desc \*

    :param flags:
        clock flags
    :type flags: unsigned long

.. _`clk_hw_register_gpio_mux`:

clk_hw_register_gpio_mux
========================

.. c:function:: struct clk_hw *clk_hw_register_gpio_mux(struct device *dev, const char *name, const char * const *parent_names, u8 num_parents, struct gpio_desc *gpiod, unsigned long flags)

    register a gpio clock mux with the clock framework

    :param dev:
        device that is registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_names:
        names of this clock's parents
    :type parent_names: const char \* const \*

    :param num_parents:
        number of parents listed in \ ``parent_names``\ 
    :type num_parents: u8

    :param gpiod:
        gpio descriptor to gate this clock
    :type gpiod: struct gpio_desc \*

    :param flags:
        clock flags
    :type flags: unsigned long

.. This file was automatic generated / don't edit.

