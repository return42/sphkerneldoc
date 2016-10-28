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
        unsigned sck;
        unsigned long mosi;
        unsigned long miso;
        u16 num_chipselect;
    }

.. _`spi_gpio_platform_data.members`:

Members
-------

sck
    number of the GPIO used for clock output

mosi
    number of the GPIO used for Master Output, Slave In (MOSI) data

miso
    number of the GPIO used for Master Input, Slave Output (MISO) data

num_chipselect
    how many slaves to allow

.. _`spi_gpio_platform_data.description`:

Description
-----------

All GPIO signals used with the SPI bus managed through this driver
(chipselects, MOSI, MISO, SCK) must be configured as GPIOs, instead
of some alternate function.

It can be convenient to use this driver with pins that have alternate
functions associated with a "native" SPI controller if a driver for that
controller is not available, or is missing important functionality.

On platforms which can do so, configure MISO with a weak pullup unless
there's an external pullup on that signal.  That saves power by avoiding
floating signals.  (A weak pulldown would save power too, but many
drivers expect to see all-ones data as the no slave "response".)

.. This file was automatic generated / don't edit.

