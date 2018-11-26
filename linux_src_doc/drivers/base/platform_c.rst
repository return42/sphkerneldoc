.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/platform.c

.. _`arch_setup_pdev_archdata`:

arch_setup_pdev_archdata
========================

.. c:function:: void arch_setup_pdev_archdata(struct platform_device *pdev)

    Allow manipulation of archdata before its used

    :param pdev:
        platform device
    :type pdev: struct platform_device \*

.. _`arch_setup_pdev_archdata.description`:

Description
-----------

This is called before \ :c:func:`platform_device_add`\  such that any pdev_archdata may
be setup before the platform_notifier is called.  So if a user needs to

.. _`arch_setup_pdev_archdata.manipulate-any-relevant-information-in-the-pdev_archdata-they-can-do`:

manipulate any relevant information in the pdev_archdata they can do
--------------------------------------------------------------------


     \ :c:func:`platform_device_alloc`\ 
     ... manipulate ...
     \ :c:func:`platform_device_add`\ 

And if they don't care they can just call \ :c:func:`platform_device_register`\  and
everything will just work out.

.. _`platform_get_resource`:

platform_get_resource
=====================

.. c:function:: struct resource *platform_get_resource(struct platform_device *dev, unsigned int type, unsigned int num)

    get a resource for a device

    :param dev:
        platform device
    :type dev: struct platform_device \*

    :param type:
        resource type
    :type type: unsigned int

    :param num:
        resource index
    :type num: unsigned int

.. _`platform_get_irq`:

platform_get_irq
================

.. c:function:: int platform_get_irq(struct platform_device *dev, unsigned int num)

    get an IRQ for a device

    :param dev:
        platform device
    :type dev: struct platform_device \*

    :param num:
        IRQ number index
    :type num: unsigned int

.. _`platform_irq_count`:

platform_irq_count
==================

.. c:function:: int platform_irq_count(struct platform_device *dev)

    Count the number of IRQs a platform device uses

    :param dev:
        platform device
    :type dev: struct platform_device \*

.. _`platform_irq_count.return`:

Return
------

Number of IRQs a platform device uses or EPROBE_DEFER

.. _`platform_get_resource_byname`:

platform_get_resource_byname
============================

.. c:function:: struct resource *platform_get_resource_byname(struct platform_device *dev, unsigned int type, const char *name)

    get a resource for a device by name

    :param dev:
        platform device
    :type dev: struct platform_device \*

    :param type:
        resource type
    :type type: unsigned int

    :param name:
        resource name
    :type name: const char \*

.. _`platform_get_irq_byname`:

platform_get_irq_byname
=======================

.. c:function:: int platform_get_irq_byname(struct platform_device *dev, const char *name)

    get an IRQ for a device by name

    :param dev:
        platform device
    :type dev: struct platform_device \*

    :param name:
        IRQ name
    :type name: const char \*

.. _`platform_add_devices`:

platform_add_devices
====================

.. c:function:: int platform_add_devices(struct platform_device **devs, int num)

    add a numbers of platform devices

    :param devs:
        array of platform devices to add
    :type devs: struct platform_device \*\*

    :param num:
        number of platform devices in array
    :type num: int

.. _`platform_device_put`:

platform_device_put
===================

.. c:function:: void platform_device_put(struct platform_device *pdev)

    destroy a platform device

    :param pdev:
        platform device to free
    :type pdev: struct platform_device \*

.. _`platform_device_put.description`:

Description
-----------

Free all memory associated with a platform device.  This function must
_only_ be externally called in error cases.  All other usage is a bug.

.. _`platform_device_alloc`:

platform_device_alloc
=====================

.. c:function:: struct platform_device *platform_device_alloc(const char *name, int id)

    create a platform device

    :param name:
        base name of the device we're adding
    :type name: const char \*

    :param id:
        instance id
    :type id: int

.. _`platform_device_alloc.description`:

Description
-----------

Create a platform device object which can have other objects attached
to it, and which will have attached objects freed when it is released.

.. _`platform_device_add_resources`:

platform_device_add_resources
=============================

