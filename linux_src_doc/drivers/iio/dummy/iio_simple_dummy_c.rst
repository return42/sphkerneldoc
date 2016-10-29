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

    :param struct iio_dev \*indio_dev:
        the struct iio_dev associated with this device instance

    :param struct iio_chan_spec const \*chan:
        the channel whose data is to be read

    :param int \*val:
        first element of returned value (typically INT)

    :param int \*val2:
        second element of returned value (typically MICRO)

    :param long mask:
        what we actually want to read as per the info_mask\_\*
        in iio_chan_spec.

.. _`iio_dummy_write_raw`:

iio_dummy_write_raw
===================

.. c:function:: int iio_dummy_write_raw(struct iio_dev *indio_dev, struct iio_chan_spec const *chan, int val, int val2, long mask)

    data write function.

    :param struct iio_dev \*indio_dev:
        the struct iio_dev associated with this device instance

    :param struct iio_chan_spec const \*chan:
        the channel whose data is to be written

    :param int val:
        first element of value to set (typically INT)

    :param int val2:
        second element of value to set (typically MICRO)

    :param long mask:
        what we actually want to write as per the info_mask\_\*
        in iio_chan_spec.

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

    :param struct iio_dev \*indio_dev:
        the iio device structure

.. _`iio_dummy_init_device.description`:

Description
-----------

Most drivers have one of these to set up default values,
reset the device to known state etc.

.. _`iio_dummy_probe`:

iio_dummy_probe
===============

.. c:function:: int iio_dummy_probe(int index)

    device instance probe

    :param int index:
        an id number for this instance.

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

.. c:function:: void iio_dummy_remove(int index)

    device instance removal function

    :param int index:
        device index.

.. _`iio_dummy_remove.description`:

Description
-----------

Parameters follow those of iio_dummy_probe for buses.

.. _`iio_dummy_init`:

iio_dummy_init
==============

.. c:function:: int iio_dummy_init( void)

    device driver registration

    :param  void:
        no arguments

.. _`iio_dummy_init.description`:

Description
-----------

Varies depending on bus type of the device. As there is no device
here, call probe directly. For information on device registration

.. _`iio_dummy_init.i2c`:

i2c
---

Documentation/i2c/writing-clients

.. _`iio_dummy_init.spi`:

spi
---

Documentation/spi/spi-summary

.. _`iio_dummy_exit`:

iio_dummy_exit
==============

.. c:function:: __exit void iio_dummy_exit( void)

    device driver removal

    :param  void:
        no arguments

.. _`iio_dummy_exit.description`:

Description
-----------

Varies depending on bus type of the device.
As there is no device here, call remove directly.

.. This file was automatic generated / don't edit.
