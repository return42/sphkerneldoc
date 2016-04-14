.. -*- coding: utf-8; mode: rst -*-

==========
platform.c
==========

.. _`arch_setup_pdev_archdata`:

arch_setup_pdev_archdata
========================

.. c:function:: void arch_setup_pdev_archdata (struct platform_device *pdev)

    Allow manipulation of archdata before its used

    :param struct platform_device \*pdev:
        platform device


.. _`arch_setup_pdev_archdata.description`:

Description
-----------

This is called before :c:func:`platform_device_add` such that any pdev_archdata may
be setup before the platform_notifier is called.  So if a user needs to
manipulate any relevant information in the pdev_archdata they can do::

        :c:func:`platform_device_alloc`
        ... manipulate ...
        :c:func:`platform_device_add`

And if they don't care they can just call :c:func:`platform_device_register` and
everything will just work out.


.. _`platform_get_resource`:

platform_get_resource
=====================

.. c:function:: struct resource *platform_get_resource (struct platform_device *dev, unsigned int type, unsigned int num)

    get a resource for a device

    :param struct platform_device \*dev:
        platform device

    :param unsigned int type:
        resource type

    :param unsigned int num:
        resource index


.. _`platform_get_irq`:

platform_get_irq
================

.. c:function:: int platform_get_irq (struct platform_device *dev, unsigned int num)

    get an IRQ for a device

    :param struct platform_device \*dev:
        platform device

    :param unsigned int num:
        IRQ number index


.. _`platform_irq_count`:

platform_irq_count
==================

.. c:function:: int platform_irq_count (struct platform_device *dev)

    Count the number of IRQs a platform device uses

    :param struct platform_device \*dev:
        platform device


.. _`platform_irq_count.description`:

Description
-----------

Return: Number of IRQs a platform device uses or EPROBE_DEFER


.. _`platform_get_resource_byname`:

platform_get_resource_byname
============================

.. c:function:: struct resource *platform_get_resource_byname (struct platform_device *dev, unsigned int type, const char *name)

    get a resource for a device by name

    :param struct platform_device \*dev:
        platform device

    :param unsigned int type:
        resource type

    :param const char \*name:
        resource name


.. _`platform_get_irq_byname`:

platform_get_irq_byname
=======================

.. c:function:: int platform_get_irq_byname (struct platform_device *dev, const char *name)

    get an IRQ for a device by name

    :param struct platform_device \*dev:
        platform device

    :param const char \*name:
        IRQ name


.. _`platform_add_devices`:

platform_add_devices
====================

.. c:function:: int platform_add_devices (struct platform_device **devs, int num)

    add a numbers of platform devices

    :param struct platform_device \*\*devs:
        array of platform devices to add

    :param int num:
        number of platform devices in array


.. _`platform_device_put`:

platform_device_put
===================

.. c:function:: void platform_device_put (struct platform_device *pdev)

    destroy a platform device

    :param struct platform_device \*pdev:
        platform device to free


.. _`platform_device_put.description`:

Description
-----------

Free all memory associated with a platform device.  This function must
_only_ be externally called in error cases.  All other usage is a bug.


.. _`platform_device_alloc`:

platform_device_alloc
=====================

.. c:function:: struct platform_device *platform_device_alloc (const char *name, int id)

    create a platform device

    :param const char \*name:
        base name of the device we're adding

    :param int id:
        instance id


.. _`platform_device_alloc.description`:

Description
-----------

Create a platform device object which can have other objects attached
to it, and which will have attached objects freed when it is released.


.. _`platform_device_add_resources`:

platform_device_add_resources
=============================

.. c:function:: int platform_device_add_resources (struct platform_device *pdev, const struct resource *res, unsigned int num)

    add resources to a platform device

    :param struct platform_device \*pdev:
        platform device allocated by platform_device_alloc to add resources to

    :param const struct resource \*res:
        set of resources that needs to be allocated for the device

    :param unsigned int num:
        number of resources


.. _`platform_device_add_resources.description`:

Description
-----------

Add a copy of the resources to the platform device.  The memory
associated with the resources will be freed when the platform device is
released.


.. _`platform_device_add_data`:

platform_device_add_data
========================

.. c:function:: int platform_device_add_data (struct platform_device *pdev, const void *data, size_t size)

    add platform-specific data to a platform device

    :param struct platform_device \*pdev:
        platform device allocated by platform_device_alloc to add resources to

    :param const void \*data:
        platform specific data for this platform device

    :param size_t size:
        size of platform specific data


.. _`platform_device_add_data.description`:

Description
-----------

Add a copy of platform specific data to the platform device's
platform_data pointer.  The memory associated with the platform data
will be freed when the platform device is released.


.. _`platform_device_add_properties`:

platform_device_add_properties
==============================

