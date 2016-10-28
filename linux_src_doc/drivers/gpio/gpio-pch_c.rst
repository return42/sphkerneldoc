.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-pch.c

.. _`pch_gpio_reg_data`:

struct pch_gpio_reg_data
========================

.. c:type:: struct pch_gpio_reg_data

    The register store data.

.. _`pch_gpio_reg_data.definition`:

Definition
----------

.. code-block:: c

    struct pch_gpio_reg_data {
        u32 ien_reg;
        u32 imask_reg;
        u32 po_reg;
        u32 pm_reg;
        u32 im0_reg;
        u32 im1_reg;
        u32 gpio_use_sel_reg;
    }

.. _`pch_gpio_reg_data.members`:

Members
-------

ien_reg
    To store contents of IEN register.

imask_reg
    To store contents of IMASK register.

po_reg
    To store contents of PO register.

pm_reg
    To store contents of PM register.

im0_reg
    To store contents of IM0 register.

im1_reg
    To store contents of IM1 register.

gpio_use_sel_reg
    To store contents of GPIO_USE_SEL register.
    (Only ML7223 Bus-n)

.. _`pch_gpio`:

struct pch_gpio
===============

.. c:type:: struct pch_gpio

    GPIO private data structure.

.. _`pch_gpio.definition`:

Definition
----------

.. code-block:: c

    struct pch_gpio {
        void __iomem *base;
        struct pch_regs __iomem *reg;
        struct device *dev;
        struct gpio_chip gpio;
        struct pch_gpio_reg_data pch_gpio_reg;
        int irq_base;
        enum pch_type_t ioh;
        spinlock_t spinlock;
    }

.. _`pch_gpio.members`:

Members
-------

base
    PCI base address of Memory mapped I/O register.

reg
    Memory mapped PCH GPIO register list.

dev
    Pointer to device structure.

gpio
    Data for GPIO infrastructure.

pch_gpio_reg
    Memory mapped Register data is saved here
    when suspend.

irq_base
    Save base of IRQ number for interrupt

ioh
    IOH ID

spinlock
    Used for register access protection

.. This file was automatic generated / don't edit.

