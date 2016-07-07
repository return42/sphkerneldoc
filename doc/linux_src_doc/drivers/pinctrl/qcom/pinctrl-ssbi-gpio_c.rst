.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/qcom/pinctrl-ssbi-gpio.c

.. _`pm8xxx_pin_data`:

struct pm8xxx_pin_data
======================

.. c:type:: struct pm8xxx_pin_data

    dynamic configuration for a pin

.. _`pm8xxx_pin_data.definition`:

Definition
----------

.. code-block:: c

    struct pm8xxx_pin_data {
        unsigned reg;
        int irq;
        u8 power_source;
        u8 mode;
        bool open_drain;
        bool output_value;
        u8 bias;
        u8 pull_up_strength;
        u8 output_strength;
        bool disable;
        u8 function;
        bool inverted;
    }

.. _`pm8xxx_pin_data.members`:

Members
-------

reg
    address of the control register

irq
    IRQ from the PMIC interrupt controller

power_source
    logical selected voltage source, mapping in static data
    is used translate to register values

mode
    operating mode for the pin (input/output)

open_drain
    output buffer configured as open-drain (vs push-pull)

output_value
    configured output value

bias
    register view of configured bias

pull_up_strength
    placeholder for selected pull up strength
    only used to configure bias when pull up is selected

output_strength
    selector of output-strength

disable
    pin disabled / configured as tristate

function
    pinmux selector

inverted
    pin logic is inverted

.. This file was automatic generated / don't edit.

