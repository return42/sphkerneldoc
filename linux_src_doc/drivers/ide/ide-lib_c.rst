.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-lib.c

.. _`ide_dump_status`:

ide_dump_status
===============

.. c:function:: u8 ide_dump_status(ide_drive_t *drive, const char *msg, u8 stat)

    translate ATA/ATAPI error

    :param drive:
        drive that status applies to
    :type drive: ide_drive_t \*

    :param msg:
        text message to print
    :type msg: const char \*

    :param stat:
        status byte to decode
    :type stat: u8

.. _`ide_dump_status.description`:

Description
-----------

Error reporting, in human readable form (luxurious, but a memory hog).
Combines the drive name, message and status byte to provide a
user understandable explanation of the device error.

.. This file was automatic generated / don't edit.

