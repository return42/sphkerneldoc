.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-exynos5440.c

.. _`pincfg_type`:

enum pincfg_type
================

.. c:type:: enum pincfg_type

    possible pin configuration types supported.

.. _`pincfg_type.definition`:

Definition
----------

.. code-block:: c

    enum pincfg_type {
        PINCFG_TYPE_PUD,
        PINCFG_TYPE_DRV,
        PINCFG_TYPE_SKEW_RATE,
        PINCFG_TYPE_INPUT_TYPE
    };

.. _`pincfg_type.constants`:

Constants
---------

PINCFG_TYPE_PUD
    Pull up/down configuration.

PINCFG_TYPE_DRV
    Drive strength configuration.

PINCFG_TYPE_SKEW_RATE
    Skew rate configuration.

PINCFG_TYPE_INPUT_TYPE
    Pin input type configuration.

.. _`exynos5440_pin_group`:

struct exynos5440_pin_group
===========================

.. c:type:: struct exynos5440_pin_group

    represent group of pins for pincfg setting.

.. _`exynos5440_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct exynos5440_pin_group {
        const char *name;
        const unsigned int *pins;
        u8 num_pins;
    }

.. _`exynos5440_pin_group.members`:

Members
-------

name
    name of the pin group, used to lookup the group.

pins
    the pins included in this group.

num_pins
    number of pins included in this group.

.. _`exynos5440_pmx_func`:

struct exynos5440_pmx_func
==========================

.. c:type:: struct exynos5440_pmx_func

    represent a pin function.

.. _`exynos5440_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct exynos5440_pmx_func {
        const char *name;
        const char **groups;
        u8 num_groups;
        unsigned long function;
    }

.. _`exynos5440_pmx_func.members`:

Members
-------

name
    name of the pin function, used to lookup the function.

groups
    one or more names of pin groups that provide this function.

num_groups
    number of groups included in \ ``groups``\ .

function
    the function number to be programmed when selected.

.. _`exynos5440_pinctrl_priv_data`:

struct exynos5440_pinctrl_priv_data
===================================

.. c:type:: struct exynos5440_pinctrl_priv_data

    driver's private runtime data.

.. _`exynos5440_pinctrl_priv_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos5440_pinctrl_priv_data {
        void __iomem *reg_base;
        struct gpio_chip *gc;
        struct irq_domain *irq_domain;
        const struct exynos5440_pin_group *pin_groups;
        unsigned int nr_groups;
        const struct exynos5440_pmx_func *pmx_functions;
        unsigned int nr_functions;
        struct pinctrl_gpio_range range;
    }

.. _`exynos5440_pinctrl_priv_data.members`:

Members
-------

reg_base
    ioremapped based address of the register space.

gc
    gpio chip registered with gpiolib.

irq_domain
    *undescribed*

pin_groups
    list of pin groups parsed from device tree.

nr_groups
    number of pin groups available.

pmx_functions
    list of pin functions parsed from device tree.

nr_functions
    number of pin functions available.

range
    gpio range to register with pinctrl

.. _`exynos5440_gpio_intr_data`:

struct exynos5440_gpio_intr_data
================================

.. c:type:: struct exynos5440_gpio_intr_data

    private data for gpio interrupts.

.. _`exynos5440_gpio_intr_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos5440_gpio_intr_data {
        struct exynos5440_pinctrl_priv_data *priv;
        unsigned int gpio_int;
    }

.. _`exynos5440_gpio_intr_data.members`:

Members
-------

priv
    driver's private runtime data.

gpio_int
    gpio interrupt number.

.. This file was automatic generated / don't edit.

