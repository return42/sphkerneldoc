.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/gyro/adis16060_core.c

.. _`adis16060_state`:

struct adis16060_state
======================

.. c:type:: struct adis16060_state

    device instance specific data

.. _`adis16060_state.definition`:

Definition
----------

.. code-block:: c

    struct adis16060_state {
        struct spi_device *us_w;
        struct spi_device *us_r;
        struct mutex buf_lock;
        u8 buf;
    }

.. _`adis16060_state.members`:

Members
-------

us_w
    actual spi_device to write config

us_r
    actual spi_device to read back data

buf_lock
    mutex to protect tx and rx

buf
    transmit or receive buffer

.. This file was automatic generated / don't edit.

