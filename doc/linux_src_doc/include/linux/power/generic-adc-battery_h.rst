.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/power/generic-adc-battery.h

.. _`gab_platform_data`:

struct gab_platform_data
========================

.. c:type:: struct gab_platform_data

    platform_data for generic adc iio battery driver.

.. _`gab_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct gab_platform_data {
        struct power_supply_info battery_info;
        int (* cal_charge) (long value);
        int gpio_charge_finished;
        bool gpio_inverted;
        int jitter_delay;
    }

.. _`gab_platform_data.members`:

Members
-------

battery_info
    recommended structure to specify static power supply
    parameters

cal_charge
    calculate charge level.

gpio_charge_finished
    gpio for the charger.

gpio_inverted
    Should be 1 if the GPIO is active low otherwise 0

jitter_delay
    delay required after the interrupt to check battery
    status.Default set is 10ms.

.. This file was automatic generated / don't edit.

