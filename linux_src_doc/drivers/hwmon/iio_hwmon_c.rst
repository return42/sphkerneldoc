.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/iio_hwmon.c

.. _`iio_hwmon_state`:

struct iio_hwmon_state
======================

.. c:type:: struct iio_hwmon_state

    device instance state

.. _`iio_hwmon_state.definition`:

Definition
----------

.. code-block:: c

    struct iio_hwmon_state {
        struct iio_channel *channels;
        int num_channels;
        struct device *hwmon_dev;
        struct attribute_group attr_group;
        const struct attribute_group *groups[2];
        struct attribute **attrs;
    }

.. _`iio_hwmon_state.members`:

Members
-------

channels
    filled with array of channels from iio

num_channels
    number of channels in channels (saves counting twice)

hwmon_dev
    associated hwmon device

attr_group
    the group of attributes

groups
    null terminated array of attribute groups

attrs
    null terminated array of attribute pointers.

.. This file was automatic generated / don't edit.

