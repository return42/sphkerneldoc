.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regulator/gpio-regulator.h

.. _`gpio_regulator_state`:

struct gpio_regulator_state
===========================

.. c:type:: struct gpio_regulator_state

    state description

.. _`gpio_regulator_state.definition`:

Definition
----------

.. code-block:: c

    struct gpio_regulator_state {
        int value;
        int gpios;
    }

.. _`gpio_regulator_state.members`:

Members
-------

value
    microvolts or microamps

gpios
    bitfield of gpio target-states for the value

.. _`gpio_regulator_state.description`:

Description
-----------

This structure describes a supported setting of the regulator
and the necessary gpio-state to achieve it.

The n-th bit in the bitfield describes the state of the n-th GPIO
from the gpios-array defined in gpio_regulator_config below.

.. _`gpio_regulator_config`:

struct gpio_regulator_config
============================

.. c:type:: struct gpio_regulator_config

    config structure

.. _`gpio_regulator_config.definition`:

Definition
----------

.. code-block:: c

    struct gpio_regulator_config {
        const char *supply_name;
        int enable_gpio;
        unsigned enable_high:1;
        unsigned enabled_at_boot:1;
        unsigned startup_delay;
        struct gpio *gpios;
        int nr_gpios;
        struct gpio_regulator_state *states;
        int nr_states;
        enum regulator_type type;
        struct regulator_init_data *init_data;
    }

.. _`gpio_regulator_config.members`:

Members
-------

supply_name
    Name of the regulator supply

enable_gpio
    GPIO to use for enable control
    set to -EINVAL if not used

enable_high
    Polarity of enable GPIO
    1 = Active high, 0 = Active low

enabled_at_boot
    Whether regulator has been enabled at
    boot or not. 1 = Yes, 0 = No
    This is used to keep the regulator at
    the default state

startup_delay
    Start-up time in microseconds

gpios
    Array containing the gpios needed to control
    the setting of the regulator

nr_gpios
    Number of gpios

states
    Array of gpio_regulator_state entries describing
    the gpio state for specific voltages

nr_states
    Number of states available

type
    *undescribed*

init_data
    regulator_init_data

.. _`gpio_regulator_config.description`:

Description
-----------

This structure contains gpio-voltage regulator configuration
information that must be passed by platform code to the
gpio-voltage regulator driver.

.. This file was automatic generated / don't edit.

