.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/sh/superhyway/superhyway.c

.. _`superhyway_add_device`:

superhyway_add_device
=====================

.. c:function:: int superhyway_add_device(unsigned long base, struct superhyway_device *sdev, struct superhyway_bus *bus)

    Add a SuperHyway module

    :param unsigned long base:
        Physical address where module is mapped.

    :param struct superhyway_device \*sdev:
        SuperHyway device to add, or NULL to allocate a new one.

    :param struct superhyway_bus \*bus:
        Bus where SuperHyway module resides.

.. _`superhyway_add_device.description`:

Description
-----------

This is responsible for adding a new SuperHyway module. This sets up a new
struct superhyway_device for the module being added if \ ``sdev``\  == NULL.

Devices are initially added in the order that they are scanned (from the
top-down of the memory map), and are assigned an ID based on the order that
they are added. Any manual addition of a module will thus get the ID after
the devices already discovered regardless of where it resides in memory.

Further work can and should be done in \ :c:func:`superhyway_scan_bus`\ , to be sure
that any new modules are properly discovered and subsequently registered.

.. _`superhyway_register_driver`:

superhyway_register_driver
==========================

.. c:function:: int superhyway_register_driver(struct superhyway_driver *drv)

    Register a new SuperHyway driver

    :param struct superhyway_driver \*drv:
        SuperHyway driver to register.

.. _`superhyway_register_driver.description`:

Description
-----------

This registers the passed in \ ``drv``\ . Any devices matching the id table will
automatically be populated and handed off to the driver's specified probe
routine.

.. _`superhyway_unregister_driver`:

superhyway_unregister_driver
============================

.. c:function:: void superhyway_unregister_driver(struct superhyway_driver *drv)

    Unregister a SuperHyway driver

    :param struct superhyway_driver \*drv:
        SuperHyway driver to unregister.

.. _`superhyway_unregister_driver.description`:

Description
-----------

This cleans up after \ :c:func:`superhyway_register_driver`\ , and should be invoked in
the exit path of any module drivers.

.. This file was automatic generated / don't edit.

