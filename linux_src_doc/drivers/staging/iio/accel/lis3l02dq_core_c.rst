.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/accel/lis3l02dq_core.c

.. _`lis3l02dq_spi_read_reg_8`:

lis3l02dq_spi_read_reg_8
========================

.. c:function:: int lis3l02dq_spi_read_reg_8(struct iio_dev *indio_dev, u8 reg_address, u8 *val)

    read single byte from a single register

    :param struct iio_dev \*indio_dev:
        iio_dev for this actual device

    :param u8 reg_address:
        the address of the register to be read

    :param u8 \*val:
        pass back the resulting value

.. _`lis3l02dq_spi_write_reg_8`:

lis3l02dq_spi_write_reg_8
=========================

.. c:function:: int lis3l02dq_spi_write_reg_8(struct iio_dev *indio_dev, u8 reg_address, u8 val)

    write single byte to a register

    :param struct iio_dev \*indio_dev:
        iio_dev for this device

    :param u8 reg_address:
        the address of the register to be written

    :param u8 val:
        the value to write

.. _`lis3l02dq_spi_write_reg_s16`:

lis3l02dq_spi_write_reg_s16
===========================

.. c:function:: int lis3l02dq_spi_write_reg_s16(struct iio_dev *indio_dev, u8 lower_reg_address, s16 value)

    write 2 bytes to a pair of registers

    :param struct iio_dev \*indio_dev:
        iio_dev for this device

    :param u8 lower_reg_address:
        the address of the lower of the two registers.
        Second register is assumed to have address one greater.

    :param s16 value:
        value to be written

.. This file was automatic generated / don't edit.

