.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/sht21.c

.. _`sht21`:

struct sht21
============

.. c:type:: struct sht21

    SHT21 device specific data

.. _`sht21.definition`:

Definition
----------

.. code-block:: c

    struct sht21 {
        struct i2c_client *client;
        struct mutex lock;
        char valid;
        unsigned long last_update;
        int temperature;
        int humidity;
    }

.. _`sht21.members`:

Members
-------

client
    *undescribed*

lock
    mutex to protect measurement values

valid
    only 0 before first measurement is taken

last_update
    time of last update (jiffies)

temperature
    cached temperature measurement value

humidity
    cached humidity measurement value

.. _`sht21_temp_ticks_to_millicelsius`:

sht21_temp_ticks_to_millicelsius
================================

.. c:function:: int sht21_temp_ticks_to_millicelsius(int ticks)

    convert raw temperature ticks to milli celsius

    :param int ticks:
        temperature ticks value received from sensor

.. _`sht21_rh_ticks_to_per_cent_mille`:

sht21_rh_ticks_to_per_cent_mille
================================

.. c:function:: int sht21_rh_ticks_to_per_cent_mille(int ticks)

    convert raw humidity ticks to one-thousandths of a percent relative humidity

    :param int ticks:
        humidity ticks value received from sensor

.. _`sht21_update_measurements`:

sht21_update_measurements
=========================

.. c:function:: int sht21_update_measurements(struct device *dev)

    get updated measurements from device

    :param struct device \*dev:
        device

.. _`sht21_update_measurements.description`:

Description
-----------

Returns 0 on success, else negative errno.

.. _`sht21_show_temperature`:

sht21_show_temperature
======================

.. c:function:: ssize_t sht21_show_temperature(struct device *dev, struct device_attribute *attr, char *buf)

    show temperature measurement value in sysfs

    :param struct device \*dev:
        device

    :param struct device_attribute \*attr:
        device attribute

    :param char \*buf:
        sysfs buffer (PAGE_SIZE) where measurement values are written to

.. _`sht21_show_temperature.description`:

Description
-----------

Will be called on read access to temp1_input sysfs attribute.
Returns number of bytes written into buffer, negative errno on error.

.. _`sht21_show_humidity`:

sht21_show_humidity
===================

.. c:function:: ssize_t sht21_show_humidity(struct device *dev, struct device_attribute *attr, char *buf)

    show humidity measurement value in sysfs

    :param struct device \*dev:
        device

    :param struct device_attribute \*attr:
        device attribute

    :param char \*buf:
        sysfs buffer (PAGE_SIZE) where measurement values are written to

.. _`sht21_show_humidity.description`:

Description
-----------

Will be called on read access to humidity1_input sysfs attribute.
Returns number of bytes written into buffer, negative errno on error.

.. This file was automatic generated / don't edit.
