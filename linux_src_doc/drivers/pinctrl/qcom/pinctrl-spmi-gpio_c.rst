.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/qcom/pinctrl-spmi-gpio.c

.. _`pmic_gpio_pad`:

struct pmic_gpio_pad
====================

.. c:type:: struct pmic_gpio_pad

    keep current GPIO settings

.. _`pmic_gpio_pad.definition`:

Definition
----------

.. code-block:: c

    struct pmic_gpio_pad {
        u16 base;
        int irq;
        bool is_enabled;
        bool out_value;
        bool have_buffer;
        bool output_enabled;
        bool input_enabled;
        bool analog_pass;
        bool lv_mv_type;
        unsigned int num_sources;
        unsigned int power_source;
        unsigned int buffer_type;
        unsigned int pullup;
        unsigned int strength;
        unsigned int function;
        unsigned int atest;
        unsigned int dtest_buffer;
    }

.. _`pmic_gpio_pad.members`:

Members
-------

base
    Address base in SPMI device.

irq
    IRQ number which this GPIO generate.

is_enabled
    Set to false when GPIO should be put in high Z state.

out_value
    Cached pin output value

have_buffer
    Set to true if GPIO output could be configured in push-pull,
    open-drain or open-source mode.

output_enabled
    Set to true if GPIO output logic is enabled.

input_enabled
    Set to true if GPIO input buffer logic is enabled.

analog_pass
    Set to true if GPIO is in analog-pass-through mode.

lv_mv_type
    Set to true if GPIO subtype is GPIO_LV(0x10) or GPIO_MV(0x11).

num_sources
    Number of power-sources supported by this GPIO.

power_source
    Current power-source used.

buffer_type
    Push-pull, open-drain or open-source.

pullup
    Constant current which flow trough GPIO output buffer.

strength
    No, Low, Medium, High

function
    See pmic_gpio_functions[]

atest
    the ATEST selection for GPIO analog-pass-through mode

dtest_buffer
    the DTEST buffer selection for digital input mode.

.. This file was automatic generated / don't edit.

