.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/st_sensors/st_sensors_core.c

.. _`st_sensors_of_name_probe`:

st_sensors_of_name_probe
========================

.. c:function:: void st_sensors_of_name_probe(struct device *dev, const struct of_device_id *match, char *name, int len)

    device tree probe for ST sensor name

    :param dev:
        driver model representation of the device.
    :type dev: struct device \*

    :param match:
        the OF match table for the device, containing compatible strings
        but also a .data field with the corresponding internal kernel name
        used by this sensor.
    :type match: const struct of_device_id \*

    :param name:
        device name buffer reference.
    :type name: char \*

    :param len:
        device name buffer length.
    :type len: int

.. _`st_sensors_of_name_probe.description`:

Description
-----------

In effect this function matches a compatible string to an internal kernel
name for a certain sensor device, so that the rest of the autodetection can
rely on that name from this point on. I2C/SPI devices will be renamed
to match the internal kernel convention.

.. This file was automatic generated / don't edit.

