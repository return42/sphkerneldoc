.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-pmic-eic-sprd.c

.. _`sprd_pmic_eic`:

struct sprd_pmic_eic
====================

.. c:type:: struct sprd_pmic_eic

    PMIC EIC controller

.. _`sprd_pmic_eic.definition`:

Definition
----------

.. code-block:: c

    struct sprd_pmic_eic {
        struct gpio_chip chip;
        struct irq_chip intc;
        struct regmap *map;
        u32 offset;
        u8 reg[CACHE_NR_REGS];
        struct mutex buslock;
        int irq;
    }

.. _`sprd_pmic_eic.members`:

Members
-------

chip
    the gpio_chip structure.

intc
    the irq_chip structure.

map
    *undescribed*

offset
    the EIC controller's offset address of the PMIC.

reg
    the array to cache the EIC registers.

buslock
    for bus lock/sync and unlock.

irq
    the interrupt number of the PMIC EIC conteroller.

.. This file was automatic generated / don't edit.

