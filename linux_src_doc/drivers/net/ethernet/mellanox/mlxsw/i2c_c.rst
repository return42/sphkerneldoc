.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlxsw/i2c.c

.. _`mlxsw_i2c`:

struct mlxsw_i2c
================

.. c:type:: struct mlxsw_i2c

    device private data:

.. _`mlxsw_i2c.definition`:

Definition
----------

.. code-block:: c

    struct mlxsw_i2c {
        struct {
            u32 mb_size_in;
            u32 mb_off_in;
            u32 mb_size_out;
            u32 mb_off_out;
            struct mutex lock;
        } cmd;
        struct device *dev;
        struct mlxsw_core *core;
        struct mlxsw_bus_info bus_info;
    }

.. _`mlxsw_i2c.members`:

Members
-------

mb_size_in
    *undescribed*

mb_off_in
    *undescribed*

mb_size_out
    *undescribed*

mb_off_out
    *undescribed*

lock
    *undescribed*

md
    *undescribed*

dev
    I2C device;

core
    switch core pointer;

bus_info
    bus info block;

.. This file was automatic generated / don't edit.

