.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dummy/iio_simple_dummy.c

.. _`iio_dummy_accel_calibscale`:

struct iio_dummy_accel_calibscale
=================================

.. c:type:: struct iio_dummy_accel_calibscale

    realworld to register mapping

.. _`iio_dummy_accel_calibscale.definition`:

Definition
----------

.. code-block:: c

    struct iio_dummy_accel_calibscale {
        int val;
        int val2;
        int regval;
    }

.. _`iio_dummy_accel_calibscale.members`:

Members
-------

val
    first value in read_raw - here integer part.

val2
    second value in read_raw etc - here micro part.

regval
    register value - magic device specific numbers.

.. _`iio_dummy_read_raw`:

iio_dummy_read_raw
==================

.. c:function:: int iio_dummy_read_raw(struct iio_dev *indio_dev, struct iio_chan_spec const *chan, int *val, int *val2, long mask)

    data read function.

    :param indio_dev:
        the struct iio_dev associated with this device instance
    :type indio_dev: struct iio_dev \*

    :param chan:
        the channel whose data is to be read
    :type chan: struct iio_chan_spec const \*

    :param val:
        first element of returned value (typically INT)
    :type val: int \*

    :param val2:
        second element of returned value (typically MICRO)
    :type val2: int \*

    :param mask:
        what we actually want to read as per the info_mask\_\*
        in iio_chan_spec.
    :type mask: long

.. _`iio_dummy_write_raw`:

iio_dummy_write_raw
===================

.. c:function:: int iio_dummy_write_raw(struct iio_dev *indio_dev, struct iio_chan_spec const *chan, int val, int val2, long mask)

    data write function.

    :param indio_dev:
        the struct iio_dev associated with this device instance
    :type indio_dev: struct iio_dev \*

    :param chan:
        the channel whose data is to be written
    :type chan: struct iio_chan_spec const \*

    :param val:
        first element of value to set (typically INT)
    :type val: int

    :param val2:
        second element of value to set (typically MICRO)
    :type val2: int

    :param mask:
        what we actually want to write as per the info_mask\_\*
        in iio_chan_spec.
    :type mask: long

.. _`iio_dummy_write_raw.description`:

Description
-----------

Note that all raw writes are assumed IIO_VAL_INT and info mask elements
are assumed to be IIO_INT_PLUS_MICRO unless the callback write_raw_get_fmt
in struct iio_info is provided by the driver.

.. _`iio_dummy_init_device`:

iio_dummy_init_device
=====================

.. c:function:: int iio_dummy_init_device(struct iio_dev *indio_dev)

    device instance specific init

    :param indio_dev:
        the iio device structure
    :type indio_dev: struct iio_dev \*

.. _`iio_dummy_init_device.description`:

Description
-----------

Most drivers have one of these to set up default values,
reset the device to known state etc.

.. _`iio_dummy_probe`:

iio_dummy_probe
===============

.. c:function:: struct iio_sw_device *iio_dummy_probe(const char *name)

    device instance probe

    :param name:
        *undescribed*
    :type name: const char \*

.. _`iio_dummy_probe.description`:

Description
-----------

Arguments are bus type specific.

.. _`iio_dummy_probe.i2c`:

I2C
---

iio_dummy_probe(struct i2c_client \*client,
const struct i2c_device_id \*id)

.. _`iio_dummy_probe.spi`:

SPI
---

iio_dummy_probe(struct spi_device \*spi)

.. _`iio_dummy_remove`:

iio_dummy_remove
================

.. c:function:: int iio_dummy_remove(struct iio_sw_device *swd)

    device instance removal function

    :param swd:
        pointer to software IIO device abstraction
    :type swd: struct iio_sw_device \*

.. _`iio_dummy_remove.description`:

Description
-----------

Parameters follow those of iio_dummy_probe for buses.

.. This file was automatic generated / don't edit.

