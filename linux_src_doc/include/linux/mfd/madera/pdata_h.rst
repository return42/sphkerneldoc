.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/madera/pdata.h

.. _`madera_pdata`:

struct madera_pdata
===================

.. c:type:: struct madera_pdata

    Configuration data for Madera devices

.. _`madera_pdata.definition`:

Definition
----------

.. code-block:: c

    struct madera_pdata {
        struct gpio_desc *reset;
        struct arizona_ldo1_pdata ldo1;
        struct arizona_micsupp_pdata micvdd;
        unsigned int irq_flags;
        int gpio_base;
        const struct pinctrl_map *gpio_configs;
        int n_gpio_configs;
        u32 gpsw[MADERA_MAX_GPSW];
    }

.. _`madera_pdata.members`:

Members
-------

reset
    GPIO controlling /RESET (NULL = none)

ldo1
    Substruct of pdata for the LDO1 regulator

micvdd
    Substruct of pdata for the MICVDD regulator

irq_flags
    Mode for primary IRQ (defaults to active low)

gpio_base
    Base GPIO number

gpio_configs
    Array of GPIO configurations (See Documentation/pinctrl.txt)

n_gpio_configs
    Number of entries in gpio_configs

gpsw
    General purpose switch mode setting. Depends on the external
    hardware connected to the switch. (See the SW1_MODE field
    in the datasheet for the available values for your codec)

.. This file was automatic generated / don't edit.

