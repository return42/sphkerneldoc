.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-at91-pio4.c

.. _`atmel_pioctrl`:

struct atmel_pioctrl
====================

.. c:type:: struct atmel_pioctrl

    Atmel PIO controller (pinmux + gpio)

.. _`atmel_pioctrl.definition`:

Definition
----------

.. code-block:: c

    struct atmel_pioctrl {
        void __iomem *reg_base;
        struct clk *clk;
        unsigned nbanks;
        struct pinctrl_dev *pinctrl_dev;
        struct atmel_group *groups;
        const char * const *group_names;
        struct atmel_pin **pins;
        unsigned npins;
        struct gpio_chip *gpio_chip;
        struct irq_domain *irq_domain;
        int *irqs;
        unsigned *pm_wakeup_sources;
        struct {
            u32 imr;
            u32 odsr;
            u32 cfgr[ATMEL_PIO_NPINS_PER_BANK];
        } *pm_suspend_backup;
        struct device *dev;
        struct device_node *node;
    }

.. _`atmel_pioctrl.members`:

Members
-------

reg_base
    base address of the controller.

clk
    clock of the controller.

nbanks
    number of PIO groups, it can vary depending on the SoC.

pinctrl_dev
    pinctrl device registered.

groups
    groups table to provide group name and pin in the group to pinctrl.

group_names
    group names table to provide all the group/pin names to
    pinctrl or gpio.

pins
    pins table used for both pinctrl and gpio. pin_id, bank and line
    fields are set at probe time. Other ones are set when parsing dt
    pinctrl.

npins
    number of pins.

gpio_chip
    gpio chip registered.

irq_domain
    irq domain for the gpio controller.

irqs
    table containing the hw irq number of the bank. The index of the
    table is the bank id.

pm_wakeup_sources
    *undescribed*

pm_suspend_backup
    *undescribed*

imr
    *undescribed*

odsr
    *undescribed*

cfgr
    *undescribed*

dev
    device entry for the Atmel PIO controller.

node
    node of the Atmel PIO controller.

.. This file was automatic generated / don't edit.

