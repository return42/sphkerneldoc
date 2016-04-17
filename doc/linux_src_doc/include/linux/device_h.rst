.. -*- coding: utf-8; mode: rst -*-

========
device.h
========


.. _`bus_type`:

struct bus_type
===============

.. c:type:: bus_type

    The bus type of the device


.. _`bus_type.definition`:

Definition
----------

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


.. _`bus_type.members`:

Members
-------

:``name``:
    The name of the bus.

:``dev_name``:
    Used for subsystems to enumerate devices like ("foo\ ``u``\ ", dev->id).

:``dev_root``:
    Default device to use as the parent.

:``dev_attrs``:
    Default attributes of the devices on the bus.

:``bus_groups``:
    Default attributes of the bus.

:``dev_groups``:
    Default attributes of the devices on the bus.

:``drv_groups``:
    Default attributes of the device drivers on the bus.

:``match``:
    Called, perhaps multiple times, whenever a new device or driver
    is added for this bus. It should return a positive value if the
    given device can be handled by the given driver and zero
    otherwise. It may also return error code if determining that
    the driver supports the device is not possible. In case of
    -EPROBE_DEFER it will queue the device for deferred probing.

:``uevent``:
    Called when a device is added, removed, or a few other things
    that generate uevents to add the environment variables.

:``probe``:
    Called when a new device or driver add to this bus, and callback
    the specific driver's probe to initial the matched device.

:``remove``:
    Called when a device removed from this bus.

:``shutdown``:
    Called at shut-down time to quiesce the device.

:``online``:
    Called to put the device back online (after offlining it).

:``offline``:
    Called to put the device offline for hot-removal. May fail.

:``suspend``:
    Called when a device on this bus wants to go to sleep mode.

:``resume``:
    Called to bring a device on this bus out of sleep mode.

:``pm``:
    Power management operations of this bus, callback the specific
    device driver's pm-ops.

:``iommu_ops``:
    IOMMU specific operations for this bus, used to attach IOMMU
    driver implementations to a bus and allow the driver to do
    bus-specific setup

:``p``:
    The private data of the driver core, only the driver core can
    touch this.

:``lock_key``:
    Lock class key for use by the lock validator




.. _`bus_type.description`:

Description
-----------

A bus is a channel between the processor and one or more devices. For the
purposes of the device model, all devices are connected via a bus, even if
it is an internal, virtual, "platform" bus. Buses can plug into each other.
A USB controller is usually a PCI device, for example. The device model
represents the actual connections between buses and the devices they control.
A bus is represented by the bus_type structure. It contains the name, the
default attributes, the bus' methods, PM operations, and the driver core's
private data.



.. _`probe_type`:

enum probe_type
===============

.. c:type:: probe_type

    device driver probe type to try Device drivers may opt in for special handling of their respective probe routines. This tells the core what to expect and prefer.


.. _`probe_type.definition`:

Definition
----------

.. code-block:: c

    enum probe_type {
      PROBE_DEFAULT_STRATEGY,
      PROBE_PREFER_ASYNCHRONOUS,
      PROBE_FORCE_SYNCHRONOUS
    };


.. _`probe_type.constants`:

Constants
---------

:``PROBE_DEFAULT_STRATEGY``:
    Used by drivers that work equally well
    whether probed synchronously or asynchronously.

:``PROBE_PREFER_ASYNCHRONOUS``:
    Drivers for "slow" devices which
    probing order is not essential for booting the system may
    opt into executing their probes asynchronously.

:``PROBE_FORCE_SYNCHRONOUS``:
    Use this to annotate drivers that need
    their probe routines to run synchronously with driver and
    device registration (with the exception of -EPROBE_DEFER
    handling - re-probing always ends up being done asynchronously).


.. _`probe_type.description`:

Description
-----------

Note that the end goal is to switch the kernel to use asynchronous
probing by default, so annotating drivers with
``PROBE_PREFER_ASYNCHRONOUS`` is a temporary measure that allows us
to speed up boot process while we are validating the rest of the
drivers.



.. _`device_driver`:

struct device_driver
====================

.. c:type:: device_driver

    The basic device driver structure


.. _`device_driver.definition`:

Definition
----------

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


.. _`device_driver.members`:

Members
-------

:``name``:
    Name of the device driver.

:``bus``:
    The bus which the device of this driver belongs to.

:``owner``:
    The module owner.

:``mod_name``:
    Used for built-in modules.

:``suppress_bind_attrs``:
    Disables bind/unbind via sysfs.

:``probe_type``:
    Type of the probe (synchronous or asynchronous) to use.

:``of_match_table``:
    The open firmware table.

:``acpi_match_table``:
    The ACPI match table.

:``probe``:
    Called to query the existence of a specific device,
    whether this driver can work with it, and bind the driver
    to a specific device.

:``remove``:
    Called when the device is removed from the system to
    unbind a device from this driver.

