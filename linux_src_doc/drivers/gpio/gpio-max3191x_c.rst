.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-max3191x.c

.. _`max3191x_chip`:

struct max3191x_chip
====================

.. c:type:: struct max3191x_chip

    max3191x daisy-chain

.. _`max3191x_chip.definition`:

Definition
----------

.. code-block:: c

    struct max3191x_chip {
        struct gpio_chip gpio;
        struct mutex lock;
        u32 nchips;
        enum max3191x_mode mode;
        struct gpio_descs *modesel_pins;
        struct gpio_descs *fault_pins;
        struct gpio_descs *db0_pins;
        struct gpio_descs *db1_pins;
        struct spi_message mesg;
        struct spi_transfer xfer;
        unsigned long *crc_error;
        unsigned long *overtemp;
        unsigned long *undervolt1;
        unsigned long *undervolt2;
        unsigned long *fault;
        bool ignore_uv;
    }

.. _`max3191x_chip.members`:

Members
-------

gpio
    GPIO controller struct

lock
    protects read sequences

nchips
    number of chips in the daisy-chain

mode
    current mode, 0 for 16-bit, 1 for 8-bit;
    for simplicity, all chips in the daisy-chain are assumed
    to use the same mode

modesel_pins
    GPIO pins to configure modesel of each chip

fault_pins
    GPIO pins to detect fault of each chip

db0_pins
    GPIO pins to configure debounce of each chip

db1_pins
    GPIO pins to configure debounce of each chip

mesg
    SPI message to perform a readout

xfer
    SPI transfer used by \ ``mesg``\ 

crc_error
    bitmap signaling CRC error for each chip

overtemp
    bitmap signaling overtemperature alarm for each chip

undervolt1
    bitmap signaling undervoltage alarm for each chip

undervolt2
    bitmap signaling undervoltage warning for each chip

fault
    bitmap signaling assertion of \ ``fault_pins``\  for each chip

ignore_uv
    whether to ignore undervoltage alarms;
    set by a device property if the chips are powered through
    5VOUT instead of VCC24V, in which case they will constantly
    signal undervoltage;
    for simplicity, all chips in the daisy-chain are assumed
    to be powered the same way

.. This file was automatic generated / don't edit.

