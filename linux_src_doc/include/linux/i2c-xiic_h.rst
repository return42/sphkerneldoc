.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/i2c-xiic.h

.. _`xiic_i2c_platform_data`:

struct xiic_i2c_platform_data
=============================

.. c:type:: struct xiic_i2c_platform_data

    Platform data of the Xilinx I2C driver

.. _`xiic_i2c_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct xiic_i2c_platform_data {
        u8 num_devices;
        struct i2c_board_info const *devices;
    }

.. _`xiic_i2c_platform_data.members`:

Members
-------

num_devices
    Number of devices that shall be added when the driver
    is probed.

devices
    The actuall devices to add.

.. _`xiic_i2c_platform_data.description`:

Description
-----------

This purpose of this platform data struct is to be able to provide a number
of devices that should be added to the I2C bus. The reason is that sometimes
the I2C board info is not enough, a new PCI board can for instance be
plugged into a standard PC, and the bus number might be unknown at
early init time.

.. This file was automatic generated / don't edit.

