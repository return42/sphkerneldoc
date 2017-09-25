.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/mlxcpld-hotplug.c

.. _`mlxcpld_hotplug_attr_type`:

enum mlxcpld_hotplug_attr_type
==============================

.. c:type:: enum mlxcpld_hotplug_attr_type

    sysfs attributes for hotplug events:

.. _`mlxcpld_hotplug_attr_type.definition`:

Definition
----------

.. code-block:: c

    enum mlxcpld_hotplug_attr_type {
        MLXCPLD_HOTPLUG_ATTR_TYPE_PSU,
        MLXCPLD_HOTPLUG_ATTR_TYPE_PWR,
        MLXCPLD_HOTPLUG_ATTR_TYPE_FAN
    };

.. _`mlxcpld_hotplug_attr_type.constants`:

Constants
---------

MLXCPLD_HOTPLUG_ATTR_TYPE_PSU
    power supply unit attribute;

MLXCPLD_HOTPLUG_ATTR_TYPE_PWR
    power cable attribute;

MLXCPLD_HOTPLUG_ATTR_TYPE_FAN
    FAN drawer attribute;

.. _`mlxcpld_hotplug_priv_data`:

struct mlxcpld_hotplug_priv_data
================================

.. c:type:: struct mlxcpld_hotplug_priv_data

    platform private data:

.. _`mlxcpld_hotplug_priv_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxcpld_hotplug_priv_data {
        int irq;
        struct platform_device *pdev;
        struct mlxcpld_hotplug_platform_data *plat;
        struct device *hwmon;
        struct attribute *mlxcpld_hotplug_attr[MLXCPLD_HOTPLUG_ATTRS_NUM + 1];
        struct sensor_device_attribute_2 mlxcpld_hotplug_dev_attr[MLXCPLD_HOTPLUG_ATTRS_NUM];
        struct attribute_group group;
        const struct attribute_group *groups[2];
        struct delayed_work dwork;
        spinlock_t lock;
        u8 aggr_cache;
        u8 psu_cache;
        u8 pwr_cache;
        u8 fan_cache;
    }

.. _`mlxcpld_hotplug_priv_data.members`:

Members
-------

irq
    platform interrupt number;

pdev
    platform device;

plat
    platform data;

hwmon
    hwmon device;

mlxcpld_hotplug_attr
    sysfs attributes array;

mlxcpld_hotplug_dev_attr
    sysfs sensor device attribute array;

group
    sysfs attribute group;

groups
    list of sysfs attribute group for hwmon registration;

dwork
    delayed work template;

lock
    spin lock;

aggr_cache
    last value of aggregation register status;

psu_cache
    last value of PSU register status;

pwr_cache
    last value of power register status;

fan_cache
    last value of FAN register status;

.. This file was automatic generated / don't edit.

