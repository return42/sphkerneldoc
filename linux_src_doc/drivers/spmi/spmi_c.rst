.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spmi/spmi.c

.. _`spmi_device_add`:

spmi_device_add
===============

.. c:function:: int spmi_device_add(struct spmi_device *sdev)

    add a device previously constructed via \ :c:func:`spmi_device_alloc`\ 

    :param struct spmi_device \*sdev:
        spmi_device to be added

.. _`spmi_device_remove`:

spmi_device_remove
==================

.. c:function:: void spmi_device_remove(struct spmi_device *sdev)

    remove an SPMI device

    :param struct spmi_device \*sdev:
        spmi_device to be removed

.. _`spmi_register_read`:

spmi_register_read
==================

.. c:function:: int spmi_register_read(struct spmi_device *sdev, u8 addr, u8 *buf)

    register read

    :param struct spmi_device \*sdev:
        SPMI device.

    :param u8 addr:
        slave register address (5-bit address).

    :param u8 \*buf:
        buffer to be populated with data from the Slave.

.. _`spmi_register_read.description`:

Description
-----------

Reads 1 byte of data from a Slave device register.

.. _`spmi_ext_register_read`:

spmi_ext_register_read
======================

.. c:function:: int spmi_ext_register_read(struct spmi_device *sdev, u8 addr, u8 *buf, size_t len)

    extended register read

    :param struct spmi_device \*sdev:
        SPMI device.

    :param u8 addr:
        slave register address (8-bit address).

    :param u8 \*buf:
        buffer to be populated with data from the Slave.

    :param size_t len:
        the request number of bytes to read (up to 16 bytes).

.. _`spmi_ext_register_read.description`:

Description
-----------

Reads up to 16 bytes of data from the extended register space on a
Slave device.

.. _`spmi_ext_register_readl`:

spmi_ext_register_readl
=======================

.. c:function:: int spmi_ext_register_readl(struct spmi_device *sdev, u16 addr, u8 *buf, size_t len)

    extended register read long

    :param struct spmi_device \*sdev:
        SPMI device.

    :param u16 addr:
        slave register address (16-bit address).

    :param u8 \*buf:
        buffer to be populated with data from the Slave.

    :param size_t len:
        the request number of bytes to read (up to 8 bytes).

.. _`spmi_ext_register_readl.description`:

Description
-----------

Reads up to 8 bytes of data from the extended register space on a
Slave device using 16-bit address.

.. _`spmi_register_write`:

spmi_register_write
===================

.. c:function:: int spmi_register_write(struct spmi_device *sdev, u8 addr, u8 data)

    register write

    :param struct spmi_device \*sdev:
        SPMI device

    :param u8 addr:
        slave register address (5-bit address).

    :param u8 data:
        buffer containing the data to be transferred to the Slave.

.. _`spmi_register_write.description`:

Description
-----------

Writes 1 byte of data to a Slave device register.

.. _`spmi_register_zero_write`:

spmi_register_zero_write
========================

.. c:function:: int spmi_register_zero_write(struct spmi_device *sdev, u8 data)

    register zero write

    :param struct spmi_device \*sdev:
        SPMI device.

    :param u8 data:
        the data to be written to register 0 (7-bits).

.. _`spmi_register_zero_write.description`:

Description
-----------

Writes data to register 0 of the Slave device.

.. _`spmi_ext_register_write`:

spmi_ext_register_write
=======================

.. c:function:: int spmi_ext_register_write(struct spmi_device *sdev, u8 addr, const u8 *buf, size_t len)

    extended register write

    :param struct spmi_device \*sdev:
        SPMI device.

    :param u8 addr:
        slave register address (8-bit address).

    :param const u8 \*buf:
        buffer containing the data to be transferred to the Slave.

    :param size_t len:
        the request number of bytes to read (up to 16 bytes).

.. _`spmi_ext_register_write.description`:

Description
-----------

Writes up to 16 bytes of data to the extended register space of a
Slave device.

.. _`spmi_ext_register_writel`:

spmi_ext_register_writel
========================

.. c:function:: int spmi_ext_register_writel(struct spmi_device *sdev, u16 addr, const u8 *buf, size_t len)

    extended register write long

    :param struct spmi_device \*sdev:
        SPMI device.

    :param u16 addr:
        slave register address (16-bit address).

    :param const u8 \*buf:
        buffer containing the data to be transferred to the Slave.

    :param size_t len:
        the request number of bytes to read (up to 8 bytes).

