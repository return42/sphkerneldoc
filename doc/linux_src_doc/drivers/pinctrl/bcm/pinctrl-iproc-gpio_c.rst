.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/bcm/pinctrl-iproc-gpio.c

.. _`iproc_set_bit`:

iproc_set_bit
=============

.. c:function:: void iproc_set_bit(struct iproc_gpio *chip, unsigned int reg, unsigned gpio, bool set)

    set or clear one bit (corresponding to the GPIO pin) in a Iproc GPIO register

    :param struct iproc_gpio \*chip:
        *undescribed*

    :param unsigned int reg:
        register offset

    :param unsigned gpio:
        GPIO pin

    :param bool set:
        set or clear

.. _`iproc_gpio_irq_set_mask`:

iproc_gpio_irq_set_mask
=======================

.. c:function:: void iproc_gpio_irq_set_mask(struct irq_data *d, bool unmask)

    mask/unmask a GPIO interrupt

    :param struct irq_data \*d:
        IRQ chip data

    :param bool unmask:
        mask/unmask GPIO interrupt

.. This file was automatic generated / don't edit.

