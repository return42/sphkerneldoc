.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-lib.c

.. _`ide_toggle_bounce`:

ide_toggle_bounce
=================

.. c:function:: void ide_toggle_bounce(ide_drive_t *drive, int on)

    handle bounce buffering

    :param ide_drive_t \*drive:
        drive to update

    :param int on:
        on/off boolean

.. _`ide_toggle_bounce.description`:

Description
-----------

Enable or disable bounce buffering for the device. Drives move
between PIO and DMA and that changes the rules we need.

.. _`ide_dump_status`:

ide_dump_status
===============

.. c:function:: u8 ide_dump_status(ide_drive_t *drive, const char *msg, u8 stat)

    translate ATA/ATAPI error

    :param ide_drive_t \*drive:
        drive that status applies to

    :param const char \*msg:
        text message to print

    :param u8 stat:
        status byte to decode

.. _`ide_dump_status.description`:

Description
-----------

Error reporting, in human readable form (luxurious, but a memory hog).
Combines the drive name, message and status byte to provide a
user understandable explanation of the device error.

.. This file was automatic generated / don't edit.

