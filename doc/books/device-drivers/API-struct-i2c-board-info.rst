.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-i2c-board-info:

=====================
struct i2c_board_info
=====================

*man struct i2c_board_info(9)*

*4.6.0-rc5*

template for device creation


Synopsis
========

.. code-block:: c

    struct i2c_board_info {
      char type[I2C_NAME_SIZE];
      unsigned short flags;
      unsigned short addr;
      void * platform_data;
      struct dev_archdata * archdata;
      struct device_node * of_node;
      struct fwnode_handle * fwnode;
      int irq;
    };


Members
=======

type[I2C_NAME_SIZE]
    chip type, to initialize i2c_client.name

flags
    to initialize i2c_client.flags

addr
    stored in i2c_client.addr

platform_data
    stored in i2c_client.dev.platform_data

archdata
    copied into i2c_client.dev.archdata

of_node
    pointer to OpenFirmware device node

fwnode
    device node supplied by the platform firmware

irq
    stored in i2c_client.irq


Description
===========

I2C doesn't actually support hardware probing, although controllers and
devices may be able to use I2C_SMBUS_QUICK to tell whether or not
there's a device at a given address. Drivers commonly need more
information than that, such as chip type, configuration, associated IRQ,
and so on.

i2c_board_info is used to build tables of information listing I2C
devices that are present. This information is used to grow the driver
model tree. For mainboards this is done statically using
``i2c_register_board_info``; bus numbers identify adapters that aren't
yet available. For add-on boards, ``i2c_new_device`` does this
dynamically with the adapter already known.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
