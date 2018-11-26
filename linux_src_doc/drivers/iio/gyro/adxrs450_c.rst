.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/gyro/adxrs450.c

.. _`adxrs450_state`:

struct adxrs450_state
=====================

.. c:type:: struct adxrs450_state

    device instance specific data

.. _`adxrs450_state.definition`:

Definition
----------

.. code-block:: c

    struct adxrs450_state {
        struct spi_device *us;
        struct mutex buf_lock;
        __be32 tx ____cacheline_aligned;
        __be32 rx;
    }

.. _`adxrs450_state.members`:

Members
-------

us
    actual spi_device

buf_lock
    mutex to protect tx and rx

\____cacheline_aligned
    *undescribed*

rx
    receive buffer

.. _`adxrs450_spi_read_reg_16`:

adxrs450_spi_read_reg_16
========================

.. c:function:: int adxrs450_spi_read_reg_16(struct iio_dev *indio_dev, u8 reg_address, u16 *val)

    read 2 bytes from a register pair

    :param indio_dev:
        device associated with child of actual iio_dev
    :type indio_dev: struct iio_dev \*

    :param reg_address:
        the address of the lower of the two registers, which should be
        an even address, the second register's address is reg_address + 1.
    :type reg_address: u8

    :param val:
        somewhere to pass back the value read
    :type val: u16 \*

.. _`adxrs450_spi_write_reg_16`:

adxrs450_spi_write_reg_16
=========================

.. c:function:: int adxrs450_spi_write_reg_16(struct iio_dev *indio_dev, u8 reg_address, u16 val)

    write 2 bytes data to a register pair

    :param indio_dev:
        device associated with child of actual actual iio_dev
    :type indio_dev: struct iio_dev \*

    :param reg_address:
        the address of the lower of the two registers,which should be
        an even address, the second register's address is reg_address + 1.
    :type reg_address: u8

    :param val:
        value to be written.
    :type val: u16

.. _`adxrs450_spi_sensor_data`:

adxrs450_spi_sensor_data
========================

.. c:function:: int adxrs450_spi_sensor_data(struct iio_dev *indio_dev, s16 *val)

    read 2 bytes sensor data

    :param indio_dev:
        device associated with child of actual iio_dev
    :type indio_dev: struct iio_dev \*

    :param val:
        somewhere to pass back the value read
    :type val: s16 \*

.. _`adxrs450_spi_initial`:

adxrs450_spi_initial
====================

.. c:function:: int adxrs450_spi_initial(struct adxrs450_state *st, u32 *val, char chk)

    use for initializing procedure.

    :param st:
        device instance specific data
    :type st: struct adxrs450_state \*

    :param val:
        somewhere to pass back the value read
    :type val: u32 \*

    :param chk:
        Whether to perform fault check
    :type chk: char

.. This file was automatic generated / don't edit.

