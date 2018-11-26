.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-iops.c

.. _`ide_in_drive_list`:

ide_in_drive_list
=================

.. c:function:: int ide_in_drive_list(u16 *id, const struct drive_list_entry *table)

    look for drive in black/white list

    :param id:
        drive identifier
    :type id: u16 \*

    :param table:
        list to inspect
    :type table: const struct drive_list_entry \*

.. _`ide_in_drive_list.description`:

Description
-----------

Look for a drive in the blacklist and the whitelist tables
Returns 1 if the drive is found in the table.

.. _`ide_execute_command`:

ide_execute_command
===================

.. c:function:: void ide_execute_command(ide_drive_t *drive, struct ide_cmd *cmd, ide_handler_t *handler, unsigned timeout)

    execute an IDE command

    :param drive:
        IDE drive to issue the command against
    :type drive: ide_drive_t \*

    :param cmd:
        command
    :type cmd: struct ide_cmd \*

    :param handler:
        handler for next phase
    :type handler: ide_handler_t \*

    :param timeout:
        timeout for command
    :type timeout: unsigned

.. _`ide_execute_command.description`:

Description
-----------

Helper function to issue an IDE command. This handles the
atomicity requirements, command timing and ensures that the
handler and IRQ setup do not race. All IDE command kick off
should go via this function or do equivalent locking.

.. This file was automatic generated / don't edit.

