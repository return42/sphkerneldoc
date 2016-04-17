.. -*- coding: utf-8; mode: rst -*-

==========
clk-gpio.c
==========


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



.. _`clk_register_gpio_gate`:

clk_register_gpio_gate
======================

.. c:function:: struct clk *clk_register_gpio_gate (struct device *dev, const char *name, const char *parent_name, unsigned gpio, bool active_low, unsigned long flags)

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



.. _`clk_register_gpio_mux`:

clk_register_gpio_mux
=====================

.. c:function:: struct clk *clk_register_gpio_mux (struct device *dev, const char *name, const char *const *parent_names, u8 num_parents, unsigned gpio, bool active_low, unsigned long flags)

    register a gpio clock mux with the clock framework

    :param struct device \*dev:
        device that is registering this clock

    :param const char \*name:
        name of this clock

    :param const \*parent_names:
        names of this clock's parents

    :param u8 num_parents:
        number of parents listed in ``parent_names``

    :param unsigned gpio:
        gpio number to gate this clock

    :param bool active_low:
        true if gpio should be set to 0 to enable clock

    :param unsigned long flags:
        clock flags

