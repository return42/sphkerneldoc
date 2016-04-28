.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-driver:

=================
struct rio_driver
=================

*man struct rio_driver(9)*

*4.6.0-rc5*

RIO driver info


Synopsis
========

.. code-block:: c

    struct rio_driver {
      struct list_head node;
      char * name;
      const struct rio_device_id * id_table;
      int (* probe) (struct rio_dev * dev, const struct rio_device_id * id);
      void (* remove) (struct rio_dev * dev);
      void (* shutdown) (struct rio_dev *dev);
      int (* suspend) (struct rio_dev * dev, u32 state);
      int (* resume) (struct rio_dev * dev);
      int (* enable_wake) (struct rio_dev * dev, u32 state, int enable);
      struct device_driver driver;
    };


Members
=======

node
    Node in list of drivers

name
    RIO driver name

id_table
    RIO device ids to be associated with this driver

probe
    RIO device inserted

remove
    RIO device removed

shutdown
    shutdown notification callback

suspend
    RIO device suspended

resume
    RIO device awakened

enable_wake
    RIO device enable wake event

driver
    LDM driver struct


Description
===========

Provides info on a RIO device driver for insertion/removal and power
management purposes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
