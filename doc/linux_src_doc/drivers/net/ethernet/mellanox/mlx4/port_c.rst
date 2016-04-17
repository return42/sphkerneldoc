.. -*- coding: utf-8; mode: rst -*-

======
port.c
======


.. _`mlx4_get_module_info`:

mlx4_get_module_info
====================

.. c:function:: int mlx4_get_module_info (struct mlx4_dev *dev, u8 port, u16 offset, u16 size, u8 *data)

    Read cable module eeprom data

    :param struct mlx4_dev \*dev:
        mlx4_dev.

    :param u8 port:
        port number.

    :param u16 offset:
        byte offset in eeprom to start reading data from.

    :param u16 size:
        num of bytes to read.

    :param u8 \*data:
        output buffer to put the requested data into.



.. _`mlx4_get_module_info.description`:

Description
-----------

Reads cable module eeprom data, puts the outcome data into
data pointer paramer.
Returns num of read bytes on success or a negative error
code.

