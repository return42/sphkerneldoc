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
        struct cmd;
        struct device *dev;
        struct mlxsw_core *core;
        struct mlxsw_bus_info bus_info;
    }

.. _`mlxsw_i2c.members`:

Members
-------

cmd
    *undescribed*

cmd.mb_size_in
    input mailbox size;

cmd.mb_off_in
    input mailbox offset in register space;

cmd.mb_size_out
    output mailbox size;

cmd.mb_off_out
    output mailbox offset in register space;

cmd.lock
    command execution lock;

dev
    I2C device;

core
    switch core pointer;

bus_info
    bus info block;

.. This file was automatic generated / don't edit.

