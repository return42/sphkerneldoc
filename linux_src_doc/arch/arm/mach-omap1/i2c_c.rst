.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap1/i2c.c

.. _`omap_i2c_bus_setup`:

omap_i2c_bus_setup
==================

.. c:function:: int omap_i2c_bus_setup(char *str)

    Process command line options for the I2C bus speed

    :param str:
        String of options
    :type str: char \*

.. _`omap_i2c_bus_setup.description`:

Description
-----------

This function allow to override the default I2C bus speed for given I2C
bus with a command line option.

.. _`omap_i2c_bus_setup.format`:

Format
------

i2c_bus=bus_id,clkrate (in kHz)

Returns 1 on success, 0 otherwise.

.. _`omap_register_i2c_bus`:

omap_register_i2c_bus
=====================

.. c:function:: int omap_register_i2c_bus(int bus_id, u32 clkrate, struct i2c_board_info const *info, unsigned len)

    register I2C bus with device descriptors

    :param bus_id:
        bus id counting from number 1
    :type bus_id: int

    :param clkrate:
        clock rate of the bus in kHz
    :type clkrate: u32

    :param info:
        pointer into I2C device descriptor table or NULL
    :type info: struct i2c_board_info const \*

    :param len:
        number of descriptors in the table
    :type len: unsigned

.. _`omap_register_i2c_bus.description`:

Description
-----------

Returns 0 on success or an error code.

.. This file was automatic generated / don't edit.

