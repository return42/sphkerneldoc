.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/accel/lis3l02dq.h

.. _`lis3l02dq_state`:

struct lis3l02dq_state
======================

.. c:type:: struct lis3l02dq_state

    device instance specific data

.. _`lis3l02dq_state.definition`:

Definition
----------

.. code-block:: c

    struct lis3l02dq_state {
        struct spi_device *us;
        struct iio_trigger *trig;
        struct mutex buf_lock;
        int gpio;
        bool trigger_on;
        u8 tx[LIS3L02DQ_MAX_RX] ____cacheline_aligned;
        u8 rx[LIS3L02DQ_MAX_RX] ____cacheline_aligned;
    }

.. _`lis3l02dq_state.members`:

Members
-------

us
    actual spi_device

trig
    data ready trigger registered with iio

buf_lock
    mutex to protect tx and rx

gpio
    *undescribed*

trigger_on
    *undescribed*

tx
    transmit buffer

rx
    receive buffer

.. This file was automatic generated / don't edit.