.. c:function:: int platform_device_add_properties (struct platform_device *pdev, const struct property_set *pset)

    add built-in properties to a platform device

    :param struct platform_device \*pdev:
        platform device to add properties to

    :param const struct property_set \*pset:
        properties to add


.. _`platform_device_add_properties.description`:

Description
-----------

The function will take deep copy of the properties in ``pset`` and attach
the copy to the platform device. The memory associated with properties
will be freed when the platform device is released.


.. _`platform_device_add`:

platform_device_add
===================

.. c:function:: int platform_device_add (struct platform_device *pdev)

    add a platform device to device hierarchy

    :param struct platform_device \*pdev:
        platform device we're adding


.. _`platform_device_add.description`:

Description
-----------

This is part 2 of :c:func:`platform_device_register`, though may be called
separately _iff_ pdev was allocated by :c:func:`platform_device_alloc`.


.. _`platform_device_del`:

platform_device_del
===================

.. c:function:: void platform_device_del (struct platform_device *pdev)

    remove a platform-level device

    :param struct platform_device \*pdev:
        platform device we're removing


.. _`platform_device_del.description`:

Description
-----------

Note that this function will also release all memory- and port-based
resources owned by the device (\ ``dev``\ ->resource).  This function must
_only_ be externally called in error cases.  All other usage is a bug.


.. _`platform_device_register`:

platform_device_register
========================

.. c:function:: int platform_device_register (struct platform_device *pdev)

    add a platform-level device

    :param struct platform_device \*pdev:
        platform device we're adding


.. _`platform_device_unregister`:

platform_device_unregister
==========================

.. c:function:: void platform_device_unregister (struct platform_device *pdev)

    unregister a platform-level device

    :param struct platform_device \*pdev:
        platform device we're unregistering


.. _`platform_device_unregister.description`:

Description
-----------

Unregistration is done in 2 steps. First we release all resources
and remove it from the subsystem, then we drop reference count by
calling :c:func:`platform_device_put`.


.. _`platform_device_register_full`:

platform_device_register_full
=============================

.. c:function:: struct platform_device *platform_device_register_full (const struct platform_device_info *pdevinfo)

    add a platform-level device with resources and platform-specific data

    :param const struct platform_device_info \*pdevinfo:
        data used to create device


.. _`platform_device_register_full.description`:

Description
-----------

Returns :c:type:`struct platform_device <platform_device>` pointer on success, or :c:func:`ERR_PTR` on error.


.. _`__platform_driver_register`:

__platform_driver_register
==========================

.. c:function:: int __platform_driver_register (struct platform_driver *drv, struct module *owner)

    register a driver for platform-level devices

    :param struct platform_driver \*drv:
        platform driver structure

    :param struct module \*owner:
        owning module/driver


.. _`platform_driver_unregister`:

platform_driver_unregister
==========================

.. c:function:: void platform_driver_unregister (struct platform_driver *drv)

    unregister a driver for platform-level devices

    :param struct platform_driver \*drv:
        platform driver structure


.. _`__platform_driver_probe`:

__platform_driver_probe
=======================

