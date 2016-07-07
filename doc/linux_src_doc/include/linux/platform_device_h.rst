.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_device.h

.. _`platform_device_register_resndata`:

platform_device_register_resndata
=================================

.. c:function:: struct platform_device *platform_device_register_resndata(struct device *parent, const char *name, int id, const struct resource *res, unsigned int num, const void *data, size_t size)

    add a platform-level device with resources and platform-specific data

    :param struct device \*parent:
        parent device for the device we're adding

    :param const char \*name:
        base name of the device we're adding

    :param int id:
        instance id

    :param const struct resource \*res:
        set of resources that needs to be allocated for the device

    :param unsigned int num:
        number of resources

    :param const void \*data:
        platform specific data for this platform device

    :param size_t size:
        size of platform specific data

.. _`platform_device_register_resndata.description`:

Description
-----------

Returns \ :c:type:`struct platform_device <platform_device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`platform_device_register_simple`:

platform_device_register_simple
===============================

.. c:function:: struct platform_device *platform_device_register_simple(const char *name, int id, const struct resource *res, unsigned int num)

    add a platform-level device and its resources

    :param const char \*name:
        base name of the device we're adding

    :param int id:
        instance id

    :param const struct resource \*res:
        set of resources that needs to be allocated for the device

    :param unsigned int num:
        number of resources

.. _`platform_device_register_simple.description`:

Description
-----------

This function creates a simple platform device that requires minimal
resource and memory management. Canned release function freeing memory
allocated for the device allows drivers using such devices to be
unloaded without waiting for the last reference to the device to be
dropped.

This interface is primarily intended for use with legacy drivers which
probe hardware directly.  Because such drivers create sysfs device nodes
themselves, rather than letting system infrastructure handle such device
enumeration tasks, they don't fully conform to the Linux driver model.
In particular, when such drivers are built as modules, they can't be
"hotplugged".

Returns \ :c:type:`struct platform_device <platform_device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`platform_device_register_data`:

platform_device_register_data
=============================

.. c:function:: struct platform_device *platform_device_register_data(struct device *parent, const char *name, int id, const void *data, size_t size)

    add a platform-level device with platform-specific data

    :param struct device \*parent:
        parent device for the device we're adding

    :param const char \*name:
        base name of the device we're adding

    :param int id:
        instance id

    :param const void \*data:
        platform specific data for this platform device

    :param size_t size:
        size of platform specific data

.. _`platform_device_register_data.description`:

Description
-----------

This function creates a simple platform device that requires minimal
resource and memory management. Canned release function freeing memory
allocated for the device allows drivers using such devices to be
unloaded without waiting for the last reference to the device to be
dropped.

Returns \ :c:type:`struct platform_device <platform_device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. This file was automatic generated / don't edit.

