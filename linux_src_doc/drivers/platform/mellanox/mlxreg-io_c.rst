.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/mellanox/mlxreg-io.c

.. _`mlxreg_io_priv_data`:

struct mlxreg_io_priv_data
==========================

.. c:type:: struct mlxreg_io_priv_data

    driver's private data:

.. _`mlxreg_io_priv_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_io_priv_data {
        struct platform_device *pdev;
        struct mlxreg_core_platform_data *pdata;
        struct device *hwmon;
        struct attribute *mlxreg_io_attr[MLXREG_IO_ATT_NUM + 1];
        struct sensor_device_attribute mlxreg_io_dev_attr[MLXREG_IO_ATT_NUM];
        struct attribute_group group;
        const struct attribute_group *groups[2];
    }

.. _`mlxreg_io_priv_data.members`:

Members
-------

pdev
    platform device;

pdata
    platform data;

hwmon
    hwmon device;

mlxreg_io_attr
    sysfs attributes array;

mlxreg_io_dev_attr
    sysfs sensor device attribute array;

group
    sysfs attribute group;

groups
    list of sysfs attribute group for hwmon registration;

.. This file was automatic generated / don't edit.