.. c:function:: int __platform_driver_probe (struct platform_driver *drv, int (*probe) (struct platform_device *, struct module *module)

    register driver for non-hotpluggable device

    :param struct platform_driver \*drv:
        platform driver structure

    :param int (\*probe) (struct platform_device \*):
        the driver probe routine, probably from an __init section

    :param struct module \*module:
        module which will be the owner of the driver


.. _`__platform_driver_probe.description`:

Description
-----------

Use this instead of :c:func:`platform_driver_register` when you know the device
is not hotpluggable and has already been registered, and you want to
remove its run-once :c:func:`probe` infrastructure from memory after the driver
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

.. c:function:: struct platform_device *__platform_create_bundle (struct platform_driver *driver, int (*probe) (struct platform_device *, struct resource *res, unsigned int n_res, const void *data, size_t size, struct module *module)

    register driver and create corresponding device

    :param struct platform_driver \*driver:
        platform driver structure

    :param int (\*probe) (struct platform_device \*):
        the driver probe routine, probably from an __init section

    :param struct resource \*res:
        set of resources that needs to be allocated for the device

    :param unsigned int n_res:
        number of resources

    :param const void \*data:
        platform specific data for this platform device

    :param size_t size:
        size of platform specific data

    :param struct module \*module:
        module which will be the owner of the driver


.. _`__platform_create_bundle.description`:

Description
-----------

Use this in legacy-style modules that probe hardware directly and
register a single platform device and corresponding platform driver.

Returns :c:type:`struct platform_device <platform_device>` pointer on success, or :c:func:`ERR_PTR` on error.


.. _`__platform_register_drivers`:

__platform_register_drivers
===========================

.. c:function:: int __platform_register_drivers (struct platform_driver *const *drivers, unsigned int count, struct module *owner)

    register an array of platform drivers

    :param const \*drivers:
        an array of drivers to register

    :param unsigned int count:
        the number of drivers to register

    :param struct module \*owner:
        module owning the drivers


.. _`__platform_register_drivers.description`:

Description
-----------

Registers platform drivers specified by an array. On failure to register a
driver, all previously registered drivers will be unregistered. Callers of
this API should use :c:func:`platform_unregister_drivers` to unregister drivers in
the reverse order.

Returns: 0 on success or a negative error code on failure.


.. _`platform_unregister_drivers`:

platform_unregister_drivers
===========================

.. c:function:: void platform_unregister_drivers (struct platform_driver *const *drivers, unsigned int count)

    unregister an array of platform drivers

    :param const \*drivers:
        an array of drivers to unregister

    :param unsigned int count:
        the number of drivers to unregister


.. _`platform_unregister_drivers.description`:

Description
-----------

Unegisters platform drivers specified by an array. This is typically used
to complement an earlier call to :c:func:`platform_register_drivers`. Drivers are
unregistered in the reverse order in which they were registered.


.. _`platform_match`:

platform_match
==============

.. c:function:: int platform_match (struct device *dev, struct device_driver *drv)

    bind platform device to platform driver.

    :param struct device \*dev:
        device.

    :param struct device_driver \*drv:
        driver.


.. _`platform_match.description`:

Description
-----------

Platform device IDs are assumed to be encoded like this:
"<name><instance>", where <name> is a short description of the type of
device, like "pci" or "floppy", and <instance> is the enumerated
instance of the device, like '0' or '42'.  Driver IDs are simply
"<name>".  So, extract the <name> from the platform_device structure,
and compare it against the name of the driver. Return whether they match
or not.


.. _`early_platform_driver_register`:

early_platform_driver_register
==============================

.. c:function:: int early_platform_driver_register (struct early_platform_driver *epdrv, char *buf)

    register early platform driver

    :param struct early_platform_driver \*epdrv:
        early_platform driver structure

    :param char \*buf:
        string passed from :c:func:`early_param`


.. _`early_platform_driver_register.description`:

Description
-----------

Helper function for :c:func:`early_platform_init` / :c:func:`early_platform_init_buffer`


.. _`early_platform_add_devices`:

early_platform_add_devices
==========================

.. c:function:: void early_platform_add_devices (struct platform_device **devs, int num)

    adds a number of early platform devices

    :param struct platform_device \*\*devs:
        array of early platform devices to add

    :param int num:
        number of early platform devices in array


.. _`early_platform_add_devices.description`:

Description
-----------

Used by early architecture code to register early platform devices and
their platform data.


.. _`early_platform_driver_register_all`:

early_platform_driver_register_all
==================================

.. c:function:: void early_platform_driver_register_all (char *class_str)

    register early platform drivers

    :param char \*class_str:
        string to identify early platform driver class


.. _`early_platform_driver_register_all.description`:

Description
-----------

Used by architecture code to register all early platform drivers
for a certain class. If omitted then only early platform drivers
with matching kernel command line class parameters will be registered.


.. _`early_platform_match`:

early_platform_match
====================

.. c:function:: struct platform_device *early_platform_match (struct early_platform_driver *epdrv, int id)

    find early platform device matching driver

    :param struct early_platform_driver \*epdrv:
        early platform driver structure

    :param int id:
        id to match against


.. _`early_platform_left`:

early_platform_left
===================

.. c:function:: int early_platform_left (struct early_platform_driver *epdrv, int id)

    check if early platform driver has matching devices

    :param struct early_platform_driver \*epdrv:
        early platform driver structure

    :param int id:
        return true if id or above exists


.. _`early_platform_driver_probe_id`:

early_platform_driver_probe_id
==============================

.. c:function:: int early_platform_driver_probe_id (char *class_str, int id, int nr_probe)

    probe drivers matching class_str and id

    :param char \*class_str:
        string to identify early platform driver class

    :param int id:
        id to match against

    :param int nr_probe:
        number of platform devices to successfully probe before exiting


.. _`early_platform_driver_probe`:

early_platform_driver_probe
===========================

.. c:function:: int early_platform_driver_probe (char *class_str, int nr_probe, int user_only)

    probe a class of registered drivers

    :param char \*class_str:
        string to identify early platform driver class

    :param int nr_probe:
        number of platform devices to successfully probe before exiting

    :param int user_only:
        only probe user specified early platform devices


.. _`early_platform_driver_probe.description`:

Description
-----------

Used by architecture code to probe registered early platform drivers
within a certain class. For probe to happen a registered early platform
device matching a registered early platform driver is needed.


.. _`early_platform_cleanup`:

early_platform_cleanup
======================

.. c:function:: void early_platform_cleanup ( void)

    clean up early platform code

    :param void:
        no arguments

