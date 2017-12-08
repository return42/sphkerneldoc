.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/ad_sigma_delta.c

.. _`ad_sd_set_comm`:

ad_sd_set_comm
==============

.. c:function:: void ad_sd_set_comm(struct ad_sigma_delta *sigma_delta, uint8_t comm)

    Set communications register

    :param struct ad_sigma_delta \*sigma_delta:
        The sigma delta device

    :param uint8_t comm:
        New value for the communications register

.. _`ad_sd_write_reg`:

ad_sd_write_reg
===============

.. c:function:: int ad_sd_write_reg(struct ad_sigma_delta *sigma_delta, unsigned int reg, unsigned int size, unsigned int val)

    Write a register

    :param struct ad_sigma_delta \*sigma_delta:
        The sigma delta device

    :param unsigned int reg:
        Address of the register

    :param unsigned int size:
        Size of the register (0-3)

    :param unsigned int val:
        Value to write to the register

.. _`ad_sd_write_reg.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sd_read_reg`:

ad_sd_read_reg
==============

.. c:function:: int ad_sd_read_reg(struct ad_sigma_delta *sigma_delta, unsigned int reg, unsigned int size, unsigned int *val)

    Read a register

    :param struct ad_sigma_delta \*sigma_delta:
        The sigma delta device

    :param unsigned int reg:
        Address of the register

    :param unsigned int size:
        Size of the register (1-4)

    :param unsigned int \*val:
        Read value

.. _`ad_sd_read_reg.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sd_reset`:

ad_sd_reset
===========

.. c:function:: int ad_sd_reset(struct ad_sigma_delta *sigma_delta, unsigned int reset_length)

    Reset the serial interface

    :param struct ad_sigma_delta \*sigma_delta:
        The sigma delta device

    :param unsigned int reset_length:
        Number of SCLKs with DIN = 1

.. _`ad_sd_reset.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sd_calibrate_all`:

ad_sd_calibrate_all
===================

.. c:function:: int ad_sd_calibrate_all(struct ad_sigma_delta *sigma_delta, const struct ad_sd_calib_data *cb, unsigned int n)

    Performs channel calibration

    :param struct ad_sigma_delta \*sigma_delta:
        The sigma delta device

    :param const struct ad_sd_calib_data \*cb:
        Array of channels and calibration type to perform

    :param unsigned int n:
        Number of items in cb

.. _`ad_sd_calibrate_all.description`:

Description
-----------

Returns 0 on success, an error code otherwise.

.. _`ad_sigma_delta_single_conversion`:

ad_sigma_delta_single_conversion
================================

.. c:function:: int ad_sigma_delta_single_conversion(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, int *val)

    Performs a single data conversion

    :param struct iio_dev \*indio_dev:
        The IIO device

    :param const struct iio_chan_spec \*chan:
        The conversion is done for this channel

    :param int \*val:
        Pointer to the location where to store the read value

.. _`ad_sigma_delta_single_conversion.return`:

Return
------

0 on success, an error value otherwise.

.. _`ad_sd_validate_trigger`:

ad_sd_validate_trigger
======================

.. c:function:: int ad_sd_validate_trigger(struct iio_dev *indio_dev, struct iio_trigger *trig)

    validate_trigger callback for ad_sigma_delta devices

    :param struct iio_dev \*indio_dev:
        The IIO device

    :param struct iio_trigger \*trig:
        The new trigger

.. _`ad_sd_validate_trigger.return`:

Return
------

0 if the 'trig' matches the trigger registered by the ad_sigma_delta
device, -EINVAL otherwise.

.. _`ad_sd_setup_buffer_and_trigger`:

ad_sd_setup_buffer_and_trigger
==============================

.. c:function:: int ad_sd_setup_buffer_and_trigger(struct iio_dev *indio_dev)

    :param struct iio_dev \*indio_dev:
        The IIO device

.. _`ad_sd_cleanup_buffer_and_trigger`:

ad_sd_cleanup_buffer_and_trigger
================================

.. c:function:: void ad_sd_cleanup_buffer_and_trigger(struct iio_dev *indio_dev)

    :param struct iio_dev \*indio_dev:
        The IIO device

.. _`ad_sd_init`:

ad_sd_init
==========

.. c:function:: int ad_sd_init(struct ad_sigma_delta *sigma_delta, struct iio_dev *indio_dev, struct spi_device *spi, const struct ad_sigma_delta_info *info)

    Initializes a ad_sigma_delta struct

    :param struct ad_sigma_delta \*sigma_delta:
        The ad_sigma_delta device

    :param struct iio_dev \*indio_dev:
        The IIO device which the Sigma Delta device is used for

    :param struct spi_device \*spi:
        The SPI device for the ad_sigma_delta device

    :param const struct ad_sigma_delta_info \*info:
        Device specific callbacks and options

.. _`ad_sd_init.description`:

Description
-----------

This function needs to be called before any other operations are performed on
the ad_sigma_delta struct.

.. This file was automatic generated / don't edit.

