.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-rza1.c

.. _`rza1_pinmux_get_flags`:

rza1_pinmux_get_flags
=====================

.. c:function:: unsigned int rza1_pinmux_get_flags(unsigned int port, unsigned int pin, unsigned int func, struct rza1_pinctrl *rza1_pctl)

    return pinmux flags associated to a pin

    :param port:
        *undescribed*
    :type port: unsigned int

    :param pin:
        *undescribed*
    :type pin: unsigned int

    :param func:
        *undescribed*
    :type func: unsigned int

    :param rza1_pctl:
        *undescribed*
    :type rza1_pctl: struct rza1_pinctrl \*

.. _`rza1_set_bit`:

rza1_set_bit
============

.. c:function:: void rza1_set_bit(struct rza1_port *port, unsigned int reg, unsigned int bit, bool set)

    un-locked set/clear a single bit in pin configuration registers

    :param port:
        *undescribed*
    :type port: struct rza1_port \*

    :param reg:
        *undescribed*
    :type reg: unsigned int

    :param bit:
        *undescribed*
    :type bit: unsigned int

    :param set:
        *undescribed*
    :type set: bool

.. _`rza1_pin_reset`:

rza1_pin_reset
==============

.. c:function:: void rza1_pin_reset(struct rza1_port *port, unsigned int pin)

    reset a pin to default initial state

    :param port:
        port where pin sits on
    :type port: struct rza1_port \*

    :param pin:
        pin offset
    :type pin: unsigned int

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

    :param port:
        port where pin sits on
    :type port: struct rza1_port \*

    :param pin:
        pin offset
    :type pin: unsigned int

    :param input:
        input enable/disable flag
    :type input: bool

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

    :param rza1_pctl:
        *undescribed*
    :type rza1_pctl: struct rza1_pinctrl \*

    :param mux_conf:
        pin multiplexing descriptor
    :type mux_conf: struct rza1_mux_conf \*

.. _`rza1_gpio_request`:

rza1_gpio_request
=================

.. c:function:: int rza1_gpio_request(struct gpio_chip *chip, unsigned int gpio)

    configure pin in port mode

    :param chip:
        gpio chip where the gpio sits on
    :type chip: struct gpio_chip \*

    :param gpio:
        gpio offset
    :type gpio: unsigned int

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

    :param chip:
        gpio chip where the gpio sits on
    :type chip: struct gpio_chip \*

    :param gpio:
        gpio offset
    :type gpio: unsigned int

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

    :param chip:
        gpio chip where the gpio sits on
    :type chip: struct gpio_chip \*

    :param gpio:
        gpio offset
    :type gpio: unsigned int

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

    :param np:
        device tree node to parse
    :type np: struct device_node \*

.. _`rza1_parse_pinmux_node`:

rza1_parse_pinmux_node
======================

.. c:function:: int rza1_parse_pinmux_node(struct rza1_pinctrl *rza1_pctl, struct device_node *np, struct rza1_mux_conf *mux_confs, unsigned int *grpins)

    parse a pin mux sub-node

    :param rza1_pctl:
        RZ/A1 pin controller device
    :type rza1_pctl: struct rza1_pinctrl \*

    :param np:
        of pmx sub-node
    :type np: struct device_node \*

    :param mux_confs:
        array of pin mux configurations to fill with parsed info
    :type mux_confs: struct rza1_mux_conf \*

    :param grpins:
        array of pin ids to mux
    :type grpins: unsigned int \*

.. _`rza1_dt_node_to_map`:

rza1_dt_node_to_map
===================

.. c:function:: int rza1_dt_node_to_map(struct pinctrl_dev *pctldev, struct device_node *np, struct pinctrl_map **map, unsigned int *num_maps)

    map a pin mux node to a function/group

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param np:
        device tree node to parse
    :type np: struct device_node \*

    :param map:
        pointer to pin map (output)
    :type map: struct pinctrl_map \*\*

    :param num_maps:
        number of collected maps (output)
    :type num_maps: unsigned int \*

.. _`rza1_dt_node_to_map.description`:

Description
-----------

Parse and register a pin mux function.

.. _`rza1_set_mux`:

rza1_set_mux
============

.. c:function:: int rza1_set_mux(struct pinctrl_dev *pctldev, unsigned int selector, unsigned int group)

    retrieve pins from a group and apply their mux settings

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        function selector
    :type selector: unsigned int

    :param group:
        group selector
    :type group: unsigned int

.. _`rza1_parse_gpiochip`:

rza1_parse_gpiochip
===================

.. c:function:: int rza1_parse_gpiochip(struct rza1_pinctrl *rza1_pctl, struct device_node *np, struct gpio_chip *chip, struct pinctrl_gpio_range *range)

    parse and register a gpio chip and pin range

    :param rza1_pctl:
        RZ/A1 pin controller device
    :type rza1_pctl: struct rza1_pinctrl \*

    :param np:
        of gpio-controller node
    :type np: struct device_node \*

    :param chip:
        gpio chip to register to gpiolib
    :type chip: struct gpio_chip \*

    :param range:
        pin range to register to pinctrl core
    :type range: struct pinctrl_gpio_range \*

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

    :param rza1_pctl:
        RZ/A1 pin controller device
    :type rza1_pctl: struct rza1_pinctrl \*

.. _`rza1_pinctrl_register`:

rza1_pinctrl_register
=====================

.. c:function:: int rza1_pinctrl_register(struct rza1_pinctrl *rza1_pctl)

    Enumerate pins, ports and gpiochips; register them to pinctrl and gpio cores.

    :param rza1_pctl:
        RZ/A1 pin controller device
    :type rza1_pctl: struct rza1_pinctrl \*

.. This file was automatic generated / don't edit.

