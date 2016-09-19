.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/gpio-core.h

.. _`samsung_gpio_pm`:

struct samsung_gpio_pm
======================

.. c:type:: struct samsung_gpio_pm

    power management (suspend/resume) information

.. _`samsung_gpio_pm.definition`:

Definition
----------

.. code-block:: c

    struct samsung_gpio_pm {
        void (*save)(struct samsung_gpio_chip *chip);
        void (*resume)(struct samsung_gpio_chip *chip);
    }

.. _`samsung_gpio_pm.members`:

Members
-------

save
    Routine to save the state of the GPIO block

resume
    Routine to resume the GPIO block.

.. _`samsung_gpio_chip`:

struct samsung_gpio_chip
========================

.. c:type:: struct samsung_gpio_chip

    wrapper for specific implementation of gpio

.. _`samsung_gpio_chip.definition`:

Definition
----------

.. code-block:: c

    struct samsung_gpio_chip {
        struct gpio_chip chip;
        struct samsung_gpio_cfg *config;
        struct samsung_gpio_pm *pm;
        void __iomem *base;
        int irq_base;
        int group;
        spinlock_t lock;
        #ifdef CONFIG_PM
        u32 pm_save[4];
        #endif
        u32 bitmap_gpio_int;
    }

.. _`samsung_gpio_chip.members`:

Members
-------

chip
    The chip structure to be exported via gpiolib.

config
    special function and pull-resistor control information.

pm
    *undescribed*

base
    The base pointer to the gpio configuration registers.

irq_base
    The base irq number.

group
    The group register number for gpio interrupt support.

lock
    Lock for exclusive access to this gpio bank.

pm_save
    Save information for suspend/resume support.

bitmap_gpio_int
    Bitmap for representing GPIO interrupt or not.

.. _`samsung_gpio_chip.description`:

Description
-----------

This wrapper provides the necessary information for the Samsung
specific gpios being registered with gpiolib.

The lock protects each gpio bank from multiple access of the shared
configuration registers, or from reading of data whilst another thread
is writing to the register set.

Each chip has its own lock to avoid any  contention between different
CPU cores trying to get one lock for different GPIO banks, where each
bank of GPIO has its own register space and configuration registers.

.. _`samsung_gpiolib_to_irq`:

samsung_gpiolib_to_irq
======================

.. c:function:: int samsung_gpiolib_to_irq(struct gpio_chip *chip, unsigned int offset)

    convert gpio pin to irq number

    :param struct gpio_chip \*chip:
        The gpio chip that the pin belongs to.

    :param unsigned int offset:
        The offset of the pin in the chip.

.. _`samsung_gpiolib_to_irq.description`:

Description
-----------

This helper returns the irq number calculated from the chip->irq_base and
the provided offset.

.. This file was automatic generated / don't edit.