:``shutdown``:
    Called at shut-down time to quiesce the device.

:``suspend``:
    Called to put the device to sleep mode. Usually to a
    low power state.

:``resume``:
    Called to bring a device from sleep mode.

:``groups``:
    Default attributes that get created by the driver core
    automatically.

:``pm``:
    Power management operations of the device which matched
    this driver.

:``p``:
    Driver core's private data, no one other than the driver
    core can touch this.




.. _`device_driver.description`:

Description
-----------

The device driver-model tracks all of the drivers known to the system.
The main reason for this tracking is to enable the driver core to match
up drivers with new devices. Once drivers are known objects within the
system, however, a number of other things become possible. Device drivers
can export information and configuration variables that are independent
of any specific device.



.. _`subsys_interface`:

struct subsys_interface
=======================

.. c:type:: subsys_interface

    interfaces to device functions


.. _`subsys_interface.definition`:

Definition
----------

.. code-block:: c

  struct subsys_interface {
    const char * name;
    struct bus_type * subsys;
    struct list_head node;
    int (* add_dev) (struct device *dev, struct subsys_interface *sif);
    void (* remove_dev) (struct device *dev, struct subsys_interface *sif);
  };


.. _`subsys_interface.members`:

Members
-------

:``name``:
    name of the device function

:``subsys``:
    subsytem of the devices to attach to

:``node``:
    the list of functions registered at the subsystem

:``add_dev``:
    device hookup to device function handler

:``remove_dev``:
    device hookup to device function handler




.. _`subsys_interface.description`:

Description
-----------

Simple interfaces attached to a subsystem. Multiple interfaces can
attach to a subsystem and its devices. Unlike drivers, they do not
exclusively claim or control devices. Interfaces usually represent
a specific functionality of a subsystem/class of devices.



.. _`class`:

struct class
============

.. c:type:: class

    device classes


.. _`class.definition`:

Definition
----------

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


.. _`class.members`:

Members
-------

:``name``:
    Name of the class.

:``owner``:
    The module owner.

:``class_attrs``:
    Default attributes of this class.

:``dev_groups``:
    Default attributes of the devices that belong to the class.

:``dev_kobj``:
    The kobject that represents this class and links it into the hierarchy.

:``dev_uevent``:
    Called when a device is added, removed from this class, or a
    few other things that generate uevents to add the environment
    variables.

:``devnode``:
    Callback to provide the devtmpfs.

:``class_release``:
    Called to release this class.

:``dev_release``:
    Called to release the device.

:``suspend``:
    Used to put the device to sleep mode, usually to a low power
    state.

:``resume``:
    Used to bring the device from the sleep mode.

:``ns_type``:
    Callbacks so sysfs can detemine namespaces.

:``namespace``:
    Namespace of the device belongs to this class.

:``pm``:
    The default device power management operations of this class.

:``p``:
    The private data of the driver core, no one other than the
    driver core can touch this.




.. _`class.description`:

Description
-----------

A class is a higher-level view of a device that abstracts out low-level
implementation details. Drivers may see a SCSI disk or an ATA disk, but,
at the class level, they are all simply disks. Classes allow user space
to work with devices based on what they do, rather than how they are
connected or how they work.



.. _`device`:

struct device
=============

.. c:type:: device

    The basic device structure


.. _`device.definition`:

Definition
----------

.. code-block:: c

  struct device {
    struct device * parent;
    struct device_private * p;
    struct kobject kobj;
    const char * init_name;
    const struct device_type * type;
    struct mutex mutex;
    struct bus_type * bus;
    struct device_driver * driver;
    void * platform_data;
    void * driver_data;
    struct dev_pm_info power;
    struct dev_pm_domain * pm_domain;
    #ifdef CONFIG_GENERIC_MSI_IRQ_DOMAIN
    struct irq_domain * msi_domain;
    #endif
    #ifdef CONFIG_PINCTRL
    struct dev_pin_info * pins;
    #endif
    #ifdef CONFIG_GENERIC_MSI_IRQ
    struct list_head msi_list;
    #endif
    #ifdef CONFIG_NUMA
    int numa_node;
    #endif
    u64 * dma_mask;
    u64 coherent_dma_mask;
    unsigned long dma_pfn_offset;
    struct device_dma_parameters * dma_parms;
    struct list_head dma_pools;
    struct dma_coherent_mem * dma_mem;
    #ifdef CONFIG_DMA_CMA
    struct cma * cma_area;
    #endif
    struct dev_archdata archdata;
    struct device_node * of_node;
    struct fwnode_handle * fwnode;
    dev_t devt;
    u32 id;
    spinlock_t devres_lock;
    struct list_head devres_head;
    struct klist_node knode_class;
    struct class * class;
    const struct attribute_group ** groups;
    void (* release) (struct device *dev);
    struct iommu_group * iommu_group;
    bool offline_disabled:1;
    bool offline:1;
  };


.. _`device.members`:

