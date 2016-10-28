.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/system-bus.c

.. _`ps3_system_bus_release_device`:

ps3_system_bus_release_device
=============================

.. c:function:: void ps3_system_bus_release_device(struct device *_dev)

    remove a device from the system bus

    :param struct device \*_dev:
        *undescribed*

.. _`ps3_system_bus_device_register`:

ps3_system_bus_device_register
==============================

.. c:function:: int ps3_system_bus_device_register(struct ps3_system_bus_device *dev)

    add a device to the system bus

    :param struct ps3_system_bus_device \*dev:
        *undescribed*

.. _`ps3_system_bus_device_register.description`:

Description
-----------

\ :c:func:`ps3_system_bus_device_register`\  expects the dev object to be allocated
dynamically by the caller.  The system bus takes ownership of the dev
object and frees the object in \ :c:func:`ps3_system_bus_release_device`\ .

.. This file was automatic generated / don't edit.

