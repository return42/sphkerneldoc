.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-reg.c

.. _`gpio_reg_init`:

gpio_reg_init
=============

.. c:function:: struct gpio_chip *gpio_reg_init(struct device *dev, void __iomem *reg, int base, int num, const char *label, u32 direction, u32 def_out, const char *const *names, struct irq_domain *irqdom, const int *irqs)

    add a fixed in/out register as gpio

    :param dev:
        optional struct device associated with this register
    :type dev: struct device \*

    :param reg:
        *undescribed*
    :type reg: void __iomem \*

    :param base:
        start gpio number, or -1 to allocate
    :type base: int

    :param num:
        number of GPIOs, maximum 32
    :type num: int

    :param label:
        GPIO chip label
    :type label: const char \*

    :param direction:
        bitmask of fixed direction, one per GPIO signal, 1 = in
    :type direction: u32

    :param def_out:
        initial GPIO output value
    :type def_out: u32

    :param names:
        array of \ ``num``\  strings describing each GPIO signal or \ ``NULL``\ 
    :type names: const char \*const \*

    :param irqdom:
        irq domain or \ ``NULL``\ 
    :type irqdom: struct irq_domain \*

    :param irqs:
        array of \ ``num``\  ints describing the interrupt mapping for each
        GPIO signal, or \ ``NULL``\ .  If \ ``irqdom``\  is \ ``NULL``\ , then this
        describes the Linux interrupt number, otherwise it describes
        the hardware interrupt number in the specified irq domain.
    :type irqs: const int \*

.. _`gpio_reg_init.description`:

Description
-----------

Add a single-register GPIO device containing up to 32 GPIO signals,
where each GPIO has a fixed input or output configuration.  Only
input GPIOs are assumed to be readable from the register, and only
then after a double-read.  Output values are assumed not to be
readable.

.. This file was automatic generated / don't edit.

