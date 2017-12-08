.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dac/ti-dac082s085.c

.. _`ti_dac_chip`:

struct ti_dac_chip
==================

.. c:type:: struct ti_dac_chip

    TI DAC chip

.. _`ti_dac_chip.definition`:

Definition
----------

.. code-block:: c

    struct ti_dac_chip {
        struct mutex lock;
        struct regulator *vref;
        struct spi_message mesg;
        struct spi_transfer xfer;
        u16 val[4];
        bool powerdown;
        u8 powerdown_mode;
        u8 resolution;
        u8 buf[2] ____cacheline_aligned;
    }

.. _`ti_dac_chip.members`:

Members
-------

lock
    protects write sequences

vref
    regulator generating Vref

mesg
    SPI message to perform a write

xfer
    SPI transfer used by \ ``mesg``\ 

val
    cached value of each output

powerdown
    whether the chip is powered down

powerdown_mode
    selected by the user

resolution
    resolution of the chip

buf
    buffer for \ ``xfer``\ 

.. This file was automatic generated / don't edit.

