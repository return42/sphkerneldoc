.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/hwmon.h

.. _`hwmon_ops`:

struct hwmon_ops
================

.. c:type:: struct hwmon_ops

    hwmon device operations

.. _`hwmon_ops.definition`:

Definition
----------

.. code-block:: c

    struct hwmon_ops {
        umode_t (*is_visible)(const void *drvdata, enum hwmon_sensor_types type,u32 attr, int channel);
        int (*read)(struct device *dev, enum hwmon_sensor_types type,u32 attr, int channel, long *val);
        int (*write)(struct device *dev, enum hwmon_sensor_types type,u32 attr, int channel, long val);
    }

.. _`hwmon_ops.members`:

Members
-------

is_visible
    Callback to return attribute visibility. Mandatory.
    Parameters are:
    \ ``const``\  void \*drvdata:
    Pointer to driver-private data structure passed
    as argument to \ :c:func:`hwmon_device_register_with_info`\ .
    \ ``type``\ :  Sensor type
    \ ``attr``\ :  Sensor attribute
    \ ``channel``\ :
    Channel number
    The function returns the file permissions.
    If the return value is 0, no attribute will be created.

read
    Read callback. Optional. If not provided, attributes
    will not be readable.
    Parameters are:
    \ ``dev``\ :   Pointer to hardware monitoring device
    \ ``type``\ :  Sensor type
    \ ``attr``\ :  Sensor attribute
    \ ``channel``\ :
    Channel number
    \ ``val``\ :   Pointer to returned value
    The function returns 0 on success or a negative error number.

write
    Write callback. Optional. If not provided, attributes
    will not be writable.
    Parameters are:
    \ ``dev``\ :   Pointer to hardware monitoring device
    \ ``type``\ :  Sensor type
    \ ``attr``\ :  Sensor attribute
    \ ``channel``\ :
    Channel number
    \ ``val``\ :   Value to write
    The function returns 0 on success or a negative error number.

.. This file was automatic generated / don't edit.
