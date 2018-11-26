.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hv/vmbus_drv.c

.. _`__vmbus_driver_register`:

\__vmbus_driver_register
========================

.. c:function:: int __vmbus_driver_register(struct hv_driver *hv_driver, struct module *owner, const char *mod_name)

    Register a vmbus's driver

    :param hv_driver:
        Pointer to driver structure you want to register
    :type hv_driver: struct hv_driver \*

    :param owner:
        owner module of the drv
    :type owner: struct module \*

    :param mod_name:
        module name string
    :type mod_name: const char \*

.. _`__vmbus_driver_register.description`:

Description
-----------

Registers the given driver with Linux through the 'driver_register()' call
and sets up the hyper-v vmbus handling for this driver.
It will return the state of the 'driver_register()' call.

.. _`vmbus_driver_unregister`:

vmbus_driver_unregister
=======================

.. c:function:: void vmbus_driver_unregister(struct hv_driver *hv_driver)

    Unregister a vmbus's driver

    :param hv_driver:
        Pointer to driver structure you want to
        un-register
    :type hv_driver: struct hv_driver \*

.. _`vmbus_driver_unregister.description`:

Description
-----------

Un-register the given driver that was previous registered with a call to
\ :c:func:`vmbus_driver_register`\ 

.. _`vmbus_allocate_mmio`:

vmbus_allocate_mmio
===================

.. c:function:: int vmbus_allocate_mmio(struct resource **new, struct hv_device *device_obj, resource_size_t min, resource_size_t max, resource_size_t size, resource_size_t align, bool fb_overlap_ok)

    Pick a memory-mapped I/O range.

    :param new:
        If successful, supplied a pointer to the
        allocated MMIO space.
    :type new: struct resource \*\*

    :param device_obj:
        Identifies the caller
    :type device_obj: struct hv_device \*

    :param min:
        Minimum guest physical address of the
        allocation
    :type min: resource_size_t

    :param max:
        Maximum guest physical address
    :type max: resource_size_t

    :param size:
        Size of the range to be allocated
    :type size: resource_size_t

    :param align:
        Alignment of the range to be allocated
    :type align: resource_size_t

    :param fb_overlap_ok:
        Whether this allocation can be allowed
        to overlap the video frame buffer.
    :type fb_overlap_ok: bool

.. _`vmbus_allocate_mmio.description`:

Description
-----------

This function walks the resources granted to VMBus by the
\_CRS object in the ACPI namespace underneath the parent
"bridge" whether that's a root PCI bus in the Generation 1
case or a Module Device in the Generation 2 case.  It then
attempts to allocate from the global MMIO pool in a way that
matches the constraints supplied in these parameters and by
that \_CRS.

.. _`vmbus_allocate_mmio.return`:

Return
------

0 on success, -errno on failure

.. _`vmbus_free_mmio`:

vmbus_free_mmio
===============

.. c:function:: void vmbus_free_mmio(resource_size_t start, resource_size_t size)

    Free a memory-mapped I/O range.

    :param start:
        Base address of region to release.
    :type start: resource_size_t

    :param size:
        Size of the range to be allocated
    :type size: resource_size_t

.. _`vmbus_free_mmio.description`:

Description
-----------

This function releases anything requested by
\ :c:func:`vmbus_mmio_allocate`\ .

.. This file was automatic generated / don't edit.

