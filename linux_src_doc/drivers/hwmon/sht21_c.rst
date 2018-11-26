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
        unsigned long last_update;
        int temperature;
        int humidity;
        char valid;
        char eic[18];
    }

.. _`sht21.members`:

Members
-------

client
    I2C client device

lock
    mutex to protect measurement values

last_update
    time of last update (jiffies)

temperature
    cached temperature measurement value

humidity
    cached humidity measurement value

valid
    only 0 before first measurement is taken

eic
    cached electronic identification code text

.. _`sht21_temp_ticks_to_millicelsius`:

sht21_temp_ticks_to_millicelsius
================================

.. c:function:: int sht21_temp_ticks_to_millicelsius(int ticks)

    convert raw temperature ticks to milli celsius

    :param ticks:
        temperature ticks value received from sensor
    :type ticks: int

.. _`sht21_rh_ticks_to_per_cent_mille`:

sht21_rh_ticks_to_per_cent_mille
================================

.. c:function:: int sht21_rh_ticks_to_per_cent_mille(int ticks)

    convert raw humidity ticks to one-thousandths of a percent relative humidity

    :param ticks:
        humidity ticks value received from sensor
    :type ticks: int

.. _`sht21_update_measurements`:

sht21_update_measurements
=========================

.. c:function:: int sht21_update_measurements(struct device *dev)

    get updated measurements from device

    :param dev:
        device
    :type dev: struct device \*

.. _`sht21_update_measurements.description`:

Description
-----------

Returns 0 on success, else negative errno.

.. _`sht21_show_temperature`:

sht21_show_temperature
======================

.. c:function:: ssize_t sht21_show_temperature(struct device *dev, struct device_attribute *attr, char *buf)

    show temperature measurement value in sysfs

    :param dev:
        device
    :type dev: struct device \*

    :param attr:
        device attribute
    :type attr: struct device_attribute \*

    :param buf:
        sysfs buffer (PAGE_SIZE) where measurement values are written to
    :type buf: char \*

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

    :param dev:
        device
    :type dev: struct device \*

    :param attr:
        device attribute
    :type attr: struct device_attribute \*

    :param buf:
        sysfs buffer (PAGE_SIZE) where measurement values are written to
    :type buf: char \*

.. _`sht21_show_humidity.description`:

Description
-----------

Will be called on read access to humidity1_input sysfs attribute.
Returns number of bytes written into buffer, negative errno on error.

.. _`eic_show`:

eic_show
========

.. c:function:: ssize_t eic_show(struct device *dev, struct device_attribute *attr, char *buf)

    show Electronic Identification Code in sysfs

    :param dev:
        device
    :type dev: struct device \*

    :param attr:
        device attribute
    :type attr: struct device_attribute \*

    :param buf:
        sysfs buffer (PAGE_SIZE) where EIC is written
    :type buf: char \*

.. _`eic_show.description`:

Description
-----------

Will be called on read access to eic sysfs attribute.
Returns number of bytes written into buffer, negative errno on error.

.. This file was automatic generated / don't edit.

