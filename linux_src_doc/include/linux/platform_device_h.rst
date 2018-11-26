.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_device.h

.. _`platform_device_register_resndata`:

platform_device_register_resndata
=================================

.. c:function:: struct platform_device *platform_device_register_resndata(struct device *parent, const char *name, int id, const struct resource *res, unsigned int num, const void *data, size_t size)

    add a platform-level device with resources and platform-specific data

    :param parent:
        parent device for the device we're adding
    :type parent: struct device \*

    :param name:
        base name of the device we're adding
    :type name: const char \*

    :param id:
        instance id
    :type id: int

    :param res:
        set of resources that needs to be allocated for the device
    :type res: const struct resource \*

    :param num:
        number of resources
    :type num: unsigned int

    :param data:
        platform specific data for this platform device
    :type data: const void \*

    :param size:
        size of platform specific data
    :type size: size_t

.. _`platform_device_register_resndata.description`:

Description
-----------

Returns \ :c:type:`struct platform_device <platform_device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`platform_device_register_simple`:

platform_device_register_simple
===============================

.. c:function:: struct platform_device *platform_device_register_simple(const char *name, int id, const struct resource *res, unsigned int num)

    add a platform-level device and its resources

    :param name:
        base name of the device we're adding
    :type name: const char \*

    :param id:
        instance id
    :type id: int

    :param res:
        set of resources that needs to be allocated for the device
    :type res: const struct resource \*

    :param num:
        number of resources
    :type num: unsigned int

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

    :param parent:
        parent device for the device we're adding
    :type parent: struct device \*

    :param name:
        base name of the device we're adding
    :type name: const char \*

    :param id:
        instance id
    :type id: int

    :param data:
        platform specific data for this platform device
    :type data: const void \*

    :param size:
        size of platform specific data
    :type size: size_t

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

