.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/device-init.c

.. _`ps3_setup_gelic_device`:

ps3_setup_gelic_device
======================

.. c:function:: int ps3_setup_gelic_device(const struct ps3_repository_device *repo)

    Setup and register a gelic device instance.

    :param const struct ps3_repository_device \*repo:
        *undescribed*

.. _`ps3_setup_gelic_device.description`:

Description
-----------

Allocates memory for a struct ps3_system_bus_device instance, initialises the
structure members, and registers the device instance with the system bus.

.. _`ps3_setup_dynamic_device`:

ps3_setup_dynamic_device
========================

.. c:function:: int ps3_setup_dynamic_device(const struct ps3_repository_device *repo)

    Setup a dynamic device from the repository

    :param const struct ps3_repository_device \*repo:
        *undescribed*

.. _`ps3_setup_static_device`:

ps3_setup_static_device
=======================

.. c:function:: int ps3_setup_static_device(const struct ps3_repository_device *repo)

    Setup a static device from the repository

    :param const struct ps3_repository_device \*repo:
        *undescribed*

.. _`ps3_probe_thread`:

ps3_probe_thread
================

.. c:function:: int ps3_probe_thread(void *data)

    Background repository probing at system startup.

    :param void \*data:
        *undescribed*

.. _`ps3_probe_thread.description`:

Description
-----------

This implementation only supports background probing on a single bus.
It uses the hypervisor's storage device notification mechanism to wait until
a storage device is ready.  The device notification mechanism uses a
pseudo device to asynchronously notify the guest when storage devices become
ready.  The notification device has a block size of 512 bytes.

.. _`ps3_stop_probe_thread`:

ps3_stop_probe_thread
=====================

.. c:function:: int ps3_stop_probe_thread(struct notifier_block *nb, unsigned long code, void *data)

    Stops the background probe thread.

    :param struct notifier_block \*nb:
        *undescribed*

    :param unsigned long code:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ps3_start_probe_thread`:

ps3_start_probe_thread
======================

.. c:function:: int ps3_start_probe_thread(enum ps3_bus_type bus_type)

    Starts the background probe thread.

    :param enum ps3_bus_type bus_type:
        *undescribed*

.. _`ps3_register_devices`:

ps3_register_devices
====================

.. c:function:: int ps3_register_devices( void)

    Probe the system and register devices found.

    :param  void:
        no arguments

.. _`ps3_register_devices.description`:

Description
-----------

A \ :c:func:`device_initcall`\  routine.

.. This file was automatic generated / don't edit.

