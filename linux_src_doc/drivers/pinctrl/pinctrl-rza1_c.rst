.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-rza1.c

.. _`rza1_pinmux_get_flags`:

rza1_pinmux_get_flags
=====================

.. c:function:: unsigned int rza1_pinmux_get_flags(unsigned int port, unsigned int pin, unsigned int func, struct rza1_pinctrl *rza1_pctl)

    return pinmux flags associated to a pin

    :param unsigned int port:
        *undescribed*

    :param unsigned int pin:
        *undescribed*

    :param unsigned int func:
        *undescribed*

    :param struct rza1_pinctrl \*rza1_pctl:
        *undescribed*

.. _`rza1_set_bit`:

rza1_set_bit
============

.. c:function:: void rza1_set_bit(struct rza1_port *port, unsigned int reg, unsigned int bit, bool set)

    un-locked set/clear a single bit in pin configuration registers

    :param struct rza1_port \*port:
        *undescribed*

    :param unsigned int reg:
        *undescribed*

    :param unsigned int bit:
        *undescribed*

    :param bool set:
        *undescribed*

.. _`rza1_pin_reset`:

rza1_pin_reset
==============

.. c:function:: void rza1_pin_reset(struct rza1_port *port, unsigned int pin)

    reset a pin to default initial state

    :param struct rza1_port \*port:
        port where pin sits on

    :param unsigned int pin:
        pin offset

.. _`rza1_pin_reset.description`:

Description
-----------

Reset pin state disabling input buffer and bi-directional control,
and configure it as input port.
Note that pin is now configured with direction as input but with input
buffer disabled. This implies the pin value cannot be read in this state.

.. _`rza1_pin_set_direction`:

rza1_pin_set_direction
======================

.. c:function:: void rza1_pin_set_direction(struct rza1_port *port, unsigned int pin, bool input)

    set I/O direction on a pin in port mode

    :param struct rza1_port \*port:
        port where pin sits on

    :param unsigned int pin:
        pin offset

    :param bool input:
        input enable/disable flag

.. _`rza1_pin_set_direction.description`:

Description
-----------

When running in output port mode keep PBDC enabled to allow reading the
pin value from PPR.

.. _`rza1_pin_mux_single`:

rza1_pin_mux_single
===================

.. c:function:: int rza1_pin_mux_single(struct rza1_pinctrl *rza1_pctl, struct rza1_mux_conf *mux_conf)

    configure pin multiplexing on a single pin

    :param struct rza1_pinctrl \*rza1_pctl:
        *undescribed*

    :param struct rza1_mux_conf \*mux_conf:
        pin multiplexing descriptor

.. _`rza1_gpio_request`:

rza1_gpio_request
=================

.. c:function:: int rza1_gpio_request(struct gpio_chip *chip, unsigned int gpio)

    configure pin in port mode

    :param struct gpio_chip \*chip:
        gpio chip where the gpio sits on

    :param unsigned int gpio:
        gpio offset

.. _`rza1_gpio_request.description`:

Description
-----------

Configure a pin as gpio (port mode).
After reset, the pin is in input mode with input buffer disabled.
To use the pin as input or output, set_direction shall be called first

.. _`rza1_gpio_free`:

rza1_gpio_free
==============

.. c:function:: void rza1_gpio_free(struct gpio_chip *chip, unsigned int gpio)

    reset a pin

    :param struct gpio_chip \*chip:
        gpio chip where the gpio sits on

    :param unsigned int gpio:
        gpio offset

.. _`rza1_gpio_free.description`:

Description
-----------

Surprisingly, disable_free a gpio, is equivalent to request it.
Reset pin to port mode, with input buffer disabled. This overwrites all
port direction settings applied with set_direction

.. _`rza1_gpio_get`:

rza1_gpio_get
=============

.. c:function:: int rza1_gpio_get(struct gpio_chip *chip, unsigned int gpio)

    read a gpio pin value

    :param struct gpio_chip \*chip:
        gpio chip where the gpio sits on

    :param unsigned int gpio:
        gpio offset

.. _`rza1_gpio_get.description`:

Description
-----------

Read gpio pin value through PPR register.
Requires bi-directional mode to work when reading the value of a pin
in output mode

.. _`rza1_dt_node_pin_count`:

rza1_dt_node_pin_count
======================

.. c:function:: int rza1_dt_node_pin_count(struct device_node *np)

    Count number of pins in a dt node or in all its children sub-nodes

    :param struct device_node \*np:
        device tree node to parse

.. _`rza1_parse_pinmux_node`:

rza1_parse_pinmux_node
======================

.. c:function:: int rza1_parse_pinmux_node(struct rza1_pinctrl *rza1_pctl, struct device_node *np, struct rza1_mux_conf *mux_confs, unsigned int *grpins)

    parse a pin mux sub-node

    :param struct rza1_pinctrl \*rza1_pctl:
        RZ/A1 pin controller device

    :param struct device_node \*np:
        of pmx sub-node

    :param struct rza1_mux_conf \*mux_confs:
        array of pin mux configurations to fill with parsed info

    :param unsigned int \*grpins:
        array of pin ids to mux

.. _`rza1_dt_node_to_map`:

rza1_dt_node_to_map
===================

.. c:function:: int rza1_dt_node_to_map(struct pinctrl_dev *pctldev, struct device_node *np, struct pinctrl_map **map, unsigned int *num_maps)

    map a pin mux node to a function/group

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param struct device_node \*np:
        device tree node to parse

    :param struct pinctrl_map \*\*map:
        pointer to pin map (output)

    :param unsigned int \*num_maps:
        number of collected maps (output)

.. _`rza1_dt_node_to_map.description`:

Description
-----------

Parse and register a pin mux function.

.. _`rza1_set_mux`:

rza1_set_mux
============

.. c:function:: int rza1_set_mux(struct pinctrl_dev *pctldev, unsigned int selector, unsigned int group)

    retrieve pins from a group and apply their mux settings

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param unsigned int selector:
        function selector

    :param unsigned int group:
        group selector

.. _`rza1_parse_gpiochip`:

rza1_parse_gpiochip
===================

.. c:function:: int rza1_parse_gpiochip(struct rza1_pinctrl *rza1_pctl, struct device_node *np, struct gpio_chip *chip, struct pinctrl_gpio_range *range)

    parse and register a gpio chip and pin range

    :param struct rza1_pinctrl \*rza1_pctl:
        RZ/A1 pin controller device

    :param struct device_node \*np:
        of gpio-controller node

    :param struct gpio_chip \*chip:
        gpio chip to register to gpiolib

    :param struct pinctrl_gpio_range \*range:
        pin range to register to pinctrl core

.. _`rza1_parse_gpiochip.description`:

Description
-----------

The gpio controller subnode shall provide a "gpio-ranges" list property as
defined by gpio device tree binding documentation.

.. _`rza1_gpio_register`:

rza1_gpio_register
==================

.. c:function:: int rza1_gpio_register(struct rza1_pinctrl *rza1_pctl)

    parse DT to collect gpio-chips and gpio-ranges

    :param struct rza1_pinctrl \*rza1_pctl:
        RZ/A1 pin controller device

.. _`rza1_pinctrl_register`:

rza1_pinctrl_register
=====================

.. c:function:: int rza1_pinctrl_register(struct rza1_pinctrl *rza1_pctl)

    Enumerate pins, ports and gpiochips; register them to pinctrl and gpio cores.

    :param struct rza1_pinctrl \*rza1_pctl:
        RZ/A1 pin controller device

.. This file was automatic generated / don't edit.

