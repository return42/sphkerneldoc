.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regulator/fixed.h

.. _`fixed_voltage_config`:

struct fixed_voltage_config
===========================

.. c:type:: struct fixed_voltage_config

    fixed_voltage_config structure

.. _`fixed_voltage_config.definition`:

Definition
----------

.. code-block:: c

    struct fixed_voltage_config {
        const char *supply_name;
        const char *input_supply;
        int microvolts;
        int gpio;
        unsigned startup_delay;
        unsigned gpio_is_open_drain:1;
        unsigned enable_high:1;
        unsigned enabled_at_boot:1;
        struct regulator_init_data *init_data;
    }

.. _`fixed_voltage_config.members`:

Members
-------

supply_name
    Name of the regulator supply

input_supply
    Name of the input regulator supply

microvolts
    Output voltage of regulator

gpio
    GPIO to use for enable control
    set to -EINVAL if not used

startup_delay
    Start-up time in microseconds

gpio_is_open_drain
    Gpio pin is open drain or normal type.
    If it is open drain type then HIGH will be set
    through PULL-UP with setting gpio as input
    and low will be set as gpio-output with driven
    to low. For non-open-drain case, the gpio will
    will be in output and drive to low/high accordingly.

enable_high
    Polarity of enable GPIO
    1 = Active high, 0 = Active low

enabled_at_boot
    Whether regulator has been enabled at
    boot or not. 1 = Yes, 0 = No
    This is used to keep the regulator at
    the default state

init_data
    regulator_init_data

.. _`fixed_voltage_config.description`:

Description
-----------

This structure contains fixed voltage regulator configuration
information that must be passed by platform code to the fixed
voltage regulator driver.

.. This file was automatic generated / don't edit.

