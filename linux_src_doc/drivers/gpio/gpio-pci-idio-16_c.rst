.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-pci-idio-16.c

.. _`idio_16_gpio_reg`:

struct idio_16_gpio_reg
=======================

.. c:type:: struct idio_16_gpio_reg

    GPIO device registers structure

.. _`idio_16_gpio_reg.definition`:

Definition
----------

.. code-block:: c

    struct idio_16_gpio_reg {
        u8 out0_7;
        u8 in0_7;
        u8 irq_ctl;
        u8 filter_ctl;
        u8 out8_15;
        u8 in8_15;
        u8 irq_status;
    }

.. _`idio_16_gpio_reg.members`:

Members
-------

out0_7
    Read: FET Drive Outputs 0-7
    Write: FET Drive Outputs 0-7

in0_7
    Read: Isolated Inputs 0-7
    Write: Clear Interrupt

irq_ctl
    Read: Enable IRQ
    Write: Disable IRQ

filter_ctl
    Read: Activate Input Filters 0-15
    Write: Deactivate Input Filters 0-15

out8_15
    Read: FET Drive Outputs 8-15
    Write: FET Drive Outputs 8-15

in8_15
    Read: Isolated Inputs 8-15
    Write: Unused

irq_status
    Read: Interrupt status
    Write: Unused

.. _`idio_16_gpio`:

struct idio_16_gpio
===================

.. c:type:: struct idio_16_gpio

    GPIO device private data structure

.. _`idio_16_gpio.definition`:

Definition
----------

.. code-block:: c

    struct idio_16_gpio {
        struct gpio_chip chip;
        raw_spinlock_t lock;
        struct idio_16_gpio_reg __iomem *reg;
        unsigned long irq_mask;
    }

.. _`idio_16_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

lock
    synchronization lock to prevent I/O race conditions

reg
    I/O address offset for the GPIO device registers

irq_mask
    I/O bits affected by interrupts

.. This file was automatic generated / don't edit.

