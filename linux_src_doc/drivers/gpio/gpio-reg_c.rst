.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-reg.c

.. _`gpio_reg_init`:

gpio_reg_init
=============

.. c:function:: struct gpio_chip *gpio_reg_init(struct device *dev, void __iomem *reg, int base, int num, const char *label, u32 direction, u32 def_out, const char *const *names, struct irq_domain *irqdom, const int *irqs)

    add a fixed in/out register as gpio

    :param struct device \*dev:
        optional struct device associated with this register

    :param void __iomem \*reg:
        *undescribed*

    :param int base:
        start gpio number, or -1 to allocate

    :param int num:
        number of GPIOs, maximum 32

    :param const char \*label:
        GPIO chip label

    :param u32 direction:
        bitmask of fixed direction, one per GPIO signal, 1 = in

    :param u32 def_out:
        initial GPIO output value

    :param const char \*const \*names:
        array of \ ``num``\  strings describing each GPIO signal or \ ``NULL``\ 

    :param struct irq_domain \*irqdom:
        irq domain or \ ``NULL``\ 

    :param const int \*irqs:
        array of \ ``num``\  ints describing the interrupt mapping for each
        GPIO signal, or \ ``NULL``\ .  If \ ``irqdom``\  is \ ``NULL``\ , then this
        describes the Linux interrupt number, otherwise it describes
        the hardware interrupt number in the specified irq domain.

.. _`gpio_reg_init.description`:

Description
-----------

Add a single-register GPIO device containing up to 32 GPIO signals,
where each GPIO has a fixed input or output configuration.  Only
input GPIOs are assumed to be readable from the register, and only
then after a double-read.  Output values are assumed not to be
readable.

.. This file was automatic generated / don't edit.

