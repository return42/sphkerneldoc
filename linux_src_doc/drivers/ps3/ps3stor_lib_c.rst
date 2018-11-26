.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ps3/ps3stor_lib.c

.. _`ps3stor_setup`:

ps3stor_setup
=============

.. c:function:: int ps3stor_setup(struct ps3_storage_device *dev, irq_handler_t handler)

    Setup a storage device before use

    :param dev:
        Pointer to a struct ps3_storage_device
    :type dev: struct ps3_storage_device \*

    :param handler:
        Pointer to an interrupt handler
    :type handler: irq_handler_t

.. _`ps3stor_setup.description`:

Description
-----------

Returns 0 for success, or an error code

.. _`ps3stor_teardown`:

ps3stor_teardown
================

.. c:function:: void ps3stor_teardown(struct ps3_storage_device *dev)

    Tear down a storage device after use

    :param dev:
        Pointer to a struct ps3_storage_device
    :type dev: struct ps3_storage_device \*

.. _`ps3stor_read_write_sectors`:

ps3stor_read_write_sectors
==========================

.. c:function:: u64 ps3stor_read_write_sectors(struct ps3_storage_device *dev, u64 lpar, u64 start_sector, u64 sectors, int write)

    read/write from/to a storage device

    :param dev:
        Pointer to a struct ps3_storage_device
    :type dev: struct ps3_storage_device \*

    :param lpar:
        HV logical partition address
    :type lpar: u64

    :param start_sector:
        First sector to read/write
    :type start_sector: u64

    :param sectors:
        Number of sectors to read/write
    :type sectors: u64

    :param write:
        Flag indicating write (non-zero) or read (zero)
    :type write: int

.. _`ps3stor_read_write_sectors.description`:

Description
-----------

Returns 0 for success, -1 in case of failure to submit the command, or
an LV1 status value in case of other errors

.. _`ps3stor_send_command`:

ps3stor_send_command
====================

.. c:function:: u64 ps3stor_send_command(struct ps3_storage_device *dev, u64 cmd, u64 arg1, u64 arg2, u64 arg3, u64 arg4)

    send a device command to a storage device

    :param dev:
        Pointer to a struct ps3_storage_device
    :type dev: struct ps3_storage_device \*

    :param cmd:
        Command number
    :type cmd: u64

    :param arg1:
        First command argument
    :type arg1: u64

    :param arg2:
        Second command argument
    :type arg2: u64

    :param arg3:
        Third command argument
    :type arg3: u64

    :param arg4:
        Fourth command argument
    :type arg4: u64

.. _`ps3stor_send_command.description`:

Description
-----------

Returns 0 for success, -1 in case of failure to submit the command, or
an LV1 status value in case of other errors

.. This file was automatic generated / don't edit.