.. c:function:: int platform_device_add_resources(struct platform_device *pdev, const struct resource *res, unsigned int num)

    add resources to a platform device

    :param pdev:
        platform device allocated by platform_device_alloc to add resources to
    :type pdev: struct platform_device \*

    :param res:
        set of resources that needs to be allocated for the device
    :type res: const struct resource \*

    :param num:
        number of resources
    :type num: unsigned int

.. _`platform_device_add_resources.description`:

Description
-----------

Add a copy of the resources to the platform device.  The memory
associated with the resources will be freed when the platform device is
released.

.. _`platform_device_add_data`:

platform_device_add_data
========================

.. c:function:: int platform_device_add_data(struct platform_device *pdev, const void *data, size_t size)

    add platform-specific data to a platform device

    :param pdev:
        platform device allocated by platform_device_alloc to add resources to
    :type pdev: struct platform_device \*

    :param data:
        platform specific data for this platform device
    :type data: const void \*

    :param size:
        size of platform specific data
    :type size: size_t

.. _`platform_device_add_data.description`:

Description
-----------

Add a copy of platform specific data to the platform device's
platform_data pointer.  The memory associated with the platform data
will be freed when the platform device is released.

.. _`platform_device_add_properties`:

platform_device_add_properties
==============================

.. c:function:: int platform_device_add_properties(struct platform_device *pdev, const struct property_entry *properties)

    add built-in properties to a platform device

    :param pdev:
        platform device to add properties to
    :type pdev: struct platform_device \*

    :param properties:
        null terminated array of properties to add
    :type properties: const struct property_entry \*

.. _`platform_device_add_properties.description`:

Description
-----------

The function will take deep copy of \ ``properties``\  and attach the copy to the
platform device. The memory associated with properties will be freed when the
platform device is released.

.. _`platform_device_add`:

platform_device_add
===================

.. c:function:: int platform_device_add(struct platform_device *pdev)

    add a platform device to device hierarchy

    :param pdev:
        platform device we're adding
    :type pdev: struct platform_device \*

.. _`platform_device_add.description`:

Description
-----------

This is part 2 of \ :c:func:`platform_device_register`\ , though may be called
separately _iff_ pdev was allocated by \ :c:func:`platform_device_alloc`\ .

.. _`platform_device_del`:

platform_device_del
===================

.. c:function:: void platform_device_del(struct platform_device *pdev)

    remove a platform-level device

    :param pdev:
        platform device we're removing
    :type pdev: struct platform_device \*

.. _`platform_device_del.description`:

Description
-----------

Note that this function will also release all memory- and port-based
resources owned by the device (@dev->resource).  This function must
_only_ be externally called in error cases.  All other usage is a bug.

.. _`platform_device_register`:

platform_device_register
========================

.. c:function:: int platform_device_register(struct platform_device *pdev)

    add a platform-level device

    :param pdev:
        platform device we're adding
    :type pdev: struct platform_device \*

.. _`platform_device_unregister`:

platform_device_unregister
==========================

.. c:function:: void platform_device_unregister(struct platform_device *pdev)

    unregister a platform-level device

    :param pdev:
        platform device we're unregistering
    :type pdev: struct platform_device \*

.. _`platform_device_unregister.description`:

Description
-----------

Unregistration is done in 2 steps. First we release all resources
and remove it from the subsystem, then we drop reference count by
calling \ :c:func:`platform_device_put`\ .

.. _`platform_device_register_full`:

platform_device_register_full
=============================

.. c:function:: struct platform_device *platform_device_register_full(const struct platform_device_info *pdevinfo)

    add a platform-level device with resources and platform-specific data

    :param pdevinfo:
        data used to create device
    :type pdevinfo: const struct platform_device_info \*

.. _`platform_device_register_full.description`:

Description
-----------

