.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/slot-gpio.c

.. _`mmc_gpio_request_ro`:

mmc_gpio_request_ro
===================

.. c:function:: int mmc_gpio_request_ro(struct mmc_host *host, unsigned int gpio)

    request a gpio for write-protection

    :param struct mmc_host \*host:
        mmc host

    :param unsigned int gpio:
        gpio number requested

.. _`mmc_gpio_request_ro.description`:

Description
-----------

As devm\_\* managed functions are used in \ :c:func:`mmc_gpio_request_ro`\ , client
drivers do not need to worry about freeing up memory.

Returns zero on success, else an error.

.. _`mmc_gpio_request_cd`:

mmc_gpio_request_cd
===================

.. c:function:: int mmc_gpio_request_cd(struct mmc_host *host, unsigned int gpio, unsigned int debounce)

    request a gpio for card-detection

    :param struct mmc_host \*host:
        mmc host

    :param unsigned int gpio:
        gpio number requested

    :param unsigned int debounce:
        debounce time in microseconds

.. _`mmc_gpio_request_cd.description`:

Description
-----------

As devm\_\* managed functions are used in \ :c:func:`mmc_gpio_request_cd`\ , client
drivers do not need to worry about freeing up memory.

If GPIO debouncing is desired, set the debounce parameter to a non-zero
value. The caller is responsible for ensuring that the GPIO driver associated
with the GPIO supports debouncing, otherwise an error will be returned.

Returns zero on success, else an error.

.. _`mmc_gpiod_request_cd`:

mmc_gpiod_request_cd
====================

.. c:function:: int mmc_gpiod_request_cd(struct mmc_host *host, const char *con_id, unsigned int idx, bool override_active_level, unsigned int debounce, bool *gpio_invert)

    request a gpio descriptor for card-detection

    :param struct mmc_host \*host:
        mmc host

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned int idx:
        index of the GPIO to obtain in the consumer

    :param bool override_active_level:
        ignore \ ``GPIO_ACTIVE_LOW``\  flag

    :param unsigned int debounce:
        debounce time in microseconds

    :param bool \*gpio_invert:
        will return whether the GPIO line is inverted or not, set
        to NULL to ignore

.. _`mmc_gpiod_request_cd.description`:

Description
-----------

Use this function in place of \ :c:func:`mmc_gpio_request_cd`\  to use the GPIO
descriptor API.  Note that it must be called prior to \ :c:func:`mmc_add_host`\ 
otherwise the caller must also call \ :c:func:`mmc_gpiod_request_cd_irq`\ .

Returns zero on success, else an error.

.. _`mmc_gpiod_request_ro`:

mmc_gpiod_request_ro
====================

.. c:function:: int mmc_gpiod_request_ro(struct mmc_host *host, const char *con_id, unsigned int idx, bool override_active_level, unsigned int debounce, bool *gpio_invert)

    request a gpio descriptor for write protection

    :param struct mmc_host \*host:
        mmc host

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned int idx:
        index of the GPIO to obtain in the consumer

    :param bool override_active_level:
        ignore \ ``GPIO_ACTIVE_LOW``\  flag

    :param unsigned int debounce:
        debounce time in microseconds

    :param bool \*gpio_invert:
        will return whether the GPIO line is inverted or not,
        set to NULL to ignore

.. _`mmc_gpiod_request_ro.description`:

Description
-----------

Use this function in place of \ :c:func:`mmc_gpio_request_ro`\  to use the GPIO
descriptor API.

Returns zero on success, else an error.

.. This file was automatic generated / don't edit.

