.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/adis.c

.. _`adis_read_reg`:

adis_read_reg
=============

.. c:function:: int adis_read_reg(struct adis *adis, unsigned int reg, unsigned int *val, unsigned int size)

    read 2 bytes from a 16-bit register

    :param struct adis \*adis:
        The adis device

    :param unsigned int reg:
        The address of the lower of the two registers

    :param unsigned int \*val:
        The value read back from the device

    :param unsigned int size:
        *undescribed*

.. _`adis_enable_irq`:

adis_enable_irq
===============

.. c:function:: int adis_enable_irq(struct adis *adis, bool enable)

    Enable or disable data ready IRQ

    :param struct adis \*adis:
        The adis device

    :param bool enable:
        Whether to enable the IRQ

.. _`adis_enable_irq.description`:

Description
-----------

Returns 0 on success, negative error code otherwise

.. _`adis_check_status`:

adis_check_status
=================

.. c:function:: int adis_check_status(struct adis *adis)

    Check the device for error conditions

    :param struct adis \*adis:
        The adis device

.. _`adis_check_status.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise

.. _`adis_reset`:

adis_reset
==========

.. c:function:: int adis_reset(struct adis *adis)

    Reset the device

    :param struct adis \*adis:
        The adis device

.. _`adis_reset.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise

.. _`adis_initial_startup`:

adis_initial_startup
====================

.. c:function:: int adis_initial_startup(struct adis *adis)

    Performs device self-test

    :param struct adis \*adis:
        The adis device

.. _`adis_initial_startup.description`:

Description
-----------

Returns 0 if the device is operational, a negative error code otherwise.

This function should be called early on in the device initialization sequence
to ensure that the device is in a sane and known state and that it is usable.

.. _`adis_single_conversion`:

adis_single_conversion
======================

.. c:function:: int adis_single_conversion(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, unsigned int error_mask, int *val)

    Performs a single sample conversion

    :param struct iio_dev \*indio_dev:
        The IIO device

    :param const struct iio_chan_spec \*chan:
        The IIO channel

    :param unsigned int error_mask:
        Mask for the error bit

    :param int \*val:
        Result of the conversion

.. _`adis_single_conversion.description`:

Description
-----------

Returns IIO_VAL_INT on success, a negative error code otherwise.

The function performs a single conversion on a given channel and post
processes the value accordingly to the channel spec. If a error_mask is given
the function will check if the mask is set in the returned raw value. If it
is set the function will perform a self-check. If the device does not report
a error bit in the channels raw value set error_mask to 0.

.. _`adis_init`:

adis_init
=========

.. c:function:: int adis_init(struct adis *adis, struct iio_dev *indio_dev, struct spi_device *spi, const struct adis_data *data)

    Initialize adis device structure

    :param struct adis \*adis:
        The adis device

    :param struct iio_dev \*indio_dev:
        The iio device

    :param struct spi_device \*spi:
        The spi device

    :param const struct adis_data \*data:
        Chip specific data

.. _`adis_init.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise.

This function must be called, before any other adis helper function may be
called.

.. This file was automatic generated / don't edit.