Returns \ :c:type:`struct platform_device <platform_device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`__platform_driver_register`:

__platform_driver_register
==========================

.. c:function:: int __platform_driver_register(struct platform_driver *drv, struct module *owner)

    register a driver for platform-level devices

    :param drv:
        platform driver structure
    :type drv: struct platform_driver \*

    :param owner:
        owning module/driver
    :type owner: struct module \*

.. _`platform_driver_unregister`:

platform_driver_unregister
==========================

.. c:function:: void platform_driver_unregister(struct platform_driver *drv)

    unregister a driver for platform-level devices

    :param drv:
        platform driver structure
    :type drv: struct platform_driver \*

.. _`__platform_driver_probe`:

__platform_driver_probe
=======================

.. c:function:: int __platform_driver_probe(struct platform_driver *drv, int (*probe)(struct platform_device *), struct module *module)

    register driver for non-hotpluggable device

    :param drv:
        platform driver structure
    :type drv: struct platform_driver \*

    :param int (\*probe)(struct platform_device \*):
        the driver probe routine, probably from an __init section

    :param module:
        module which will be the owner of the driver
    :type module: struct module \*

.. _`__platform_driver_probe.description`:

Description
-----------

Use this instead of \ :c:func:`platform_driver_register`\  when you know the device
is not hotpluggable and has already been registered, and you want to
remove its run-once \ :c:func:`probe`\  infrastructure from memory after the driver
has bound to the device.

One typical use for this would be with drivers for controllers integrated
into system-on-chip processors, where the controller devices have been
configured as part of board setup.

Note that this is incompatible with deferred probing.

Returns zero if the driver registered and bound to a device, else returns
a negative error code and with the driver not registered.

.. _`__platform_create_bundle`:

__platform_create_bundle
========================

.. c:function:: struct platform_device *__platform_create_bundle(struct platform_driver *driver, int (*probe)(struct platform_device *), struct resource *res, unsigned int n_res, const void *data, size_t size, struct module *module)

    register driver and create corresponding device

    :param driver:
        platform driver structure
    :type driver: struct platform_driver \*

    :param int (\*probe)(struct platform_device \*):
        the driver probe routine, probably from an __init section

    :param res:
        set of resources that needs to be allocated for the device
    :type res: struct resource \*

    :param n_res:
        number of resources
    :type n_res: unsigned int

    :param data:
        platform specific data for this platform device
    :type data: const void \*

    :param size:
        size of platform specific data
    :type size: size_t

    :param module:
        module which will be the owner of the driver
    :type module: struct module \*

.. _`__platform_create_bundle.description`:

Description
-----------

Use this in legacy-style modules that probe hardware directly and
register a single platform device and corresponding platform driver.

Returns \ :c:type:`struct platform_device <platform_device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`__platform_register_drivers`:

__platform_register_drivers
===========================

.. c:function:: int __platform_register_drivers(struct platform_driver * const *drivers, unsigned int count, struct module *owner)

    register an array of platform drivers

    :param drivers:
        an array of drivers to register
    :type drivers: struct platform_driver \* const \*

    :param count:
        the number of drivers to register
    :type count: unsigned int

    :param owner:
        module owning the drivers
    :type owner: struct module \*

.. _`__platform_register_drivers.description`:

Description
-----------

Registers platform drivers specified by an array. On failure to register a
driver, all previously registered drivers will be unregistered. Callers of
this API should use \ :c:func:`platform_unregister_drivers`\  to unregister drivers in
the reverse order.

.. _`__platform_register_drivers.return`:

Return
------

0 on success or a negative error code on failure.

.. _`platform_unregister_drivers`:

platform_unregister_drivers
===========================

.. c:function:: void platform_unregister_drivers(struct platform_driver * const *drivers, unsigned int count)

    unregister an array of platform drivers

    :param drivers:
        an array of drivers to unregister
    :type drivers: struct platform_driver \* const \*

    :param count:
        the number of drivers to unregister
    :type count: unsigned int

.. _`platform_unregister_drivers.description`:

Description
-----------

Unegisters platform drivers specified by an array. This is typically used
to complement an earlier call to \ :c:func:`platform_register_drivers`\ . Drivers are
unregistered in the reverse order in which they were registered.

.. _`platform_match`:

platform_match
==============

