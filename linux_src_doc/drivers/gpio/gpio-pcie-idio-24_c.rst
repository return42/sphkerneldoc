.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-pcie-idio-24.c

.. _`idio_24_gpio_reg`:

struct idio_24_gpio_reg
=======================

.. c:type:: struct idio_24_gpio_reg

    GPIO device registers structure

.. _`idio_24_gpio_reg.definition`:

Definition
----------

.. code-block:: c

    struct idio_24_gpio_reg {
        u8 out0_7;
        u8 out8_15;
        u8 out16_23;
        u8 ttl_out0_7;
        u8 in0_7;
        u8 in8_15;
        u8 in16_23;
        u8 ttl_in0_7;
        u8 cos0_7;
        u8 cos8_15;
        u8 cos16_23;
        u8 cos_ttl0_7;
        u8 ctl;
        u8 reserved;
        u8 cos_enable;
        u8 soft_reset;
    }

.. _`idio_24_gpio_reg.members`:

Members
-------

out0_7
    Read: FET Outputs 0-7
    Write: FET Outputs 0-7

out8_15
    Read: FET Outputs 8-15
    Write: FET Outputs 8-15

out16_23
    Read: FET Outputs 16-23
    Write: FET Outputs 16-23

ttl_out0_7
    Read: TTL/CMOS Outputs 0-7
    Write: TTL/CMOS Outputs 0-7

in0_7
    Read: Isolated Inputs 0-7
    Write: Reserved

in8_15
    Read: Isolated Inputs 8-15
    Write: Reserved

in16_23
    Read: Isolated Inputs 16-23
    Write: Reserved

ttl_in0_7
    Read: TTL/CMOS Inputs 0-7
    Write: Reserved

cos0_7
    Read: COS Status Inputs 0-7
    Write: COS Clear Inputs 0-7

cos8_15
    Read: COS Status Inputs 8-15
    Write: COS Clear Inputs 8-15

cos16_23
    Read: COS Status Inputs 16-23
    Write: COS Clear Inputs 16-23

cos_ttl0_7
    Read: COS Status TTL/CMOS 0-7
    Write: COS Clear TTL/CMOS 0-7

ctl
    Read: Control Register
    Write: Control Register

reserved
    Read: Reserved
    Write: Reserved

cos_enable
    Read: COS Enable
    Write: COS Enable

soft_reset
    Read: IRQ Output Pin Status
    Write: Software Board Reset

.. _`idio_24_gpio`:

struct idio_24_gpio
===================

.. c:type:: struct idio_24_gpio

    GPIO device private data structure

.. _`idio_24_gpio.definition`:

Definition
----------

.. code-block:: c

    struct idio_24_gpio {
        struct gpio_chip chip;
        raw_spinlock_t lock;
        struct idio_24_gpio_reg __iomem *reg;
        unsigned long irq_mask;
    }

.. _`idio_24_gpio.members`:

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

