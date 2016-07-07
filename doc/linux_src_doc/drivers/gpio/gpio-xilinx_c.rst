.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-xilinx.c

.. _`xgpio_instance`:

struct xgpio_instance
=====================

.. c:type:: struct xgpio_instance

    Stores information about GPIO device

.. _`xgpio_instance.definition`:

Definition
----------

.. code-block:: c

    struct xgpio_instance {
        struct of_mm_gpio_chip mmchip;
        unsigned int gpio_width[2];
        u32 gpio_state[2];
        u32 gpio_dir[2];
        spinlock_t gpio_lock[2];
    }

.. _`xgpio_instance.members`:

Members
-------

mmchip
    OF GPIO chip for memory mapped banks

gpio_width
    GPIO width for every channel

gpio_state
    GPIO state shadow register

gpio_dir
    GPIO direction shadow register

gpio_lock
    Lock used for synchronization

.. _`xgpio_get`:

xgpio_get
=========

.. c:function:: int xgpio_get(struct gpio_chip *gc, unsigned int gpio)

    Read the specified signal of the GPIO device.

    :param struct gpio_chip \*gc:
        Pointer to gpio_chip device structure.

    :param unsigned int gpio:
        GPIO signal number.

.. _`xgpio_get.description`:

Description
-----------

This function reads the specified signal of the GPIO device.

.. _`xgpio_get.return`:

Return
------

0 if direction of GPIO signals is set as input otherwise it
returns negative error value.

.. _`xgpio_set`:

xgpio_set
=========

.. c:function:: void xgpio_set(struct gpio_chip *gc, unsigned int gpio, int val)

    Write the specified signal of the GPIO device.

    :param struct gpio_chip \*gc:
        Pointer to gpio_chip device structure.

    :param unsigned int gpio:
        GPIO signal number.

    :param int val:
        Value to be written to specified signal.

.. _`xgpio_set.description`:

Description
-----------

This function writes the specified value in to the specified signal of the
GPIO device.

.. _`xgpio_dir_in`:

xgpio_dir_in
============

.. c:function:: int xgpio_dir_in(struct gpio_chip *gc, unsigned int gpio)

    Set the direction of the specified GPIO signal as input.

    :param struct gpio_chip \*gc:
        Pointer to gpio_chip device structure.

    :param unsigned int gpio:
        GPIO signal number.

.. _`xgpio_dir_in.return`:

Return
------

0 - if direction of GPIO signals is set as input
otherwise it returns negative error value.

.. _`xgpio_dir_out`:

xgpio_dir_out
=============

.. c:function:: int xgpio_dir_out(struct gpio_chip *gc, unsigned int gpio, int val)

    Set the direction of the specified GPIO signal as output.

    :param struct gpio_chip \*gc:
        Pointer to gpio_chip device structure.

    :param unsigned int gpio:
        GPIO signal number.

    :param int val:
        Value to be written to specified signal.

.. _`xgpio_dir_out.description`:

Description
-----------

This function sets the direction of specified GPIO signal as output.

.. _`xgpio_dir_out.return`:

Return
------

If all GPIO signals of GPIO chip is configured as input then it returns
error otherwise it returns 0.

.. _`xgpio_save_regs`:

xgpio_save_regs
===============

.. c:function:: void xgpio_save_regs(struct of_mm_gpio_chip *mm_gc)

    Set initial values of GPIO pins

    :param struct of_mm_gpio_chip \*mm_gc:
        Pointer to memory mapped GPIO chip structure

.. _`xgpio_remove`:

xgpio_remove
============

.. c:function:: int xgpio_remove(struct platform_device *pdev)

    Remove method for the GPIO device.

    :param struct platform_device \*pdev:
        pointer to the platform device

.. _`xgpio_remove.description`:

Description
-----------

This function remove gpiochips and frees all the allocated resources.

.. _`xgpio_remove.return`:

Return
------

0 always

.. _`xgpio_probe`:

xgpio_probe
===========

.. c:function:: int xgpio_probe(struct platform_device *pdev)

    Probe method for the GPIO device.

    :param struct platform_device \*pdev:
        pointer to the platform device

.. _`xgpio_probe.return`:

Return
------

It returns 0, if the driver is bound to the GPIO device, or
a negative value if there is an error.

.. This file was automatic generated / don't edit.

