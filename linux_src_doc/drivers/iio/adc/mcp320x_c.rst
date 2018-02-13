.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/mcp320x.c

.. _`mcp320x`:

struct mcp320x
==============

.. c:type:: struct mcp320x

    Microchip SPI ADC instance

.. _`mcp320x.definition`:

Definition
----------

.. code-block:: c

    struct mcp320x {
        struct spi_device *spi;
        struct spi_message msg;
        struct spi_transfer transfer[2];
        struct spi_message start_conv_msg;
        struct spi_transfer start_conv_transfer;
        struct regulator *reg;
        struct mutex lock;
        const struct mcp320x_chip_info *chip_info;
        u8 tx_buf ____cacheline_aligned;
        u8 rx_buf[4];
    }

.. _`mcp320x.members`:

Members
-------

spi
    SPI slave (parent of the IIO device)

msg
    SPI message to select a channel and receive a value from the ADC

transfer
    SPI transfers used by \ ``msg``\ 

start_conv_msg
    SPI message to start a conversion by briefly asserting CS

start_conv_transfer
    SPI transfer used by \ ``start_conv_msg``\ 

reg
    regulator generating Vref

lock
    protects read sequences

chip_info
    ADC properties

\____cacheline_aligned
    *undescribed*

rx_buf
    buffer for \ ``transfer``\ [1]

.. This file was automatic generated / don't edit.

