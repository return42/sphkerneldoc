.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spi/spi_gpio.h

.. _`spi_gpio_platform_data`:

struct spi_gpio_platform_data
=============================

.. c:type:: struct spi_gpio_platform_data

    parameter for bitbanged SPI master

.. _`spi_gpio_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct spi_gpio_platform_data {
        u16 num_chipselect;
    }

.. _`spi_gpio_platform_data.members`:

Members
-------

num_chipselect
    how many slaves to allow

.. This file was automatic generated / don't edit.

