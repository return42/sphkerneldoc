.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/amba/bus.c

.. _`amba_driver_register`:

amba_driver_register
====================

.. c:function:: int amba_driver_register(struct amba_driver *drv)

    register an AMBA device driver

    :param drv:
        amba device driver structure
    :type drv: struct amba_driver \*

.. _`amba_driver_register.description`:

Description
-----------

Register an AMBA device driver with the Linux device model
core.  If devices pre-exist, the drivers probe function will
be called.

.. _`amba_driver_unregister`:

amba_driver_unregister
======================

.. c:function:: void amba_driver_unregister(struct amba_driver *drv)

    remove an AMBA device driver

    :param drv:
        AMBA device driver structure to remove
    :type drv: struct amba_driver \*

.. _`amba_driver_unregister.description`:

Description
-----------

Unregister an AMBA device driver from the Linux device
model.  The device model will call the drivers remove function
for each device the device driver is currently handling.

.. _`amba_device_add`:

amba_device_add
===============

.. c:function:: int amba_device_add(struct amba_device *dev, struct resource *parent)

    add a previously allocated AMBA device structure

    :param dev:
        AMBA device allocated by amba_device_alloc
    :type dev: struct amba_device \*

    :param parent:
        resource parent for this devices resources
    :type parent: struct resource \*

.. _`amba_device_add.description`:

Description
-----------

Claim the resource, and read the device cell ID if not already
initialized.  Register the AMBA device with the Linux device
manager.

.. _`amba_device_alloc`:

amba_device_alloc
=================

.. c:function:: struct amba_device *amba_device_alloc(const char *name, resource_size_t base, size_t size)

    allocate an AMBA device

    :param name:
        sysfs name of the AMBA device
    :type name: const char \*

    :param base:
        base of AMBA device
    :type base: resource_size_t

    :param size:
        size of AMBA device
    :type size: size_t

.. _`amba_device_alloc.description`:

Description
-----------

Allocate and initialize an AMBA device structure.  Returns \ ``NULL``\ 
on failure.

.. _`amba_device_register`:

amba_device_register
====================

.. c:function:: int amba_device_register(struct amba_device *dev, struct resource *parent)

    register an AMBA device

    :param dev:
        AMBA device to register
    :type dev: struct amba_device \*

    :param parent:
        parent memory resource
    :type parent: struct resource \*

.. _`amba_device_register.description`:

Description
-----------

Setup the AMBA device, reading the cell ID if present.
Claim the resource, and register the AMBA device with
the Linux device manager.

.. _`amba_device_put`:

amba_device_put
===============

.. c:function:: void amba_device_put(struct amba_device *dev)

    put an AMBA device

    :param dev:
        AMBA device to put
    :type dev: struct amba_device \*

.. _`amba_device_unregister`:

amba_device_unregister
======================

.. c:function:: void amba_device_unregister(struct amba_device *dev)

    unregister an AMBA device

    :param dev:
        AMBA device to remove
    :type dev: struct amba_device \*

.. _`amba_device_unregister.description`:

Description
-----------

Remove the specified AMBA device from the Linux device
manager.  All files associated with this object will be
destroyed, and device drivers notified that the device has
been removed.  The AMBA device's resources including
the amba_device structure will be freed once all
references to it have been dropped.

.. _`amba_find_device`:

amba_find_device
================

.. c:function:: struct amba_device *amba_find_device(const char *busid, struct device *parent, unsigned int id, unsigned int mask)

    locate an AMBA device given a bus id

    :param busid:
        bus id for device (or NULL)
    :type busid: const char \*

    :param parent:
        parent device (or NULL)
    :type parent: struct device \*

    :param id:
        peripheral ID (or 0)
    :type id: unsigned int

    :param mask:
        peripheral ID mask (or 0)
    :type mask: unsigned int

.. _`amba_find_device.description`:

Description
-----------

Return the AMBA device corresponding to the supplied parameters.
If no device matches, returns NULL.

.. _`amba_find_device.note`:

NOTE
----

When a valid device is found, its refcount is
incremented, and must be decremented before the returned
reference.

.. _`amba_request_regions`:

amba_request_regions
====================

.. c:function:: int amba_request_regions(struct amba_device *dev, const char *name)

    request all mem regions associated with device

    :param dev:
        amba_device structure for device
    :type dev: struct amba_device \*

    :param name:
        name, or NULL to use driver name
    :type name: const char \*

.. _`amba_release_regions`:

amba_release_regions
====================

.. c:function:: void amba_release_regions(struct amba_device *dev)

    release mem regions associated with device

    :param dev:
        amba_device structure for device
    :type dev: struct amba_device \*

.. _`amba_release_regions.description`:

Description
-----------

Release regions claimed by a successful call to amba_request_regions.

.. This file was automatic generated / don't edit.