.. _`spmi_ext_register_writel.description`:

Description
-----------

Writes up to 8 bytes of data to the extended register space of a
Slave device using 16-bit address.

.. _`spmi_command_reset`:

spmi_command_reset
==================

.. c:function:: int spmi_command_reset(struct spmi_device *sdev)

    sends RESET command to the specified slave

    :param struct spmi_device \*sdev:
        SPMI device.

.. _`spmi_command_reset.description`:

Description
-----------

The Reset command initializes the Slave and forces all registers to
their reset values. The Slave shall enter the STARTUP state after
receiving a Reset command.

.. _`spmi_command_sleep`:

spmi_command_sleep
==================

.. c:function:: int spmi_command_sleep(struct spmi_device *sdev)

    sends SLEEP command to the specified SPMI device

    :param struct spmi_device \*sdev:
        SPMI device.

.. _`spmi_command_sleep.description`:

Description
-----------

The Sleep command causes the Slave to enter the user defined SLEEP state.

.. _`spmi_command_wakeup`:

spmi_command_wakeup
===================

.. c:function:: int spmi_command_wakeup(struct spmi_device *sdev)

    sends WAKEUP command to the specified SPMI device

    :param struct spmi_device \*sdev:
        SPMI device.

.. _`spmi_command_wakeup.description`:

Description
-----------

The Wakeup command causes the Slave to move from the SLEEP state to
the ACTIVE state.

.. _`spmi_command_shutdown`:

spmi_command_shutdown
=====================

.. c:function:: int spmi_command_shutdown(struct spmi_device *sdev)

    sends SHUTDOWN command to the specified SPMI device

    :param struct spmi_device \*sdev:
        SPMI device.

.. _`spmi_command_shutdown.description`:

Description
-----------

The Shutdown command causes the Slave to enter the SHUTDOWN state.

.. _`spmi_device_alloc`:

spmi_device_alloc
=================

.. c:function:: struct spmi_device *spmi_device_alloc(struct spmi_controller *ctrl)

    Allocate a new SPMI device

    :param struct spmi_controller \*ctrl:
        associated controller

.. _`spmi_device_alloc.description`:

Description
-----------

Caller is responsible for either calling \ :c:func:`spmi_device_add`\  to add the
newly allocated controller, or calling \ :c:func:`spmi_device_put`\  to discard it.

.. _`spmi_controller_alloc`:

spmi_controller_alloc
=====================

.. c:function:: struct spmi_controller *spmi_controller_alloc(struct device *parent, size_t size)

    Allocate a new SPMI controller

    :param struct device \*parent:
        parent device

    :param size_t size:
        size of private data

.. _`spmi_controller_alloc.description`:

Description
-----------

Caller is responsible for either calling \ :c:func:`spmi_controller_add`\  to add the
newly allocated controller, or calling \ :c:func:`spmi_controller_put`\  to discard it.
The allocated private data region may be accessed via
\ :c:func:`spmi_controller_get_drvdata`\ 

.. _`spmi_controller_add`:

spmi_controller_add
===================

.. c:function:: int spmi_controller_add(struct spmi_controller *ctrl)

    Add an SPMI controller

    :param struct spmi_controller \*ctrl:
        controller to be registered.

.. _`spmi_controller_add.description`:

Description
-----------

Register a controller previously allocated via \ :c:func:`spmi_controller_alloc`\  with
the SPMI core.

.. _`spmi_controller_remove`:

spmi_controller_remove
======================

.. c:function:: void spmi_controller_remove(struct spmi_controller *ctrl)

    remove an SPMI controller

    :param struct spmi_controller \*ctrl:
        controller to remove

.. _`spmi_controller_remove.description`:

Description
-----------

Remove a SPMI controller.  Caller is responsible for calling
\ :c:func:`spmi_controller_put`\  to discard the allocated controller.

.. _`__spmi_driver_register`:

__spmi_driver_register
======================

.. c:function:: int __spmi_driver_register(struct spmi_driver *sdrv, struct module *owner)

    Register client driver with SPMI core

    :param struct spmi_driver \*sdrv:
        client driver to be associated with client-device.

    :param struct module \*owner:
        *undescribed*

.. _`__spmi_driver_register.description`:

Description
-----------

This API will register the client driver with the SPMI framework.
It is typically called from the driver's module-init function.

.. This file was automatic generated / don't edit.

