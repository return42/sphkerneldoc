.. -*- coding: utf-8; mode: rst -*-

================
st_sensors_i2c.c
================


.. _`st_sensors_of_i2c_probe`:

st_sensors_of_i2c_probe
=======================

.. c:function:: void st_sensors_of_i2c_probe (struct i2c_client *client, const struct of_device_id *match)

    device tree probe for ST I2C sensors

    :param struct i2c_client \*client:
        the I2C client device for the sensor

    :param const struct of_device_id \*match:
        the OF match table for the device, containing compatible strings
        but also a .data field with the corresponding internal kernel name
        used by this sensor.



.. _`st_sensors_of_i2c_probe.description`:

Description
-----------

In effect this function matches a compatible string to an internal kernel
name for a certain sensor device, so that the rest of the autodetection can
rely on that name from this point on. I2C client devices will be renamed
to match the internal kernel convention.

