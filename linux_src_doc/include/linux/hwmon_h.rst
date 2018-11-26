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
        umode_t (*is_visible)(const void *drvdata, enum hwmon_sensor_types type, u32 attr, int channel);
        int (*read)(struct device *dev, enum hwmon_sensor_types type, u32 attr, int channel, long *val);
        int (*read_string)(struct device *dev, enum hwmon_sensor_types type, u32 attr, int channel, const char **str);
        int (*write)(struct device *dev, enum hwmon_sensor_types type, u32 attr, int channel, long val);
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
    Read callback for data attributes. Mandatory if readable
    data attributes are present.
    Parameters are:
    \ ``dev``\ :   Pointer to hardware monitoring device
    \ ``type``\ :  Sensor type
    \ ``attr``\ :  Sensor attribute
    \ ``channel``\ :
    Channel number
    \ ``val``\ :   Pointer to returned value
    The function returns 0 on success or a negative error number.

read_string
    Read callback for string attributes. Mandatory if string
    attributes are present.
    Parameters are:
    \ ``dev``\ :   Pointer to hardware monitoring device
    \ ``type``\ :  Sensor type
    \ ``attr``\ :  Sensor attribute
    \ ``channel``\ :
    Channel number
    \ ``str``\ :   Pointer to returned string
    The function returns 0 on success or a negative error number.

write
    Write callback for data attributes. Mandatory if writeable
    data attributes are present.
    Parameters are:
    \ ``dev``\ :   Pointer to hardware monitoring device
    \ ``type``\ :  Sensor type
    \ ``attr``\ :  Sensor attribute
    \ ``channel``\ :
    Channel number
    \ ``val``\ :   Value to write
    The function returns 0 on success or a negative error number.

.. _`hwmon_is_bad_char`:

hwmon_is_bad_char
=================

.. c:function:: bool hwmon_is_bad_char(const char ch)

    Is the char invalid in a hwmon name

    :param ch:
        the char to be considered
    :type ch: const char

.. _`hwmon_is_bad_char.description`:

Description
-----------

\ :c:func:`hwmon_is_bad_char`\  can be used to determine if the given character
may not be used in a hwmon name.

Returns true if the char is invalid, false otherwise.

.. This file was automatic generated / don't edit.

