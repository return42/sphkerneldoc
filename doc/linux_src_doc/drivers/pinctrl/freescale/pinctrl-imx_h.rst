.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/freescale/pinctrl-imx.h

.. _`imx_pin`:

struct imx_pin
==============

.. c:type:: struct imx_pin

    describes a single i.MX pin

.. _`imx_pin.definition`:

Definition
----------

.. code-block:: c

    struct imx_pin {
        unsigned int pin;
        unsigned int mux_mode;
        u16 input_reg;
        unsigned int input_val;
        unsigned long config;
    }

.. _`imx_pin.members`:

Members
-------

pin
    the pin_id of this pin

mux_mode
    the mux mode for this pin.

input_reg
    the select input register offset for this pin if any
    0 if no select input setting needed.

input_val
    the select input value for this pin.

config
    *undescribed*

.. _`imx_pin_group`:

struct imx_pin_group
====================

.. c:type:: struct imx_pin_group

    describes an IMX pin group

.. _`imx_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct imx_pin_group {
        const char *name;
        unsigned npins;
        unsigned int *pin_ids;
        struct imx_pin *pins;
    }

.. _`imx_pin_group.members`:

Members
-------

name
    the name of this specific pin group

npins
    the number of pins in this group array, i.e. the number of
    elements in .pins so we can iterate over that array

pin_ids
    array of pin_ids. pinctrl forces us to maintain such an array

pins
    array of pins

.. _`imx_pmx_func`:

struct imx_pmx_func
===================

.. c:type:: struct imx_pmx_func

    describes IMX pinmux functions

.. _`imx_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct imx_pmx_func {
        const char *name;
        const char **groups;
        unsigned num_groups;
    }

.. _`imx_pmx_func.members`:

Members
-------

name
    the name of this specific function

groups
    corresponding pin groups

num_groups
    the number of groups

.. _`imx_pin_reg`:

struct imx_pin_reg
==================

.. c:type:: struct imx_pin_reg

    describe a pin reg map

.. _`imx_pin_reg.definition`:

Definition
----------

.. code-block:: c

    struct imx_pin_reg {
        s16 mux_reg;
        s16 conf_reg;
    }

.. _`imx_pin_reg.members`:

Members
-------

mux_reg
    mux register offset

conf_reg
    config register offset

.. This file was automatic generated / don't edit.

