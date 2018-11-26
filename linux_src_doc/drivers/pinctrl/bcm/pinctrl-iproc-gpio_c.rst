.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/bcm/pinctrl-iproc-gpio.c

.. _`iproc_set_bit`:

iproc_set_bit
=============

.. c:function:: void iproc_set_bit(struct iproc_gpio *chip, unsigned int reg, unsigned gpio, bool set)

    set or clear one bit (corresponding to the GPIO pin) in a Iproc GPIO register

    :param chip:
        *undescribed*
    :type chip: struct iproc_gpio \*

    :param reg:
        register offset
    :type reg: unsigned int

    :param gpio:
        GPIO pin
    :type gpio: unsigned

    :param set:
        set or clear
    :type set: bool

.. _`iproc_gpio_irq_set_mask`:

iproc_gpio_irq_set_mask
=======================

.. c:function:: void iproc_gpio_irq_set_mask(struct irq_data *d, bool unmask)

    mask/unmask a GPIO interrupt

    :param d:
        IRQ chip data
    :type d: struct irq_data \*

    :param unmask:
        mask/unmask GPIO interrupt
    :type unmask: bool

.. This file was automatic generated / don't edit.

