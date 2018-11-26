.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/s3c-hwmon.c

.. _`s3c_hwmon`:

struct s3c_hwmon
================

.. c:type:: struct s3c_hwmon

    ADC hwmon client information

.. _`s3c_hwmon.definition`:

Definition
----------

.. code-block:: c

    struct s3c_hwmon {
        struct mutex lock;
        struct s3c_adc_client *client;
        struct device *hwmon_dev;
        struct s3c_hwmon_attr attrs[8];
    }

.. _`s3c_hwmon.members`:

Members
-------

lock
    Access lock to serialise the conversions.

client
    The client we registered with the S3C ADC core.

hwmon_dev
    The hwmon device we created.

attrs
    *undescribed*

.. _`s3c_hwmon_read_ch`:

s3c_hwmon_read_ch
=================

.. c:function:: int s3c_hwmon_read_ch(struct device *dev, struct s3c_hwmon *hwmon, int channel)

    read a value from a given adc channel.

    :param dev:
        The device.
    :type dev: struct device \*

    :param hwmon:
        Our state.
    :type hwmon: struct s3c_hwmon \*

    :param channel:
        The channel we're reading from.
    :type channel: int

.. _`s3c_hwmon_read_ch.description`:

Description
-----------

Read a value from the \ ``channel``\  with the proper locking and sleep until
either the read completes or we timeout awaiting the ADC core to get
back to us.

.. _`s3c_hwmon_show_raw`:

s3c_hwmon_show_raw
==================

.. c:function:: ssize_t s3c_hwmon_show_raw(struct device *dev, struct device_attribute *attr, char *buf)

    show a conversion from the raw channel number.

    :param dev:
        The device that the attribute belongs to.
    :type dev: struct device \*

    :param attr:
        The attribute being read.
    :type attr: struct device_attribute \*

    :param buf:
        The result buffer.
    :type buf: char \*

.. _`s3c_hwmon_show_raw.description`:

Description
-----------

This show deals with the raw attribute, registered for each possible
ADC channel. This does a conversion and returns the raw (un-scaled)
value returned from the hardware.

.. _`s3c_hwmon_ch_show`:

s3c_hwmon_ch_show
=================

.. c:function:: ssize_t s3c_hwmon_ch_show(struct device *dev, struct device_attribute *attr, char *buf)

    show value of a given channel

    :param dev:
        The device that the attribute belongs to.
    :type dev: struct device \*

    :param attr:
        The attribute being read.
    :type attr: struct device_attribute \*

    :param buf:
        The result buffer.
    :type buf: char \*

.. _`s3c_hwmon_ch_show.description`:

Description
-----------

Read a value from the ADC and scale it before returning it to the
caller. The scale factor is gained from the channel configuration
passed via the platform data when the device was registered.

.. _`s3c_hwmon_label_show`:

s3c_hwmon_label_show
====================

.. c:function:: ssize_t s3c_hwmon_label_show(struct device *dev, struct device_attribute *attr, char *buf)

    show label name of the given channel.

    :param dev:
        The device that the attribute belongs to.
    :type dev: struct device \*

    :param attr:
        The attribute being read.
    :type attr: struct device_attribute \*

    :param buf:
        The result buffer.
    :type buf: char \*

.. _`s3c_hwmon_label_show.description`:

Description
-----------

Return the label name of a given channel

.. _`s3c_hwmon_create_attr`:

s3c_hwmon_create_attr
=====================

.. c:function:: int s3c_hwmon_create_attr(struct device *dev, struct s3c_hwmon_chcfg *cfg, struct s3c_hwmon_attr *attrs, int channel)

    create hwmon attribute for given channel.

    :param dev:
        The device to create the attribute on.
    :type dev: struct device \*

    :param cfg:
        The channel configuration passed from the platform data.
    :type cfg: struct s3c_hwmon_chcfg \*

    :param attrs:
        *undescribed*
    :type attrs: struct s3c_hwmon_attr \*

    :param channel:
        The ADC channel number to process.
    :type channel: int

.. _`s3c_hwmon_create_attr.description`:

Description
-----------

Create the scaled attribute for use with hwmon from the specified
platform data in \ ``pdata``\ . The sysfs entry is handled by the routine
\ :c:func:`s3c_hwmon_ch_show`\ .

The attribute name is taken from the configuration data if present
otherwise the name is taken by concatenating in\_ with the channel
number.

.. _`s3c_hwmon_probe`:

s3c_hwmon_probe
===============

.. c:function:: int s3c_hwmon_probe(struct platform_device *dev)

    device probe entry.

    :param dev:
        The device being probed.
    :type dev: struct platform_device \*

.. This file was automatic generated / don't edit.

