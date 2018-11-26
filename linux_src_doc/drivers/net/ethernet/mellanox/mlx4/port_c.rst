.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx4/port.c

.. _`mlx4_get_module_info`:

mlx4_get_module_info
====================

.. c:function:: int mlx4_get_module_info(struct mlx4_dev *dev, u8 port, u16 offset, u16 size, u8 *data)

    Read cable module eeprom data

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        port number.
    :type port: u8

    :param offset:
        byte offset in eeprom to start reading data from.
    :type offset: u16

    :param size:
        num of bytes to read.
    :type size: u16

    :param data:
        output buffer to put the requested data into.
    :type data: u8 \*

.. _`mlx4_get_module_info.description`:

Description
-----------

Reads cable module eeprom data, puts the outcome data into
data pointer paramer.
Returns num of read bytes on success or a negative error
code.

.. This file was automatic generated / don't edit.

