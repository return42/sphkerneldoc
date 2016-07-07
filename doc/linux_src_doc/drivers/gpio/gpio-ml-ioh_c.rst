.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-ml-ioh.c

.. _`ioh_gpio_reg_data`:

struct ioh_gpio_reg_data
========================

.. c:type:: struct ioh_gpio_reg_data

    The register store data. \ ``ien_reg``\      To store contents of interrupt enable register.

.. _`ioh_gpio_reg_data.definition`:

Definition
----------

.. code-block:: c

    struct ioh_gpio_reg_data {
        u32 ien_reg;
        u32 imask_reg;
        u32 po_reg;
        u32 pm_reg;
        u32 im0_reg;
        u32 im1_reg;
        u32 use_sel_reg;
    }

.. _`ioh_gpio_reg_data.members`:

Members
-------

ien_reg
    *undescribed*

imask_reg
    To store contents of interrupt mask regist

po_reg
    To store contents of PO register.

pm_reg
    To store contents of PM register.

im0_reg
    To store contents of interrupt mode regist0

im1_reg
    To store contents of interrupt mode regist1

use_sel_reg
    To store contents of GPIO_USE_SEL0~3

.. _`ioh_gpio`:

struct ioh_gpio
===============

.. c:type:: struct ioh_gpio

    GPIO private data structure.

.. _`ioh_gpio.definition`:

Definition
----------

.. code-block:: c

    struct ioh_gpio {
        void __iomem *base;
        struct ioh_regs __iomem *reg;
        struct device *dev;
        struct gpio_chip gpio;
        struct ioh_gpio_reg_data ioh_gpio_reg;
        u32 gpio_use_sel;
        int ch;
        int irq_base;
        spinlock_t spinlock;
    }

.. _`ioh_gpio.members`:

Members
-------

base
    PCI base address of Memory mapped I/O register.

reg
    Memory mapped IOH GPIO register list.

dev
    Pointer to device structure.

gpio
    Data for GPIO infrastructure.

ioh_gpio_reg
    Memory mapped Register data is saved here
    when suspend.

gpio_use_sel
    Save GPIO_USE_SEL1~4 register for PM

ch
    Indicate GPIO channel

irq_base
    Save base of IRQ number for interrupt

spinlock
    Used for register access protection

.. This file was automatic generated / don't edit.

