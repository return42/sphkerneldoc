.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/max197.c

.. _`max197_data`:

struct max197_data
==================

.. c:type:: struct max197_data

    device instance specific data

.. _`max197_data.definition`:

Definition
----------

.. code-block:: c

    struct max197_data {
        struct max197_platform_data *pdata;
        struct device *hwmon_dev;
        struct mutex lock;
        int limit;
        bool scale;
        u8 ctrl_bytes[MAX197_NUM_CH];
    }

.. _`max197_data.members`:

Members
-------

pdata
    Platform data.

hwmon_dev
    The hwmon device.

lock
    Read/Write mutex.

limit
    Max range value (10V for MAX197, 4V for MAX199).

scale
    Need to scale.

ctrl_bytes
    Channels control byte.

.. This file was automatic generated / don't edit.

