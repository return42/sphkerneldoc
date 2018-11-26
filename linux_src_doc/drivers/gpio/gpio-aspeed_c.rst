.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-aspeed.c

.. _`aspeed_gpio_copro_set_ops`:

aspeed_gpio_copro_set_ops
=========================

.. c:function:: int aspeed_gpio_copro_set_ops(const struct aspeed_gpio_copro_ops *ops, void *data)

    Sets the callbacks used for handhsaking with the coprocessor for shared GPIO banks

    :param ops:
        The callbacks
    :type ops: const struct aspeed_gpio_copro_ops \*

    :param data:
        Pointer passed back to the callbacks
    :type data: void \*

.. _`aspeed_gpio_copro_grab_gpio`:

aspeed_gpio_copro_grab_gpio
===========================

.. c:function:: int aspeed_gpio_copro_grab_gpio(struct gpio_desc *desc, u16 *vreg_offset, u16 *dreg_offset, u8 *bit)

    Mark a GPIO used by the coprocessor. The entire bank gets marked and any access from the ARM will result in handshaking via callbacks.

    :param desc:
        The GPIO to be marked
    :type desc: struct gpio_desc \*

    :param vreg_offset:
        If non-NULL, returns the value register offset in the GPIO space
    :type vreg_offset: u16 \*

    :param dreg_offset:
        If non-NULL, returns the data latch register offset in the GPIO space
    :type dreg_offset: u16 \*

    :param bit:
        If non-NULL, returns the bit number of the GPIO in the registers
    :type bit: u8 \*

.. _`aspeed_gpio_copro_release_gpio`:

aspeed_gpio_copro_release_gpio
==============================

.. c:function:: int aspeed_gpio_copro_release_gpio(struct gpio_desc *desc)

    Unmark a GPIO used by the coprocessor.

    :param desc:
        The GPIO to be marked
    :type desc: struct gpio_desc \*

.. This file was automatic generated / don't edit.

