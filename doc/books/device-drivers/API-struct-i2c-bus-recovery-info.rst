.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-i2c-bus-recovery-info:

============================
struct i2c_bus_recovery_info
============================

*man struct i2c_bus_recovery_info(9)*

*4.6.0-rc5*

I2C bus recovery information


Synopsis
========

.. code-block:: c

    struct i2c_bus_recovery_info {
      int (* recover_bus) (struct i2c_adapter *);
      int (* get_scl) (struct i2c_adapter *);
      void (* set_scl) (struct i2c_adapter *, int val);
      int (* get_sda) (struct i2c_adapter *);
      void (* prepare_recovery) (struct i2c_adapter *);
      void (* unprepare_recovery) (struct i2c_adapter *);
      int scl_gpio;
      int sda_gpio;
    };


Members
=======

recover_bus
    Recover routine. Either pass driver's ``recover_bus`` routine, or
    ``i2c_generic_scl_recovery`` or ``i2c_generic_gpio_recovery``.

get_scl
    This gets current value of SCL line. Mandatory for generic SCL
    recovery. Used internally for generic GPIO recovery.

set_scl
    This sets/clears SCL line. Mandatory for generic SCL recovery. Used
    internally for generic GPIO recovery.

get_sda
    This gets current value of SDA line. Optional for generic SCL
    recovery. Used internally, if sda_gpio is a valid GPIO, for generic
    GPIO recovery.

prepare_recovery
    This will be called before starting recovery. Platform may configure
    padmux here for SDA/SCL line or something else they want.

unprepare_recovery
    This will be called after completing recovery. Platform may
    configure padmux here for SDA/SCL line or something else they want.

scl_gpio
    gpio number of the SCL line. Only required for GPIO recovery.

sda_gpio
    gpio number of the SDA line. Only required for GPIO recovery.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
