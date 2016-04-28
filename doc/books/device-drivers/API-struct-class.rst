.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-class:

============
struct class
============

*man struct class(9)*

*4.6.0-rc5*

device classes


Synopsis
========

.. code-block:: c

    struct class {
      const char * name;
      struct module * owner;
      struct class_attribute * class_attrs;
      const struct attribute_group ** dev_groups;
      struct kobject * dev_kobj;
      int (* dev_uevent) (struct device *dev, struct kobj_uevent_env *env);
      char *(* devnode) (struct device *dev, umode_t *mode);
      void (* class_release) (struct class *class);
      void (* dev_release) (struct device *dev);
      int (* suspend) (struct device *dev, pm_message_t state);
      int (* resume) (struct device *dev);
      const struct kobj_ns_type_operations * ns_type;
      const void *(* namespace) (struct device *dev);
      const struct dev_pm_ops * pm;
      struct subsys_private * p;
    };


Members
=======

name
    Name of the class.

owner
    The module owner.

class_attrs
    Default attributes of this class.

dev_groups
    Default attributes of the devices that belong to the class.

dev_kobj
    The kobject that represents this class and links it into the
    hierarchy.

dev_uevent
    Called when a device is added, removed from this class, or a few
    other things that generate uevents to add the environment variables.

devnode
    Callback to provide the devtmpfs.

class_release
    Called to release this class.

dev_release
    Called to release the device.

suspend
    Used to put the device to sleep mode, usually to a low power state.

resume
    Used to bring the device from the sleep mode.

ns_type
    Callbacks so sysfs can detemine namespaces.

namespace
    Namespace of the device belongs to this class.

pm
    The default device power management operations of this class.

p
    The private data of the driver core, no one other than the driver
    core can touch this.


Description
===========

A class is a higher-level view of a device that abstracts out low-level
implementation details. Drivers may see a SCSI disk or an ATA disk, but,
at the class level, they are all simply disks. Classes allow user space
to work with devices based on what they do, rather than how they are
connected or how they work.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
