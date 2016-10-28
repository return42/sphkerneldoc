.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/qcom/pinctrl-spmi-mpp.c

.. _`pmic_mpp_pad`:

struct pmic_mpp_pad
===================

.. c:type:: struct pmic_mpp_pad

    keep current MPP settings

.. _`pmic_mpp_pad.definition`:

Definition
----------

.. code-block:: c

    struct pmic_mpp_pad {
        u16 base;
        int irq;
        bool is_enabled;
        bool out_value;
        bool output_enabled;
        bool input_enabled;
        bool paired;
        bool has_pullup;
        unsigned int num_sources;
        unsigned int power_source;
        unsigned int amux_input;
        unsigned int aout_level;
        unsigned int pullup;
        unsigned int function;
        unsigned int drive_strength;
        unsigned int dtest;
    }

.. _`pmic_mpp_pad.members`:

Members
-------

base
    Address base in SPMI device.

irq
    IRQ number which this MPP generate.

is_enabled
    Set to false when MPP should be put in high Z state.

out_value
    Cached pin output value.

output_enabled
    Set to true if MPP output logic is enabled.

input_enabled
    Set to true if MPP input buffer logic is enabled.

paired
    Pin operates in paired mode

has_pullup
    Pin has support to configure pullup

num_sources
    Number of power-sources supported by this MPP.

power_source
    Current power-source used.

amux_input
    Set the source for analog input.

aout_level
    Analog output level

pullup
    Pullup resistor value. Valid in Bidirectional mode only.

function
    See pmic_mpp_functions[].

drive_strength
    Amount of current in sink mode

dtest
    DTEST route selector

.. This file was automatic generated / don't edit.

