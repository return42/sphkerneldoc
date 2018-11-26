.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/ad_sigma_delta.c

.. _`ad_sd_set_comm`:

ad_sd_set_comm
==============

.. c:function:: void ad_sd_set_comm(struct ad_sigma_delta *sigma_delta, uint8_t comm)

    Set communications register

    :param sigma_delta:
        The sigma delta device
    :type sigma_delta: struct ad_sigma_delta \*

    :param comm:
        New value for the communications register
    :type comm: uint8_t

.. _`ad_sd_write_reg`:

ad_sd_write_reg
===============

.. c:function:: int ad_sd_write_reg(struct ad_sigma_delta *sigma_delta, unsigned int reg, unsigned int size, unsigned int val)

    Write a register

    :param sigma_delta:
        The sigma delta device
    :type sigma_delta: struct ad_sigma_delta \*

    :param reg:
        Address of the register
    :type reg: unsigned int

    :param size:
        Size of the register (0-3)
    :type size: unsigned int

    :param val:
        Value to write to the register
    :type val: unsigned int

.. _`ad_sd_write_reg.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sd_read_reg`:

ad_sd_read_reg
==============

.. c:function:: int ad_sd_read_reg(struct ad_sigma_delta *sigma_delta, unsigned int reg, unsigned int size, unsigned int *val)

    Read a register

    :param sigma_delta:
        The sigma delta device
    :type sigma_delta: struct ad_sigma_delta \*

    :param reg:
        Address of the register
    :type reg: unsigned int

    :param size:
        Size of the register (1-4)
    :type size: unsigned int

    :param val:
        Read value
    :type val: unsigned int \*

.. _`ad_sd_read_reg.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sd_reset`:

ad_sd_reset
===========

.. c:function:: int ad_sd_reset(struct ad_sigma_delta *sigma_delta, unsigned int reset_length)

    Reset the serial interface

    :param sigma_delta:
        The sigma delta device
    :type sigma_delta: struct ad_sigma_delta \*

    :param reset_length:
        Number of SCLKs with DIN = 1
    :type reset_length: unsigned int

.. _`ad_sd_reset.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sd_calibrate_all`:

ad_sd_calibrate_all
===================

.. c:function:: int ad_sd_calibrate_all(struct ad_sigma_delta *sigma_delta, const struct ad_sd_calib_data *cb, unsigned int n)

    Performs channel calibration

    :param sigma_delta:
        The sigma delta device
    :type sigma_delta: struct ad_sigma_delta \*

    :param cb:
        Array of channels and calibration type to perform
    :type cb: const struct ad_sd_calib_data \*

    :param n:
        Number of items in cb
    :type n: unsigned int

.. _`ad_sd_calibrate_all.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sigma_delta_single_conversion`:

ad_sigma_delta_single_conversion
================================

.. c:function:: int ad_sigma_delta_single_conversion(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, int *val)

    Performs a single data conversion

    :param indio_dev:
        The IIO device
    :type indio_dev: struct iio_dev \*

    :param chan:
        The conversion is done for this channel
    :type chan: const struct iio_chan_spec \*

    :param val:
        Pointer to the location where to store the read value
    :type val: int \*

.. _`ad_sigma_delta_single_conversion.return`:

Return
------

0 on success, an error value otherwise.

.. _`ad_sd_validate_trigger`:

ad_sd_validate_trigger
======================

.. c:function:: int ad_sd_validate_trigger(struct iio_dev *indio_dev, struct iio_trigger *trig)

    validate_trigger callback for ad_sigma_delta devices

    :param indio_dev:
        The IIO device
    :type indio_dev: struct iio_dev \*

    :param trig:
        The new trigger
    :type trig: struct iio_trigger \*

.. _`ad_sd_validate_trigger.return`:

Return
------

0 if the 'trig' matches the trigger registered by the ad_sigma_delta
device, -EINVAL otherwise.

.. _`ad_sd_setup_buffer_and_trigger`:

ad_sd_setup_buffer_and_trigger
==============================

.. c:function:: int ad_sd_setup_buffer_and_trigger(struct iio_dev *indio_dev)

    :param indio_dev:
        The IIO device
    :type indio_dev: struct iio_dev \*

.. _`ad_sd_cleanup_buffer_and_trigger`:

ad_sd_cleanup_buffer_and_trigger
================================

.. c:function:: void ad_sd_cleanup_buffer_and_trigger(struct iio_dev *indio_dev)

    :param indio_dev:
        The IIO device
    :type indio_dev: struct iio_dev \*

.. _`ad_sd_init`:

ad_sd_init
==========

.. c:function:: int ad_sd_init(struct ad_sigma_delta *sigma_delta, struct iio_dev *indio_dev, struct spi_device *spi, const struct ad_sigma_delta_info *info)

    Initializes a ad_sigma_delta struct

    :param sigma_delta:
        The ad_sigma_delta device
    :type sigma_delta: struct ad_sigma_delta \*

    :param indio_dev:
        The IIO device which the Sigma Delta device is used for
    :type indio_dev: struct iio_dev \*

    :param spi:
        The SPI device for the ad_sigma_delta device
    :type spi: struct spi_device \*

    :param info:
        Device specific callbacks and options
    :type info: const struct ad_sigma_delta_info \*

.. _`ad_sd_init.description`:

Description
-----------

This function needs to be called before any other operations are performed on
the ad_sigma_delta struct.

.. This file was automatic generated / don't edit.

