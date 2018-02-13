.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/mlxreg.h

.. _`mlxreg_hotplug_device`:

struct mlxreg_hotplug_device
============================

.. c:type:: struct mlxreg_hotplug_device

    I2C device data:

.. _`mlxreg_hotplug_device.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_hotplug_device {
        struct i2c_adapter *adapter;
        struct i2c_client *client;
        struct i2c_board_info *brdinfo;
        int nr;
    }

.. _`mlxreg_hotplug_device.members`:

Members
-------

adapter
    I2C device adapter;

client
    I2C device client;

brdinfo
    device board information;

nr
    I2C device adapter number, to which device is to be attached;

.. _`mlxreg_hotplug_device.description`:

Description
-----------

Structure represents I2C hotplug device static data (board topology) and
dynamic data (related kernel objects handles).

.. _`mlxreg_core_data`:

struct mlxreg_core_data
=======================

.. c:type:: struct mlxreg_core_data

    attributes control data:

.. _`mlxreg_core_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_core_data {
        char label[MLXREG_CORE_LABEL_MAX_SIZE];
        u32 reg;
        u32 mask;
        u32 bit;
        umode_t mode;
        struct device_node *np;
        struct mlxreg_hotplug_device hpdev;
        u8 health_cntr;
        bool attached;
    }

.. _`mlxreg_core_data.members`:

Members
-------

label
    attribute register offset;

reg
    attribute register;

mask
    attribute access mask;

bit
    attribute effective bit;
    \ ``np``\  - pointer to node platform associated with attribute;
    \ ``hpdev``\  - hotplug device data;

mode
    access mode;

np
    *undescribed*

hpdev
    *undescribed*

health_cntr
    dynamic device health indication counter;

attached
    true if device has been attached after good health indication;

.. _`mlxreg_core_item`:

struct mlxreg_core_item
=======================

.. c:type:: struct mlxreg_core_item

    same type components controlled by the driver:

.. _`mlxreg_core_item.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_core_item {
        struct mlxreg_core_data *data;
        u32 aggr_mask;
        u32 reg;
        u32 mask;
        u32 cache;
        u8 count;
        u8 ind;
        u8 inversed;
        u8 health;
    }

.. _`mlxreg_core_item.members`:

Members
-------

data
    component data;

aggr_mask
    group aggregation mask;

reg
    group interrupt status register;

mask
    group interrupt mask;

cache
    last status value for elements fro the same group;

count
    number of available elements in the group;

ind
    element's index inside the group;

inversed
    if 0: 0 for signal status is OK, if 1 - 1 is OK;

health
    true if device has health indication, false in other case;

.. _`mlxreg_core_platform_data`:

struct mlxreg_core_platform_data
================================

.. c:type:: struct mlxreg_core_platform_data

    platform data:

.. _`mlxreg_core_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_core_platform_data {
        struct mlxreg_core_data *data;
        void *regmap;
        int counter;
    }

.. _`mlxreg_core_platform_data.members`:

Members
-------

data
    *undescribed*

regmap
    register map of parent device;

counter
    number of led instances;

.. _`mlxreg_core_hotplug_platform_data`:

struct mlxreg_core_hotplug_platform_data
========================================

.. c:type:: struct mlxreg_core_hotplug_platform_data

    hotplug platform data:

.. _`mlxreg_core_hotplug_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_core_hotplug_platform_data {
        struct mlxreg_core_item *items;
        int irq;
        void *regmap;
        int counter;
        u32 cell;
        u32 mask;
        u32 cell_low;
        u32 mask_low;
    }

.. _`mlxreg_core_hotplug_platform_data.members`:

Members
-------

items
    same type components with the hotplug capability;

irq
    platform interrupt number;

regmap
    register map of parent device;

counter
    number of the components with the hotplug capability;

cell
    location of top aggregation interrupt register;

mask
    top aggregation interrupt common mask;

cell_low
    location of low aggregation interrupt register;

mask_low
    low aggregation interrupt common mask;

.. This file was automatic generated / don't edit.

