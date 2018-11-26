.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-stp-xway.c

.. _`xway_stp_get`:

xway_stp_get
============

.. c:function:: int xway_stp_get(struct gpio_chip *gc, unsigned int gpio)

    gpio_chip->get - get gpios.

    :param gc:
        Pointer to gpio_chip device structure.
    :type gc: struct gpio_chip \*

    :param gpio:
        GPIO signal number.
    :type gpio: unsigned int

.. _`xway_stp_get.description`:

Description
-----------

Gets the shadow value.

.. _`xway_stp_set`:

xway_stp_set
============

.. c:function:: void xway_stp_set(struct gpio_chip *gc, unsigned gpio, int val)

    gpio_chip->set - set gpios.

    :param gc:
        Pointer to gpio_chip device structure.
    :type gc: struct gpio_chip \*

    :param gpio:
        GPIO signal number.
    :type gpio: unsigned

    :param val:
        Value to be written to specified signal.
    :type val: int

.. _`xway_stp_set.description`:

Description
-----------

Set the shadow value and call ltq_ebu_apply.

.. _`xway_stp_dir_out`:

xway_stp_dir_out
================

.. c:function:: int xway_stp_dir_out(struct gpio_chip *gc, unsigned gpio, int val)

    gpio_chip->dir_out - set gpio direction.

    :param gc:
        Pointer to gpio_chip device structure.
    :type gc: struct gpio_chip \*

    :param gpio:
        GPIO signal number.
    :type gpio: unsigned

    :param val:
        Value to be written to specified signal.
    :type val: int

.. _`xway_stp_dir_out.description`:

Description
-----------

Same as xway_stp_set, always returns 0.

.. _`xway_stp_request`:

xway_stp_request
================

.. c:function:: int xway_stp_request(struct gpio_chip *gc, unsigned gpio)

    gpio_chip->request

    :param gc:
        Pointer to gpio_chip device structure.
    :type gc: struct gpio_chip \*

    :param gpio:
        GPIO signal number.
    :type gpio: unsigned

.. _`xway_stp_request.description`:

Description
-----------

We mask out the HW driven pins

.. _`xway_stp_hw_init`:

xway_stp_hw_init
================

.. c:function:: int xway_stp_hw_init(struct xway_stp *chip)

    Configure the STP unit and enable the clock gate

    :param chip:
        *undescribed*
    :type chip: struct xway_stp \*

.. This file was automatic generated / don't edit.

