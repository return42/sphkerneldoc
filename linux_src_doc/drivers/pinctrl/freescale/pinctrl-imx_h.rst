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

