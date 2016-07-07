.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/power/gpio-charger.h

.. _`gpio_charger_platform_data`:

struct gpio_charger_platform_data
=================================

.. c:type:: struct gpio_charger_platform_data

    platform_data for gpio_charger devices

.. _`gpio_charger_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct gpio_charger_platform_data {
        const char *name;
        enum power_supply_type type;
        int gpio;
        int gpio_active_low;
        char **supplied_to;
        size_t num_supplicants;
    }

.. _`gpio_charger_platform_data.members`:

Members
-------

name
    Name for the chargers power_supply device

type
    Type of the charger

gpio
    GPIO which is used to indicate the chargers status

gpio_active_low
    Should be set to 1 if the GPIO is active low otherwise 0

supplied_to
    Array of battery names to which this chargers supplies power

num_supplicants
    Number of entries in the supplied_to array

.. This file was automatic generated / don't edit.

