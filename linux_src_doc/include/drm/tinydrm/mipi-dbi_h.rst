.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/tinydrm/mipi-dbi.h

.. _`mipi_dbi`:

struct mipi_dbi
===============

.. c:type:: struct mipi_dbi

    MIPI DBI controller

.. _`mipi_dbi.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dbi {
        struct tinydrm_device tinydrm;
        struct spi_device *spi;
        bool enabled;
        struct mutex cmdlock;
        int (*command)(struct mipi_dbi *mipi, u8 cmd, u8 *param, size_t num);
        const u8 *read_commands;
        struct gpio_desc *dc;
        u16 *tx_buf;
        void *tx_buf9;
        size_t tx_buf9_len;
        bool swap_bytes;
        struct gpio_desc *reset;
        unsigned int rotation;
        struct backlight_device *backlight;
        struct regulator *regulator;
    }

.. _`mipi_dbi.members`:

Members
-------

tinydrm
    tinydrm base

spi
    SPI device

enabled
    Pipeline is enabled

cmdlock
    Command lock

command
    Bus specific callback executing commands.

read_commands
    Array of read commands terminated by a zero entry.
    Reading is disabled if this is NULL.

dc
    Optional D/C gpio.

tx_buf
    Buffer used for transfer (copy clip rect area)

tx_buf9
    Buffer used for Option 1 9-bit conversion

tx_buf9_len
    Size of tx_buf9.

swap_bytes
    Swap bytes in buffer before transfer

reset
    Optional reset gpio

rotation
    initial rotation in degrees Counter Clock Wise

backlight
    backlight device (optional)

regulator
    power regulator (optional)

.. _`mipi_dbi_command`:

mipi_dbi_command
================

.. c:function::  mipi_dbi_command( mipi,  cmd,  seq...)

    MIPI DCS command with optional parameter(s)

    :param mipi:
        MIPI structure
    :type mipi: 

    :param cmd:
        Command
    :type cmd: 

.. _`mipi_dbi_command.description`:

Description
-----------

Send MIPI DCS command to the controller. Use \ :c:func:`mipi_dbi_command_read`\  for
get/read.

.. _`mipi_dbi_command.return`:

Return
------

Zero on success, negative error code on failure.

.. This file was automatic generated / don't edit.