.. c:function:: int platform_match(struct device *dev, struct device_driver *drv)

    bind platform device to platform driver.

    :param dev:
        device.
    :type dev: struct device \*

    :param drv:
        driver.
    :type drv: struct device_driver \*

.. _`platform_match.platform-device-ids-are-assumed-to-be-encoded-like-this`:

Platform device IDs are assumed to be encoded like this
-------------------------------------------------------

"<name><instance>", where <name> is a short description of the type of
device, like "pci" or "floppy", and <instance> is the enumerated
instance of the device, like '0' or '42'.  Driver IDs are simply
"<name>".  So, extract the <name> from the platform_device structure,
and compare it against the name of the driver. Return whether they match
or not.

.. _`early_platform_driver_register`:

early_platform_driver_register
==============================

.. c:function:: int early_platform_driver_register(struct early_platform_driver *epdrv, char *buf)

    register early platform driver

    :param epdrv:
        early_platform driver structure
    :type epdrv: struct early_platform_driver \*

    :param buf:
        string passed from \ :c:func:`early_param`\ 
    :type buf: char \*

.. _`early_platform_driver_register.description`:

Description
-----------

Helper function for \ :c:func:`early_platform_init`\  / \ :c:func:`early_platform_init_buffer`\ 

.. _`early_platform_add_devices`:

early_platform_add_devices
==========================

.. c:function:: void early_platform_add_devices(struct platform_device **devs, int num)

    adds a number of early platform devices

    :param devs:
        array of early platform devices to add
    :type devs: struct platform_device \*\*

    :param num:
        number of early platform devices in array
    :type num: int

.. _`early_platform_add_devices.description`:

Description
-----------

Used by early architecture code to register early platform devices and
their platform data.

.. _`early_platform_driver_register_all`:

early_platform_driver_register_all
==================================

.. c:function:: void early_platform_driver_register_all(char *class_str)

    register early platform drivers

    :param class_str:
        string to identify early platform driver class
    :type class_str: char \*

.. _`early_platform_driver_register_all.description`:

Description
-----------

Used by architecture code to register all early platform drivers
for a certain class. If omitted then only early platform drivers
with matching kernel command line class parameters will be registered.

.. _`early_platform_match`:

early_platform_match
====================

.. c:function:: struct platform_device *early_platform_match(struct early_platform_driver *epdrv, int id)

    find early platform device matching driver

    :param epdrv:
        early platform driver structure
    :type epdrv: struct early_platform_driver \*

    :param id:
        id to match against
    :type id: int

.. _`early_platform_left`:

early_platform_left
===================

.. c:function:: int early_platform_left(struct early_platform_driver *epdrv, int id)

    check if early platform driver has matching devices

    :param epdrv:
        early platform driver structure
    :type epdrv: struct early_platform_driver \*

    :param id:
        return true if id or above exists
    :type id: int

.. _`early_platform_driver_probe_id`:

early_platform_driver_probe_id
==============================

.. c:function:: int early_platform_driver_probe_id(char *class_str, int id, int nr_probe)

    probe drivers matching class_str and id

    :param class_str:
        string to identify early platform driver class
    :type class_str: char \*

    :param id:
        id to match against
    :type id: int

    :param nr_probe:
        number of platform devices to successfully probe before exiting
    :type nr_probe: int

.. _`early_platform_driver_probe`:

early_platform_driver_probe
===========================

.. c:function:: int early_platform_driver_probe(char *class_str, int nr_probe, int user_only)

    probe a class of registered drivers

    :param class_str:
        string to identify early platform driver class
    :type class_str: char \*

    :param nr_probe:
        number of platform devices to successfully probe before exiting
    :type nr_probe: int

    :param user_only:
        only probe user specified early platform devices
    :type user_only: int

.. _`early_platform_driver_probe.description`:

Description
-----------

Used by architecture code to probe registered early platform drivers
within a certain class. For probe to happen a registered early platform
device matching a registered early platform driver is needed.

.. _`early_platform_cleanup`:

early_platform_cleanup
======================

.. c:function:: void early_platform_cleanup( void)

    clean up early platform code

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

