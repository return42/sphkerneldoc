.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/qcom/pinctrl-ssbi-mpp.c

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
        u8 mode;
        bool input;
        bool output;
        bool high_z;
        bool paired;
        bool output_value;
        u8 power_source;
        u8 dtest;
        u8 amux;
        u8 aout_level;
        u8 drive_strength;
        unsigned pullup;
    }

.. _`pm8xxx_pin_data.members`:

Members
-------

reg
    address of the control register

irq
    IRQ from the PMIC interrupt controller

mode
    operating mode for the pin (digital, analog or current sink)

input
    pin is input

output
    pin is output

high_z
    pin is floating

paired
    mpp operates in paired mode

output_value
    logical output value of the mpp

power_source
    selected power source

dtest
    DTEST route selector

amux
    input muxing in analog mode

aout_level
    selector of the output in analog mode

drive_strength
    drive strength of the current sink

pullup
    pull up value, when in digital bidirectional mode

.. This file was automatic generated / don't edit.