Members
-------

:``parent``:
    The device's "parent" device, the device to which it is attached.
    In most cases, a parent device is some sort of bus or host
    controller. If parent is NULL, the device, is a top-level device,
    which is not usually what you want.

:``p``:
    Holds the private data of the driver core portions of the device.
    See the comment of the struct device_private for detail.

:``kobj``:
    A top-level, abstract class from which other classes are derived.

:``init_name``:
    Initial name of the device.

:``type``:
    The type of device.
    This identifies the device type and carries type-specific
    information.

:``mutex``:
    Mutex to synchronize calls to its driver.

:``bus``:
    Type of bus device is on.

:``driver``:
    Which driver has allocated this

:``platform_data``:
    Platform data specific to the device.

:``driver_data``:
    Private pointer for driver specific info.

:``power``:
    For device power management.
    See Documentation/power/devices.txt for details.

:``pm_domain``:
    Provide callbacks that are executed during system suspend,
    hibernation, system resume and during runtime PM transitions
    along with subsystem-level and driver-level callbacks.

:``msi_domain``:
    The generic MSI domain this device is using.

:``pins``:
    For device pin management.
    See Documentation/pinctrl.txt for details.

:``msi_list``:
    Hosts MSI descriptors

:``numa_node``:
    NUMA node this device is close to.

:``dma_mask``:
    Dma mask (if dma'ble device).

:``coherent_dma_mask``:
    Like dma_mask, but for alloc_coherent mapping as not all
    hardware supports 64-bit addresses for consistent allocations
    such descriptors.

:``dma_pfn_offset``:
    offset of DMA memory range relatively of RAM

:``dma_parms``:
    A low level driver may set these to teach IOMMU code about
    segment limitations.

:``dma_pools``:
    Dma pools (if dma'ble device).

:``dma_mem``:
    Internal for coherent mem override.

:``cma_area``:
    Contiguous memory area for dma allocations

:``archdata``:
    For arch-specific additions.

:``of_node``:
    Associated device tree node.

:``fwnode``:
    Associated device node supplied by platform firmware.

:``devt``:
    For creating the sysfs "dev".

:``id``:
    device instance

:``devres_lock``:
    Spinlock to protect the resource of the device.

:``devres_head``:
    The resources list of the device.

:``knode_class``:
    The node used to add the device to the class list.

:``class``:
    The class of the device.

:``groups``:
    Optional attribute groups.

:``release``:
    Callback to free the device after all references have
    gone away. This should be set by the allocator of the
    device (i.e. the bus driver that discovered the device).

:``iommu_group``:
    IOMMU group the device belongs to.

:``offline_disabled``:
    If set, the device is permanently online.

:``offline``:
    Set after successful invocation of bus type's .:c:func:`offline`.




.. _`device.example`:

Example
-------

.. code-block:: c

For devices on custom boards, as typical of embedded
		and SOC based hardware, Linux often uses platform_data to point
		to board-specific structures describing devices and how they
		are wired.  That can include what ports are available, chip
		variants, which GPIO pins act in what additional roles, and so
		on.  This shrinks the "Board Support Packages" (BSPs) and
		minimizes board-specific #ifdefs in drivers.



.. _`device.description`:

Description
-----------

At the lowest level, every device in a Linux system is represented by an
instance of struct device. The device structure contains the information
that the device model core needs to model the system. Most subsystems,
however, track additional information about the devices they host. As a
result, it is rare for devices to be represented by bare device structures;
instead, that structure, like kobject structures, is usually embedded within
a higher-level representation of the device.



.. _`module_driver`:

module_driver
=============

.. c:function:: module_driver ( __driver,  __register,  __unregister,  ...)

    Helper macro for drivers that don't do anything special in module init/exit. This eliminates a lot of boilerplate. Each module may only use this macro once, and calling it replaces module_init() and module_exit().

    :param __driver:
        driver name

    :param __register:
        register function for this driver type

    :param __unregister:
        unregister function for this driver type
        @...: Additional arguments to be passed to __register and __unregister.

    :param ...:
        variable arguments



.. _`module_driver.description`:

Description
-----------

Use this macro to construct bus specific macros for registering
drivers, and do not use it on its own.



.. _`builtin_driver`:

builtin_driver
==============

.. c:function:: builtin_driver ( __driver,  __register,  ...)

    Helper macro for drivers that don't do anything special in init and have no exit. This eliminates some boilerplate. Each driver may only use this macro once, and calling it replaces device_initcall (or in some cases, the legacy __initcall). This is meant to be a direct parallel of module_driver() above but without the __exit stuff that is not used for builtin cases.

    :param __driver:
        driver name

    :param __register:
        register function for this driver type
        @...: Additional arguments to be passed to __register

    :param ...:
        variable arguments



.. _`builtin_driver.description`:

Description
-----------

Use this macro to construct bus specific macros for registering
drivers, and do not use it on its own.

