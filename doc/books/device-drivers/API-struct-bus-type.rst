
.. _API-struct-bus-type:

===============
struct bus_type
===============

*man struct bus_type(9)*

*4.6.0-rc1*

The bus type of the device


Synopsis
========

.. code-block:: c

    struct bus_type {
      const char * name;
      const char * dev_name;
      struct device * dev_root;
      struct device_attribute * dev_attrs;
      const struct attribute_group ** bus_groups;
      const struct attribute_group ** dev_groups;
      const struct attribute_group ** drv_groups;
      int (* match) (struct device *dev, struct device_driver *drv);
      int (* uevent) (struct device *dev, struct kobj_uevent_env *env);
      int (* probe) (struct device *dev);
      int (* remove) (struct device *dev);
      void (* shutdown) (struct device *dev);
      int (* online) (struct device *dev);
      int (* offline) (struct device *dev);
      int (* suspend) (struct device *dev, pm_message_t state);
      int (* resume) (struct device *dev);
      const struct dev_pm_ops * pm;
      const struct iommu_ops * iommu_ops;
      struct subsys_private * p;
      struct lock_class_key lock_key;
    };


Members
=======

name
    The name of the bus.

dev_name
    Used for subsystems to enumerate devices like (“foo\ ``u``”, dev->id).

dev_root
    Default device to use as the parent.

dev_attrs
    Default attributes of the devices on the bus.

bus_groups
    Default attributes of the bus.

dev_groups
    Default attributes of the devices on the bus.

drv_groups
    Default attributes of the device drivers on the bus.

match
    Called, perhaps multiple times, whenever a new device or driver is added for this bus. It should return a positive value if the given device can be handled by the given driver
    and zero otherwise. It may also return error code if determining that the driver supports the device is not possible. In case of -EPROBE_DEFER it will queue the device for
    deferred probing.

uevent
    Called when a device is added, removed, or a few other things that generate uevents to add the environment variables.

probe
    Called when a new device or driver add to this bus, and callback the specific driver's probe to initial the matched device.

remove
    Called when a device removed from this bus.

shutdown
    Called at shut-down time to quiesce the device.

online
    Called to put the device back online (after offlining it).

offline
    Called to put the device offline for hot-removal. May fail.

suspend
    Called when a device on this bus wants to go to sleep mode.

resume
    Called to bring a device on this bus out of sleep mode.

pm
    Power management operations of this bus, callback the specific device driver's pm-ops.

iommu_ops
    IOMMU specific operations for this bus, used to attach IOMMU driver implementations to a bus and allow the driver to do bus-specific setup

p
    The private data of the driver core, only the driver core can touch this.

lock_key
    Lock class key for use by the lock validator


Description
===========

A bus is a channel between the processor and one or more devices. For the purposes of the device model, all devices are connected via a bus, even if it is an internal, virtual,
“platform” bus. Buses can plug into each other. A USB controller is usually a PCI device, for example. The device model represents the actual connections between buses and the
devices they control. A bus is represented by the bus_type structure. It contains the name, the default attributes, the bus' methods, PM operations, and the driver core's private
data.
