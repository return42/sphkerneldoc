.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-zynq.c

.. _`zynq_pinctrl`:

struct zynq_pinctrl
===================

.. c:type:: struct zynq_pinctrl

    driver data

.. _`zynq_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct zynq_pinctrl {
        struct pinctrl_dev *pctrl;
        struct regmap *syscon;
        u32 pctrl_offset;
        const struct zynq_pctrl_group *groups;
        unsigned int ngroups;
        const struct zynq_pinmux_function *funcs;
        unsigned int nfuncs;
    }

.. _`zynq_pinctrl.members`:

Members
-------

pctrl
    Pinctrl device

syscon
    Syscon regmap

pctrl_offset
    Offset for pinctrl into the \ ``syscon``\  space

groups
    Pingroups

ngroups
    *undescribed*

funcs
    Pinmux functions

nfuncs
    Number of \ ``funcs``\ 

.. _`zynq_pinmux_function`:

struct zynq_pinmux_function
===========================

.. c:type:: struct zynq_pinmux_function

    a pinmux function

.. _`zynq_pinmux_function.definition`:

Definition
----------

.. code-block:: c

    struct zynq_pinmux_function {
        const char *name;
        const char * const *groups;
        unsigned int ngroups;
        unsigned int mux_val;
        u32 mux;
        u32 mux_mask;
        u8 mux_shift;
    }

.. _`zynq_pinmux_function.members`:

Members
-------

name
    Name of the pinmux function.

groups
    List of pingroups for this function.

ngroups
    Number of entries in \ ``groups``\ .

mux_val
    Selector for this function

mux
    Offset of function specific mux

mux_mask
    Mask for function specific selector

mux_shift
    Shift for function specific selector

.. _`zynq_pin_config_param`:

enum zynq_pin_config_param
==========================

.. c:type:: enum zynq_pin_config_param

    possible pin configuration parameters

.. _`zynq_pin_config_param.definition`:

Definition
----------

.. code-block:: c

    enum zynq_pin_config_param {
        PIN_CONFIG_IOSTANDARD
    };

.. _`zynq_pin_config_param.constants`:

Constants
---------

PIN_CONFIG_IOSTANDARD
    if the pin can select an IO standard, the argument to
    this parameter (on a custom format) tells the driver which alternative
    IO standard to use.

.. This file was automatic generated / don't edit.

