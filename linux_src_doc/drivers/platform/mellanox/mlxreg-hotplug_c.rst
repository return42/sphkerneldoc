.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/mellanox/mlxreg-hotplug.c

.. _`mlxreg_hotplug_priv_data`:

struct mlxreg_hotplug_priv_data
===============================

.. c:type:: struct mlxreg_hotplug_priv_data

    platform private data:

.. _`mlxreg_hotplug_priv_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_hotplug_priv_data {
        int irq;
        struct device *dev;
        struct platform_device *pdev;
        struct mlxreg_hotplug_platform_data *plat;
        struct regmap *regmap;
        struct delayed_work dwork_irq;
        struct delayed_work dwork;
        spinlock_t lock;
        struct device *hwmon;
        struct attribute *mlxreg_hotplug_attr[MLXREG_HOTPLUG_ATTRS_MAX + 1];
        struct sensor_device_attribute_2 mlxreg_hotplug_dev_attr[MLXREG_HOTPLUG_ATTRS_MAX];
        struct attribute_group group;
        const struct attribute_group *groups[2];
        u32 cell;
        u32 mask;
        u32 aggr_cache;
        bool after_probe;
    }

.. _`mlxreg_hotplug_priv_data.members`:

Members
-------

irq
    platform device interrupt number;

dev
    *undescribed*

pdev
    platform device;

plat
    platform data;

regmap
    *undescribed*

dwork_irq
    *undescribed*

dwork
    delayed work template;

lock
    spin lock;

hwmon
    hwmon device;

mlxreg_hotplug_attr
    sysfs attributes array;

mlxreg_hotplug_dev_attr
    sysfs sensor device attribute array;

group
    sysfs attribute group;

groups
    list of sysfs attribute group for hwmon registration;

cell
    location of top aggregation interrupt register;

mask
    top aggregation interrupt common mask;

aggr_cache
    last value of aggregation register status;

after_probe
    *undescribed*

.. This file was automatic generated / don't edit.

