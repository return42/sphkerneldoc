.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-device-driver:

====================
struct device_driver
====================

*man struct device_driver(9)*

*4.6.0-rc5*

The basic device driver structure


Synopsis
========

.. code-block:: c

    struct device_driver {
      const char * name;
      struct bus_type * bus;
      struct module * owner;
      const char * mod_name;
      bool suppress_bind_attrs;
      enum probe_type probe_type;
      const struct of_device_id * of_match_table;
      const struct acpi_device_id * acpi_match_table;
      int (* probe) (struct device *dev);
      int (* remove) (struct device *dev);
      void (* shutdown) (struct device *dev);
      int (* suspend) (struct device *dev, pm_message_t state);
      int (* resume) (struct device *dev);
      const struct attribute_group ** groups;
      const struct dev_pm_ops * pm;
      struct driver_private * p;
    };


Members
=======

name
    Name of the device driver.

bus
    The bus which the device of this driver belongs to.

owner
    The module owner.

mod_name
    Used for built-in modules.

suppress_bind_attrs
    Disables bind/unbind via sysfs.

probe_type
    Type of the probe (synchronous or asynchronous) to use.

of_match_table
    The open firmware table.

acpi_match_table
    The ACPI match table.

probe
    Called to query the existence of a specific device, whether this
    driver can work with it, and bind the driver to a specific device.

remove
    Called when the device is removed from the system to unbind a device
    from this driver.

shutdown
    Called at shut-down time to quiesce the device.

suspend
    Called to put the device to sleep mode. Usually to a low power
    state.

resume
    Called to bring a device from sleep mode.

groups
    Default attributes that get created by the driver core
    automatically.

pm
    Power management operations of the device which matched this driver.

p
    Driver core's private data, no one other than the driver core can
    touch this.


Description
===========

The device driver-model tracks all of the drivers known to the system.
The main reason for this tracking is to enable the driver core to match
up drivers with new devices. Once drivers are known objects within the
system, however, a number of other things become possible. Device
drivers can export information and configuration variables that are
independent of any specific device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
