.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/mlxcpld-hotplug.h

.. _`mlxcpld_hotplug_device`:

struct mlxcpld_hotplug_device
=============================

.. c:type:: struct mlxcpld_hotplug_device

    I2C device data:

.. _`mlxcpld_hotplug_device.definition`:

Definition
----------

.. code-block:: c

    struct mlxcpld_hotplug_device {
        struct i2c_adapter *adapter;
        struct i2c_client *client;
        struct i2c_board_info brdinfo;
        u16 bus;
    }

.. _`mlxcpld_hotplug_device.members`:

Members
-------

adapter
    I2C device adapter;

client
    I2C device client;

brdinfo
    device board information;

bus
    I2C bus, where device is attached;

.. _`mlxcpld_hotplug_device.description`:

Description
-----------

Structure represents I2C hotplug device static data (board topology) and
dynamic data (related kernel objects handles).

.. _`mlxcpld_hotplug_platform_data`:

struct mlxcpld_hotplug_platform_data
====================================

.. c:type:: struct mlxcpld_hotplug_platform_data

    device platform data:

.. _`mlxcpld_hotplug_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxcpld_hotplug_platform_data {
        u16 top_aggr_offset;
        u8 top_aggr_mask;
        u8 top_aggr_psu_mask;
        u16 psu_reg_offset;
        u8 psu_mask;
        u8 psu_count;
        struct mlxcpld_hotplug_device *psu;
        u8 top_aggr_pwr_mask;
        u16 pwr_reg_offset;
        u8 pwr_mask;
        u8 pwr_count;
        struct mlxcpld_hotplug_device *pwr;
        u8 top_aggr_fan_mask;
        u16 fan_reg_offset;
        u8 fan_mask;
        u8 fan_count;
        struct mlxcpld_hotplug_device *fan;
    }

.. _`mlxcpld_hotplug_platform_data.members`:

Members
-------

top_aggr_offset
    offset of top aggregation interrupt register;

top_aggr_mask
    top aggregation interrupt common mask;

top_aggr_psu_mask
    top aggregation interrupt PSU mask;

psu_reg_offset
    offset of PSU interrupt register;

psu_mask
    PSU interrupt mask;

psu_count
    number of equipped replaceable PSUs;

psu
    pointer to PSU devices data array;

top_aggr_pwr_mask
    top aggregation interrupt power mask;

pwr_reg_offset
    offset of power interrupt register

pwr_mask
    power interrupt mask;

pwr_count
    number of power sources;

pwr
    pointer to power devices data array;

top_aggr_fan_mask
    top aggregation interrupt FAN mask;

fan_reg_offset
    offset of FAN interrupt register;

fan_mask
    FAN interrupt mask;

fan_count
    number of equipped replaceable FANs;

fan
    pointer to FAN devices data array;

.. _`mlxcpld_hotplug_platform_data.description`:

Description
-----------

Structure represents board platform data, related to system hotplug events,
like FAN, PSU, power cable insertion and removing. This data provides the
number of hot-pluggable devices and hardware description for event handling.

.. This file was automatic generated / don't edit.

