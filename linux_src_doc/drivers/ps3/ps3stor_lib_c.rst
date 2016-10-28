.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ps3/ps3stor_lib.c

.. _`ps3stor_setup`:

ps3stor_setup
=============

.. c:function:: int ps3stor_setup(struct ps3_storage_device *dev, irq_handler_t handler)

    Setup a storage device before use

    :param struct ps3_storage_device \*dev:
        Pointer to a struct ps3_storage_device

    :param irq_handler_t handler:
        Pointer to an interrupt handler

.. _`ps3stor_setup.description`:

Description
-----------

Returns 0 for success, or an error code

.. _`ps3stor_teardown`:

ps3stor_teardown
================

.. c:function:: void ps3stor_teardown(struct ps3_storage_device *dev)

    Tear down a storage device after use

    :param struct ps3_storage_device \*dev:
        Pointer to a struct ps3_storage_device

.. _`ps3stor_read_write_sectors`:

ps3stor_read_write_sectors
==========================

.. c:function:: u64 ps3stor_read_write_sectors(struct ps3_storage_device *dev, u64 lpar, u64 start_sector, u64 sectors, int write)

    read/write from/to a storage device

    :param struct ps3_storage_device \*dev:
        Pointer to a struct ps3_storage_device

    :param u64 lpar:
        HV logical partition address

    :param u64 start_sector:
        First sector to read/write

    :param u64 sectors:
        Number of sectors to read/write

    :param int write:
        Flag indicating write (non-zero) or read (zero)

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

    :param struct ps3_storage_device \*dev:
        Pointer to a struct ps3_storage_device

    :param u64 cmd:
        Command number

    :param u64 arg1:
        First command argument

    :param u64 arg2:
        Second command argument

    :param u64 arg3:
        Third command argument

    :param u64 arg4:
        Fourth command argument

.. _`ps3stor_send_command.description`:

Description
-----------

Returns 0 for success, -1 in case of failure to submit the command, or
an LV1 status value in case of other errors

.. This file was automatic generated / don't edit.

